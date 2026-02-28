import typst, pypandoc, sys, json, yaml, subprocess, os, shutil

typstpath = sys.argv[1]
issue = sys.argv[2]
global footnotes
global images

def parseContent(content):
    if "text" in content.keys() and content["func"] != "raw":
        return content["text"]
    elif content["func"] == "strong":
        return f"**{parseContent(content["body"])}**"
    elif content["func"] == "emph":
        return f"_{parseContent(content["body"])}_"
    elif content["func"] == "heading":
        hn = "#" * int(content["depth"])
        return f"{hn} {parseContent(content["body"])}\n\n"
    elif content["func"] == "space":
        return " "
    elif content["func"] == "smartquote":
        return "\""
    elif content["func"] == "parbreak":
        return "\n\n"
    elif content["func"] == "linebreak":
        return "\n"
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
        return f"{{% include figure.html image='{parseContent(content['body'])}' caption='{parseContent(content['caption'])}' width=700 %}}"
    elif content["func"] == "image":
        return content["source"].split("/")[-1]
    elif content["func"] == "quote":
        return f"> {parseContent(content['body'])}"
    elif content["func"] == "footnote":
        footnotes.append(parseContent(content['body']))
        return f"[^{len(footnotes)-1}]"
    elif content["func"] == "line":
        return "\n---\n"
    elif content["func"] == "super":
        return f"$$^{{{parseContent(content["body"])}}}$$"
    elif content["func"] == "colbreak" or content["func"] == "counter-update":
        return ""
    elif content["func"] == "item":
        return f"\n+ {parseContent(content["body"])}"
    elif content["func"] == "grid":
        caption = input(f"Enter caption for {content}:")
        images.append(parseContent(content['children'][0]['body']))
        return f"{{% include figure.html image='{parseContent(content['children'][0]['body'])}' caption='{caption}' width=700 %}}\n"
    elif content["func"] == "v":
        return "<br>"
    elif content["func"] == "raw":
        math = f"${content['text']}$"
        if content["block"]:
            math = f"$ {content['text']} $"
        latex = subprocess.run(
             ["pandoc", "-f", "typst", "-t", "latex"],
             input=math,
             text=True,
             capture_output=True
         ).stdout.strip()
        if latex[:2] == "\\(":
            latex = "$$" + latex[2:-2] + "$$"
        else:
            latex = "\n$$" + latex[2:-2] + "$$\n"
        return latex
    else:
        assert False, f"unhandled function -- {content}"



vars = json.loads(typst.query(typstpath, "<vars>"))
contents = json.loads(typst.query(typstpath, "<content>", sys_inputs={"html": "true"}))
refsDir = os.path.join("_data", "references")
os.makedirs(refsDir, exist_ok=True)
for (content, var) in zip(contents, vars):
    if var["value"]["type"] == "article" or var["value"]["type"] == "interview":
        footnotes = []
        images = []
        if var["value"]["type"] == "article":
            metaData = {
                    "title": str(var["value"]["title"]),
                    "authors": var["value"]["authors"],
                    "author-affiliation": var["value"]["authorAffiliations"],
                    "author-bio": var["value"]["authorInfo"],
                    "excerpt": var["value"]["abstract"],
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    "authorImage": var["value"]["authorImage"].split("/")[-1],
                    "date": var["value"]["received"],
                    "refs-file": var["value"]["refsFile"],
                    "category": var["value"]["type"],
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    }
            if metaData["refs-file"] != None:
                metaData["refs-file"] = metaData["refs-file"].split("/")[-1].replace("yaml", "yml")
                shutil.copy2(os.path.join(os.path.dirname(typstpath), "dataFiles", os.path.basename(var["value"]["refsFile"])), os.path.join(refsDir, metaData["refs-file"]))
        else:
            metaData = {
                    "title": var["value"]["title"],
                    "authors": var["value"]["authors"],
                    "author-affiliation": var["value"]["authorAffiliations"],
                    "author-bio": var["value"]["authorInfo"],
                    "excerpt": var["value"]["abstract"],
                    "hero-image": var["value"]["coverImage"].split("/")[-1],
                    "authorImage": var["value"]["authorImage"].split("/")[-1],
                    "date": var["value"]["received"],
                    "category": var["value"]["type"],
                    "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                    }
        imgDir = os.path.join("assets", "images", metaData["permalink"][1:])
        os.makedirs(imgDir, exist_ok=True)
        metaData["issue"] = int(issue)
        filename = f"{metaData['date']['year']}-{metaData['date']['month']}-{metaData['date']['day']}-{metaData['permalink'].split('/')[2]}.md"
        print(filename)
        markdown = []
        broken = False
        for data in content["value"]["children"]:
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
            if line == "\n\n" and markdown[i+1] == "\n\n":
                markdown[i+1] = ""
            elif len(line) > 2 and line[-2:] == "\n\n" and markdown[i+1] == "\n\n":
                markdown[i+1] = ""
            elif line == "\n\n" and len(markdown[i+1]) > 2 and markdown[i+1][:2] == "\n\n":
                markdown[i] = ""
        if len(footnotes) > 0:
            markdown.append("\n")
            markdown.append("\n## Footnotes")
            for (i, note) in enumerate(footnotes):
                markdown.append(f"\n[^{i+1}]: {note}\n")

        with open(filename, 'w') as outfile:
            outfile.write("---\n")
            yaml.dump(metaData, outfile, default_flow_style=False, width=9999)
            outfile.write("---")
            outfile.write("".join(markdown))
