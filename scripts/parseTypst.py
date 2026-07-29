import typst
import pypandoc
import sys
import json
import yaml
import tomllib
import subprocess
import os
import shutil
from datetime import date

typstpath = sys.argv[1]
issue = sys.argv[2]
escapeChars = {'|': "&#124;",
               '|': "&#124;",
               '>': "&gt;",
               '{': "&#123;",
               }
global footnotes
global images

def parseContent(content):
    if content is None:
        return ""
    if "text" in content.keys() and content["func"] != "raw":
        text = content["text"]
        for (char, escapeChar) in escapeChars.items():
            text = text.replace(char, escapeChar)
        return text
    elif content["func"] == "link":
        return f"[{content['dest']}]({parseContent(content['body']).strip()})"
    elif content["func"] == "strong":
        return f"**{parseContent(content['body']).strip()}**"
    elif content["func"] == "emph":
        return f"_{parseContent(content['body'])}_"
    elif content["func"] == "heading":
        hn = "#" * int(content["depth"])
        return f"\n\n{hn} {parseContent(content['body'])}\n\n"
    elif content["func"] == "space":
        return " "
    elif content["func"] == "smartquote":
        return "\"" if content["double"] else "'"
    elif content["func"] == "parbreak":
        return "\n\n"
    elif content["func"] == "linebreak":
        return "<br>\n"
    elif content["func"] == "place" or content["func"] == "rect" or content["func"] == "box":
        return parseContent(content['body'])
    elif content["func"] == "caption":
        if content['body']["func"] == "emph":
            return parseContent(content['body']['body'])
        else:
            return parseContent(content['body'])
    elif content["func"] == "styled":
        return parseContent(content["child"])
    elif content["func"] == "sequence":
        return "".join([parseContent(ele) for ele in content["children"]])
    elif content["func"] == "figure":
        images.append(parseContent(content['body']))
        if images[-1].endswith(".pdf"):
            print(f"PDF image {images[-1]} in {filename}. I replaced it with `.svg'. Please add svg image.")
        return "{% include figure.html image='" + parseContent(content['body']).replace(".pdf", ".svg") + "' caption='" + parseContent(content['caption']).replace("{", "\\{").replace("}", "\\}").replace("'", "\\'") + "' width=800 %}\n\n"
    elif content["func"] == "image":
        return content["source"].strip("//")
    elif content["func"] == "quote":
        if content['body']['func'] == "sequence":
            quote = "\n\n"
            line = ""
            for child in content['body']['children']:
                if child['func'] != "parbreak":
                    line += parseContent(child)
                else:
                    quote += f"> {line.strip()}\n"
                    quote += f"> \n"
                    line = ""
            if quote == "\n\n":
                quote += f"> {line.strip()}\n"
            quote += "\n"
            return quote
        else:
            return f"\n\n> {parseContent(content['body'])}\n\n"
    elif content["func"] == "footnote":
        footnotes.append(parseContent(content['body']))
        return f"[^{len(footnotes)}]"
    elif content["func"] == "line":
        return "\n\n---\n\n"
    elif content["func"] == "super":
        return f"$$^{{{parseContent(content['body'])}}}$$"
    elif content["func"] == "colbreak" or content["func"] == "counter-update":
        return ""
    elif content["func"] == "item":
        return f"\n+ {parseContent(content['body'])}"
    elif content["func"] == "grid":
        captionBody = content["children"][1]['body']['body']["children"][5]
        assert captionBody["func"] == "emph"
        images.append(parseContent(content['children'][0]['body']))
        if images[-1].endswith(".pdf"):
            print(f"PDF image {images[-1]} in {filename}. I replaced it with `.svg'. Please add svg image.")
        return "{% include figure.html image='" + parseContent(content['children'][0]['body']).replace(".pdf", ".svg") + "' caption='" + parseContent(captionBody['body']).replace("{", "\\{").replace("}", "\\}").replace("'", "\\'") + "' width=800 %}\n\n"
    elif content["func"] == "v":
        return "<br>"
    elif content["func"] == "raw":
        math = f"${content['text']}$"
        if content["block"]:
            math = f"$ {content['text']} $"
        math = math.replace("&", "").replace("\\ ", "").replace("\\\n", "")
        latex = subprocess.run(
             ["pandoc", "-f", "typst", "-t", "latex"],
             input=math,
             text=True,
             capture_output=True
         ).stdout.strip()
        if latex[:2] == "\\(":
            latex = "$$" + latex[2:-2] + "$$"
        else:
            latex = "\n\n$$" + latex[2:-2] + "$$\n\n"
        latex = latex.replace("\\begin{array}{r}", "\\begin{array}{c}")
        return latex
    elif content["func"] == "align":
        return parseContent(content["body"])
    elif content["func"] == "context":
        return ""
    else:
        assert False, f"unhandled function -- {content}"



vars = json.loads(typst.query(typstpath, "<vars>"))
contents = json.loads(typst.query(typstpath, "<content>", sys_inputs={"html": "true"}))
postsDir = os.path.join("_posts", f"Issue{issue}")
refsDir = os.path.join("_data", "references")
os.makedirs(postsDir, exist_ok=True)
os.makedirs(refsDir, exist_ok=True)
for (content, var) in zip(contents, vars):
    print(var["value"]["title"])
    if var["value"]["type"] == "article" or var["value"]["type"] == "interview" or var["value"]["type"] == "editor" or var["value"]["type"] == "foreword" or var["value"]["type"] == "quiz" or var["value"]["type"] == "linkedlist" or var["value"]["type"] == "crossword" or var["value"]["type"] == "digest" or var["value"]["type"] == "comic":
        footnotes = []
        images = []
        Date = date.today().strftime("%Y-%m-%d")
        if var["value"]["type"] == "article":
            Date = f'{var["value"]["received"]["year"]}-{var["value"]["received"]["month"]}-{var["value"]["received"]["day"]}'
            metaData = {
                    "title": var["value"]["title"],
                    "authors": var["value"]["authors"],
                    "author-affiliation": var["value"]["authorAffiliations"],
                    "author-bio": "<br><br>".join([parseContent(v) for v in var["value"]["authorInfo"]]),
                    "excerpt": parseContent(var["value"]["abstract"]),
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    "authorImage": var["value"]["authorImage"].split("/")[-1],
                    "date": Date,
                    "refs-file": var["value"]["refsFile"],
                    "category": var["value"]["type"],
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    "reviewed-by": var["value"]["reviewedBy"],
                    }
            if metaData["refs-file"] != None:
                metaData["refs-file"] =os.path.splitext(metaData["refs-file"].split("/")[-1])[0]
                shutil.copy2(os.path.join(os.path.dirname(typstpath), "dataFiles", os.path.basename(var["value"]["refsFile"])), os.path.join(refsDir, os.path.basename(var["value"]["refsFile"])))
        elif var["value"]["type"] == "interview":
            Date = f'{var["value"]["received"]["year"]}-{var["value"]["received"]["month"]}-{var["value"]["received"]["day"]}'
            metaData = {
                    "title": var["value"]["title"],
                    "authors": var["value"]["authors"],
                    "author-affiliation": var["value"]["authorAffiliations"],
                    "author-bio": "<br><br>".join([parseContent(v) for v in var["value"]["authorInfo"]]),
                    "excerpt": parseContent(var["value"]["abstract"]),
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    "authorImage": var["value"]["authorImage"].split("/")[-1],
                    "date": Date,
                    "category": var["value"]["type"],
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    }
        elif var["value"]["type"] == "editor" or var["value"]["type"] == "foreword":
            metaData = {
                    "title": var["value"]["title"],
                    "excerpt": parseContent(var["value"]["abstract"]),
                    "category": "meta",
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    }
        elif var["value"]["type"] == "quiz" or var["value"]["type"] == "linkedlist" or var["value"]["type"] == "crossword":
            metaData = {
                    "title": var["value"]["title"],
                    "authors": parseContent(var["value"]["authors"]),
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    }
            dataDir = os.path.join("_data", {"quiz": "quizzes", "linkedlist": "linkedlists", "crossword": "crosswords"}[var["value"]["type"]])
            os.makedirs(dataDir, exist_ok=True)
            if var["value"]["type"] == "crossword":
                data = tomllib.loads(open(os.path.join(os.path.dirname(typstpath), "dataFiles", os.path.basename(var["value"]["file"])), "r").read())
                json.dump(data, open(os.path.join(dataDir, f"issue{issue}.json"), "w"), indent=4)
            else:
                shutil.copy2(os.path.join(os.path.dirname(typstpath), "dataFiles", os.path.basename(var["value"]["file"])), os.path.join(dataDir, f"issue{issue}.yml"))
        elif var["value"]["type"] == "digest": 
            metaData = {
                    "title": var["value"]["title"],
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    "category": "digest",
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    }
            for v in yaml.safe_load(open(os.path.join(os.path.dirname(typstpath), "dataFiles", os.path.basename(var["value"]["file"])), "r")):
                images.append(v["Image"])
            # print(images)
            os.makedirs(os.path.join("_data", "digest"), exist_ok=True)
            shutil.copy2(os.path.join(os.path.dirname(typstpath), "dataFiles", os.path.basename(var["value"]["file"])), os.path.join("_data", "digest", f"issue{issue}.yml"))
        elif var["value"]["type"] == "comic": 
            metaData = {
                    "title": var["value"]["title"],
                    "authors": var["value"]["authors"],
                    "author-affiliation": var["value"]["authorAffiliations"],
                    "author-bio": "<br><br>".join([parseContent(v) for v in var["value"]["authorInfo"]]),
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    "authorImage": var["value"]["authorImage"].split("/")[-1],
                    "date": Date,
                    "category": var["value"]["type"],
                    "permalink": f"/issue{issue}/{var["value"]["permalink"]}",
                    "pages": var["value"]["pages"]
                    }
            images = images + var["value"]["pages"]
          # title: "Against All Odds -- The Man Who Brought IVF To India"
          # authors: ['Kajori Barman', 'Afreen Chowdhury']
          # author-bio: "*Kajori* (right) is a student with curiosity in the sciences. Along with pursuing her interest in science, she also indulges in sketching and painting as hobbies. During the lockdown, she started getting into digital art and has since been drawing her favourite anime and comic characters. #linebreak() *Afreen* (left)  has always been very keen about nature, particularly biology. She has always loved reading novels and comics, and as someone who nerds on fiction, she wanted to try understanding how these stories are written by creating this comic with Kajori."
          # issue: 7
          # author-affiliation: ['IISER Kolkata']
          # hero-image: "comic.svg"
          # authorImage: "kajori.jpg"
          # date: "2025-11-12"
          # category: "comic"
          # permalink: "/issue7/comic-kajori/"
          # pages: ["comic_2.jpg", "comic_3.jpg", "comic_4.jpg", "comic_5.jpg", "comic_6.jpg", "comic_7.jpg", "comic_8.jpg", "comic_9.jpg"]

        imgDir = os.path.join("assets", "images", metaData["permalink"][1:])
        os.makedirs(imgDir, exist_ok=True)
        metaData["issue"] = int(issue)
        filename = os.path.join(postsDir, f"{Date}-{metaData['permalink'].split('/')[2]}.md")
        markdown = []
        broken = False
        contents = json.loads(typst.query(typstpath, "<content>", sys_inputs={"html": "true"}))
        if "images" in var["value"]:
            img = var["value"]["images"][0]
            markdown.append("\n{% include figure.html image='" + os.path.basename(img) + "' caption='" + parseContent(var["value"]["captions"][0]) + "' width=400 %}\n")
            images.append(img.strip("//"))
        for data in content["value"]["children"]:
            # print(data)
            if data == {'func': 'v', 'amount': '1.4em'}:
                data = {'func': 'parbreak'}
            parsed = parseContent(data)
            # print(parsed)
            if parsed.startswith(" {% include figure.html"):
                parsed = parsed[1:]
            if parsed.startswith(" ") and len(parsed) > 1:
                parsed = parsed[1:]
            if parsed.endswith(" ") and len(parsed) > 1:
                parsed = parsed[:-1]
            markdown.append(parsed)
        if "images" in var["value"]:
            img = var["value"]["images"][1]
            markdown.append("\n{% include figure.html image='" + os.path.basename(img) + "' caption='" + parseContent(var["value"]["captions"][1]) + "' width=400 %}\n")
            images.append(img.strip("//"))
        for img in images:
            print(img)
            if os.path.basename(img) == img:
                shutil.copy2(os.path.join(os.path.dirname(typstpath), "images", img), imgDir)
            else:
                shutil.copy2(os.path.join(os.path.dirname(typstpath), img), imgDir)
        if "hero-image" in metaData:
            shutil.copy2(os.path.join(os.path.dirname(typstpath), "covers", metaData["hero-image"]), imgDir)
        if "authorImage" in metaData:
            shutil.copy2(os.path.join(os.path.dirname(typstpath), "authFaces", metaData["authorImage"]), imgDir)
        

        for (i, line) in enumerate(markdown[:-1]):
            seps = ["<br>\n", "\n\n"]
            if line in seps:
                if markdown[i+1] in seps:
                    markdown[i+1] = ""
                elif (len(markdown[i+1]) > len(seps[0]) and markdown[i+1][:len(seps[0])] == seps[0]) or (len(markdown[i+1]) > len(seps[1]) and markdown[i+1][:len(seps[1])] == seps[1]): 
                    markdown[i+1] = markdown[i+1][len(seps[1]):]
            elif markdown[i+1] in seps:
                if (len(line) > len(seps[0]) and line[-len(seps[0]):] == seps[0]) or (len(line) > len(seps[1]) and line[-len(seps[1]):] == seps[1]): 
                    markdown[i+1] = ""

        with open(filename, 'w') as outfile:
            outfile.write("---\n")
            yaml.dump(metaData, outfile, default_flow_style=False, width=9999)
            outfile.write("---\n")
            outfile.write("".join(markdown))
            if len(footnotes) > 0:
                outfile.write("\n\n---\n\n")
                for (i, note) in enumerate(footnotes):
                    outfile.write(f"\n[^{i+1}]: {note}\n")
