#!~/python
import typst, pypandoc, sys, json, yaml, subprocess, os, shutil

typstpath = sys.argv[1]
issue = sys.argv[2]
escapeChars = {'|': "&#124;",
               '|': "&#124;",
               '>': "&gt;",
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
        return f"[{content['dest']}]({parseContent(content["body"]).strip()})"
    elif content["func"] == "strong":
        return f"**{parseContent(content["body"]).strip()}**"
    elif content["func"] == "emph":
        return f"_{parseContent(content["body"])}_"
    elif content["func"] == "heading":
        hn = "#" * int(content["depth"])
        return f"\n\n{hn} {parseContent(content["body"])}\n\n"
    elif content["func"] == "space":
        return " "
    elif content["func"] == "smartquote":
        return "\""
    elif content["func"] == "parbreak":
        return "\n\n"
    elif content["func"] == "linebreak":
        return "<br>\n"
    elif content["func"] == "place" or content["func"] == "rect" or content["func"] == "box":
        return parseContent(content["body"])
    elif content["func"] == "caption":
        if content["body"]["func"] == "emph":
            return parseContent(content["body"]["body"])
        else:
            return parseContent(content["body"])
    elif content["func"] == "styled":
        return parseContent(content["child"])
    elif content["func"] == "sequence":
        return "".join([parseContent(ele) for ele in content["children"]])
    elif content["func"] == "figure":
        images.append(parseContent(content['body']))
        if images[-1].endswith(".pdf"):
            print(f"PDF image {images[-1]} in {filename}. I replaced it with `.svg'. Please add svg image.")
        return f"{{% include figure.html image='{parseContent(content['body']).replace(".pdf", ".svg")}' caption='{parseContent(content['caption'])}' width=800 %}}\n\n"
    elif content["func"] == "image":
        return content["source"].split("/")[-1]
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
        return f"$$^{{{parseContent(content["body"])}}}$$"
    elif content["func"] == "colbreak" or content["func"] == "counter-update":
        return ""
    elif content["func"] == "item":
        return f"\n+ {parseContent(content["body"])}"
    elif content["func"] == "grid":
        captionBody = content["children"][1]["body"]["body"]["children"][5]
        assert captionBody["func"] == "emph"
        caption = parseContent(captionBody["body"])
        images.append(parseContent(content['children'][0]['body']))
        return f"{{% include figure.html image='{parseContent(content['children'][0]['body'])}' caption='{caption}' width=700 %}}\n"
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
    else:
        assert False, f"unhandled function -- {content}"



vars = json.loads(typst.query(typstpath, "<vars>"))
contents = json.loads(typst.query(typstpath, "<content>", sys_inputs={"html": "true"}))
postsDir = os.path.join("_posts", f"issue{issue}")
refsDir = os.path.join("_data", "references")
os.makedirs(postsDir, exist_ok=True)
os.makedirs(refsDir, exist_ok=True)
for (content, var) in zip(contents, vars):
    if var["value"]["type"] == "article" or var["value"]["type"] == "interview":
        footnotes = []
        images = []
        date = f'{var["value"]["received"]["year"]}-{var["value"]["received"]["month"]}-{var["value"]["received"]["day"]}'
        if var["value"]["type"] == "article":
            metaData = {
                    "title": var["value"]["title"],
                    "authors": var["value"]["authors"],
                    "author-affiliation": var["value"]["authorAffiliations"],
                    "author-bio": "<br><br>".join([parseContent(v) for v in var["value"]["authorInfo"]]),
                    "excerpt": parseContent(var["value"]["abstract"]),
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    "authorImage": var["value"]["authorImage"].split("/")[-1],
                    "date": date,
                    "refs-file": var["value"]["refsFile"],
                    "category": var["value"]["type"],
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    }
            if metaData["refs-file"] != None:
                metaData["refs-file"] =os.path.splitext(metaData["refs-file"].split("/")[-1])[0]
                shutil.copy2(os.path.join(os.path.dirname(typstpath), "dataFiles", os.path.basename(var["value"]["refsFile"])), os.path.join(refsDir, os.path.basename(var["value"]["refsFile"])))
        else:
            metaData = {
                    "title": var["value"]["title"],
                    "authors": var["value"]["authors"],
                    "author-affiliation": var["value"]["authorAffiliations"],
                    "author-bio": "<br><br>".join([parseContent(v) for v in var["value"]["authorInfo"]]),
                    "excerpt": parseContent(var["value"]["abstract"]),
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    "authorImage": var["value"]["authorImage"].split("/")[-1],
                    "date": date,
                    "category": var["value"]["type"],
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    }
        imgDir = os.path.join("assets", "images", metaData["permalink"][1:])
        os.makedirs(imgDir, exist_ok=True)
        metaData["issue"] = int(issue)
        filename = os.path.join(postsDir, f"{date}-{metaData['permalink'].split('/')[2]}.md")
        print(filename)
        markdown = []
        broken = False
        for data in content["value"]["children"]:
            if data == {'func': 'v', 'amount': '1.4em'}:
                data = {'func': 'parbreak'}
            parsed = parseContent(data)
            if parsed.startswith(" {% include figure.html"):
                parsed = parsed[1:]
            if parsed.startswith(" ") and len(parsed) > 1:
                parsed = parsed[1:]
            if parsed.endswith(" ") and len(parsed) > 1:
                parsed = parsed[:-1]
            markdown.append(parsed)
        for img in images:
            shutil.copy2(os.path.join(os.path.dirname(typstpath), "images", img), imgDir)
        shutil.copy2(os.path.join(os.path.dirname(typstpath), "covers", metaData["hero-image"]), imgDir)
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
