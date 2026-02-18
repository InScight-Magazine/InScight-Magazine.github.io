import typst, pypandoc, sys, json, yaml, subprocess, os

typstpath = sys.argv[1]
issue = sys.argv[2]
global footnotes

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
    elif content["func"] == "caption" or content["func"] == "place" or content["func"] == "rect" or content["func"] == "box":
        return parseContent(content["body"])
    elif content["func"] == "styled":
        return parseContent(content["child"])
    elif content["func"] == "sequence":
        return "".join([parseContent(ele) for ele in content["children"]])
    elif content["func"] == "figure":
        return f"{{% include figure.html image='/{parseContent(content['body'])}' caption='{parseContent(content['caption'])}' width=700 %}}\n"
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
        return f"{{% include figure.html image='/{parseContent(content['children'][0]['body'])}' caption='{caption}' width=700 %}}\n"
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
for (content, var) in zip(contents, vars):
    if var["value"]["type"] == "article":
        footnotes = [""]
        metaData = {
                "title": var["value"]["title"],
                "authors": var["value"]["authors"],
                "author-affiliation": var["value"]["authorAffiliations"],
                "excerpt": var["value"]["abstract"],
                "hero-image": var["value"]["coverImage"].split("/")[-1],
                "authorImage": var["value"]["authorImage"],
                "date": var["value"]["received"],
                "refs-file": var["value"]["refsFile"],
                "category": var["value"]["type"],
                "permalink": var["value"]["permalink"].replace("https://scicomm.iiserkol.ac.in", "") + "/",
                }
        if metaData["refs-file"] != None:
            metaData["refs-file"] = os.path.splitext(metaData["refs-file"].split("/")[-1])[0]
        filename = f"{metaData['date']['year']}-{metaData['date']['month']}-{metaData['date']['day']}-{metaData['permalink'].split('/')[2]}.md"
        print(filename)
        markdown = []
        broken = False
        for data in content["value"]["children"]:
            markdown.append(parseContent(data))
        if len(footnotes) > 1:
            markdown.append("\n")
            for (i, note) in enumerate(footnotes[1:]):
                markdown.append(f"\n[^{i+1}]: {note}\n")

        with open(filename, 'w') as outfile:
            outfile.write("---\n")
            yaml.dump(metaData, outfile, default_flow_style=False)
            outfile.write("---")
            outfile.write(" ".join(markdown))
