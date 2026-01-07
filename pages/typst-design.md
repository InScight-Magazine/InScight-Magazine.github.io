---
title: "Typst Design Guidelines for InScight"
permalink: /typst-design/
---

This page lists the steps necessary to get started with typesetting articles for _InScight_. The typesetting engine used is [typst](https://typst.app/), a modern alternative to LaTeX. All files necessary for the task can be found on our [github repo](https://github.com/InScight-Magazine/Print-Templates).

## Setting up the system

- Download the _InScight_ typst [template repository](https://github.com/InScight-Magazine/Print-Templates/) from github. Extract into a folder if it's downloaded as a compressed archive.

- Copy the appropriate typst binary for your operating system (Windows vs Unix) from the `typst-binaries` folder and place it in your system's path.

- Install all the fonts from the `fonts` folder. 

    - On Windows, this involves going into each font subfolder (such as `neuton`), selecting all files in the folder, right clicking to bring the context menu and then selecting `Install font`.

    - On Unixish systems, it is enough to copy the contents of the `fonts` folder into `~/.fonts`.

- Having copied the typst binary and installed all fonts, remove the `fonts` and `typst-binaries` folders. The remaining contents of the folder (which we'll call `templates` from now) serve as the base for each issue of _InScight_.

## Structure of The Templates Folder
It might be useful to know your way around the various folders.
- `template-files`: Various typst templates and helper functions that are applied on the provided content to generate the actual pdf of the magazine. Please do not edit these files as it would make the styling inconsistent across pages.

- `subfiles`: These are issue-specific files that contain the actual content material for the issue, such as the articles, games, comics, editor's word, foreword, etc.

- `dataFiles`: These files contain data used to generate certain parts of the magazine. Examples include the `issueData.yml` file that contains the issue number and release date of the present issue, the `openings.csv` file that stores data about various academic job opportunities (we display them within the magazine), various bibliography files that list the references cited in articles (each article gets its own reference file), various interview files that contain the questions and answers for interviews, etc.

- `images`: Contains all non-header image files used throughout the magazine. These include files used in the bodies of articles, interviews, games, etc.

- `covers`: Contains all header/cover image files. These images are used as the title image of each article or interview or other content. Think of these as banner or teaser images.

- `authFaces`: Contains images of authors. These images are displayed within the article, alongside a short author biography.


## Getting Started With A Particular Issue Of InScight
You'll typically be asked to design multiple pieces of content during the course any given issue. 

- When you are about to start designing the first item for an issue, copy the contents of the `templates` folder and rename it appropriately (say `Issue7`). 

- Most of the folders will contain files from the previous issue --- retain those files if you want to use them as base for creating new files for the coming issue, otherwise delete them.

- Update the `issueData.yml` file to reflect the appropriate issue number and release month.

- If not already present, create a main file at the root of the folder, say `full.typ`. This fill will call all other subfiles and create the full issue. The `full.typ` file has the following structure:

```typst
#import "template-files/inscight-template.typ": *

#show: default.with(
  issueDetails: yaml("/dataFiles/issueData.yml"),
)

#include "/subfiles/front.typ"

// include rest of the files as well.
```

- In order to design a particular category of content, it's best to copy a similar category file from the previous issue and modify it. For example, to start designing an article, copy an article file from the previous issue into the `subfiles` folder of the present issue and begin modifying it according to the content.

- In order to compile the article file you are designing and see what the pdf looks like, make sure that the specific file you are designing is included in the `full.typ` file, using something like `#include "/subfiles/article.typ"`, where `article.typ` has to be replaced with the name of the file you are editing. Once this file is included within `full.typ`, start a terminal in the same folder where the `full.typ` exists, and run `typst watch full.typ`. It will watch the `full.typ` file and recompiles on changes, producing a `full.pdf` file.

Instruction for designing specific types of content are provided below.

## Designing Articles
Copy an article file from the previous issue and rename it appropriately. Before adding the actual article content into the file, copy the following files into the project:
- Image files used within the article. Copy these into `images`. Consider using a simple naming scheme such as `article-1.png`, `article-2.jpg`, `article-3.png`, etc, where `article` is to be replaced with the name of the `.typ` file for the article.

- If there are references within the article, copy them into a `.yml` file with the appropriate format (check past files) and copy it into the `dataFiles` folder.

- If there are tables within the article, copy each table into a `.csv` file and copy those into the `dataFiles` folder as well.

- Copy the author image and cover image into the appropriate folders as well.

Having prepared all files, we start editing the actual article file. At the top of the file, the following variables _must_ be set in distinct lines:
- `title`: _String_. Can contain markdown (enclose words within underscore or asterisk to make them italic or bold).

- `authors`: _Array_. Examples: `#let authors = ("Abhirup Mukherjee",)` for single author (note the trailing comma after the name to ensure the object is an array), `#let authors = ("Abhirup Mukherjee", "Swarnendu Saha")` for multiple authors.

- `affiliations`: _Array_. Similar structure as `authors`.

- `abstract`: _String_. Can contain markdown. Typically restricted to two sentences. Acts as a pitch for the article.

- `coverImage`: _String_. Name of the file for the cover image. Example: `#let coverImage = "sunrise.png"`. Ensure that the file `/covers/sunrise.png` exists.

- `authorImage`: _String_. Name of the file for the author image. Similar example, but in the folder `authFaces`.

- `authorInfo`: _String_. Short bio of author. Can contain markdown.

- `received`: _Dictionary_. Specified the date when the article was submitted to InScight. Example: `#let received = (month: 10, day: 12, year: 2025)`.

- `reviewedBy`: _Array_. List of names who reviewed the article. Similar structure as the `authors` array.

- `refsFile`: _String_. Name of the reference file that was copied to the `dataFiles` folder.

After setting the metadata, the next thing to note is the function call `#section`. This function provides the layout of the page and draws the headers and footer. Many of the arguments in the function call don't need to be touched. The ones that might need adjustment are:

- `coverCaption`: _String_. Set this if you want to add a caption to the cover image in an interview. Has no effect in an article.

- `sideImageFraction`: _Percentage_. For example: `sideImageFraction: 35%`. For an interview, sets the width of the interviewee image on the title page. `sideImageFraction: 100%` means the entire right half will be covered by the interviewee image.

- `breakAfter`: _Array_ of integers. Indicates when to apply column breaks in the references. For example: `breakAfter: (7,10)` means that columns breaks will be applied after the seventh and tenth references. Useful for distributing the list of references into multiple columns.

After the call to the `section` function, it is _imperative_ that you add a line of that contains only 

```
// begin
```

Within typst, it is commented out so it won't affect the pdf, but it will be picked up by our typst-to-html converter to note that this is where the article content begins.

We now begin designing the actual content of the article. The first letter of the first paragraph must be a drop-cap, which is applied by passing the paragraph into the `#dropcap` function as a string:

```
#dcap("Lorem ipsum dolor sit amet, consectetur adipiscing elit")
```

The following formatting options are available:
- Section headings of the article are specified using the `==` symbol: `== This is a section heading`.

- Bold and italic: `This is *bold*, this is _italic_`.

Images are inserted using the function `#img`. A typical call is of the form

```
#img(path: "/images/apurba1.svg", caption: "Drosophila as a model organism..", 
     position: top, width: 100%, portrait: true)
```

The `path` and `caption` arguments are self-explanatory. The `position` argument can take values `top` or `bottom`, and dictates the placement of the image. The `portrait` variable can be `true` or `false`. Setting it `true` means that the image will be restricted one of the columns of the article, whereas `false` allows the possibility of the image stretching to cover both columns. The `width` argument specifies the width covered by the image. If `portrait` is `true`, setting `width` to `100%` means the image will cover the entirety of a single column and the caption will appear below it. If `portrait` is `false`, a width greater than `66.6%` means the image will span both columns and the caption will appear below it, spanning both columns. A width between `33.3%` and `66.6%` will make the caption appear to the right of the image, and the image+caption together will span both columns. Setting the width to less than `33.3%` is equivalent to setting `portrait = true`.

Equations can be added by enclosing them using the \$ symbol. Inline equations have the form `$x=y$`, while adding spaces at the start and end ensure the equation is rendered in its own line: `$ x = y $`. Check out [this link](https://qwinsi.github.io/tex2typst-webapp/cheat-sheet.html) for a list of the available math functions.


This should cover most of the things that one needs to know to design an article.

## Designing Interviews
Copy an interview file (`interiewXYZ.typ`) from the previous issue and rename it appropriately. Also copy the following files into the project:
- Text file containing the interview content, into the `dataFiles` folder. The structure for this text file is described below.

- Image files used within the interview. Copy these into `images`. Consider using a simple naming scheme such as `interviewXYZ-1.png`, `interviewXYZ-2.jpg`, `interviewXYZ-3.png`, etc, where `interviewXYZ` is to be replaced with the name of the `.typ` file for the article.

- An image of the interviewee, into the `images` folder.

- Copy the cover image into the `covers` folder.

Having prepared all files, we start editing the `interiewXYZ.typ` file. At the top of the file, the following variables _must_ be set in distinct lines:
- `title`: _String_. Can contain markdown (enclose words within underscore or asterisk to make them italic or bold).

- `file`: _String_. Path of the text file containing the interview content (this file was copied above). Example: `#let file = "/dataFiles/interviewAAN.txt"`.

- `authors`: _Array_. Name of interviewer. Examples: `#let authors = ("Abhirup Mukherjee",)` for single author (note the trailing comma after the name to ensure the object is an array), `#let authors = ("Abhirup Mukherjee", "Swarnendu Saha")` for multiple authors.

- `affiliations`: _Array_. Similar structure as `authors`.

- `abstract`: _String_. Can contain markdown. Typically restricted to two sentences. Acts as a pitch for the interview.

- `coverImage`: _String_. Name of the file for the cover image. Example: `#let coverImage = "sunrise.png"`. Ensure that the file `/covers/sunrise.png` exists.

- `received`: _Dictionary_. Specified the date when the article was submitted to InScight. Example: `#let received = (month: 10, day: 12, year: 2025)`.

- `group1`: _Array_. List of codenames for the interviewers as used in the text file. Example: `#let group1 = ("SS:",)`.

- `group2`: _String_. Codenames for the interviewee, as used in the text file. Example: `#let group2 = "AAN:"`.

- `sideImage`: _String_. Path for the image of the interviewee. Example `#let sideImage = "/images/AAN.jpg"`.

After setting the metadata, the next thing to note is the function call `#section`. This function provides the layout of the page and draws the headers and footer. Many of the arguments in the function call don't need to be touched. The ones that might need adjustment are:

- `sideImageFraction`: _Percentage_. For example: `sideImageFraction: 35%`. For an interview, sets the width of the interviewee image on the title page. `sideImageFraction: 100%` means the entire right half will be covered by the interviewee image.

The actual content of the interview is set in the `interviewXYZ.txt` file that was copied into the `dataFiles` folder. It has the following structure:

```
SS: Hello sir. I am Swarnendra Saha from Team InScight...

AAN: So I did that because somehow I wanted to learn....

IMAGE: (path: "/images/AAN1.jpg", caption: "Prof. Natu  ... at *Pune University*, while ...", position: bottom, width:100%, portrait: true)

#colbreak()
```

The lines beginning with `SS:` are interviewer questions (the prefix `SS:` must match the ones provided in the `group1` variable defined in the .typ file), while those beginning with `AAN:` are the interviewee answers (this must in turn match the one provided in `group2` in the .typ file). Thes must be inserted according to the interview (the above two are just samples).

The line starting with `IMAGE:` shows how to insert images. Column breaks can be inserted by adding `#colbreak` on an empty line.

This should cover most of the things that one needs to know to design an article.


