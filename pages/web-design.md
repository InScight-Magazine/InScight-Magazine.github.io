---
title: "Website Design Guidelines for InScight"
permalink: /web-design/
---

This page lists the steps necessary to get started with creating web content for _InScight_. This includes 

- converting articles and interviews from `.typ` (typst) format to a variant of markdown that is suitable for our static site generator Jekyll,

- using datafiles from the pdf version to create the science games and the Insight Digest section

- using existing images to create a web version of a comic (if the issue has one), and

- creating "editor's word" and "foreword" pages for the given issue, again from the `.typ` file.

The website is generated using a static-site-generator _Jekyll_; it uses markdown files and some predefined templates to create an HTML website that can be deployed on our server. All files necessary for the task can be found on our [github repo](https://github.com/InScight-Magazine/InScight-Magazine.github.io).

## Setting up the system

- Download the [_InScight_ website  repository](https://github.com/InScight-Magazine/InScight-Magazine.github.io) from github. Extract into a folder if it's downloaded as a compressed archive.

- In order to use _Jekyll_, we need to first install _Ruby_. Check [this page](https://www.ruby-lang.org/en/documentation/installation/) for some guidance. My personal recommendation is to use [ruby-install](https://github.com/postmodern/ruby-install#readme) if you're on Unix-ish systems (use your distributions package manager) and [RubyInstaller](https://rubyinstaller.org/downloads/) for Windows (choose the "without devkit" latest x64 version).

- Ensure that the `bundler` executable exists in our system path and is executable. We'll be using `bundler` to install Jekyll and other necessary plugins (called *gems* in the ruby ecosystem) for building and serving our website.

- Start a terminal in the directory of the repository you downloaded earlier. Run 
```bash
bundle install
```
; it should install the gems listed in the `Gemfiles` file. 

- Having installed the gems, you can now run 
```bash
bundle exec jekyll serve
```
to build and serve the website. The output should state the url at which the website is being served; open the url in a web browser to check what the served website looks like.

## Structure of The Website
It might be useful to know your way around the various folders.

- `index.md`
The homepage content of your site, written in Markdown. Rendered using a layout (usually specified in front matter) and served as `/`.

- `_config.yml`: Main configuration file for Jekyll. Defines site metadata, build settings, plugins, base URLs, markdown engine, etc.

- `Gemfile`: Lists Ruby gems (dependencies) needed for the site.
Ensures consistent environments across machines.

- `Gemfile.lock`: Pins exact gem versions used.
Prevents unexpected breakage when dependencies update.

- `README.md`: Human-readable documentation for the repository.
Typically explains site purpose, build instructions, and contribution notes.

- `_posts/`: Holds blog posts written in Markdown or HTML.
Filenames follow `YYYY-MM-DD-title.md` and automatically become dated posts.

- `pages/`: Custom standalone pages (e.g., About, Contact, Teaching).
Unlike `_posts`, filenames don’t need dates.

- `docs/`: The publishing source for GitHub Pages.

- `_data/`: YAML/JSON/CSV files providing structured data to templates.
Useful for menus, people lists, publications, etc.

- `_layouts/`: HTML templates that wrap content.
Defines overall page structure (header, footer, navigation).

- `_includes/`: Reusable partials inserted into layouts.
Examples: header, footer, navigation bar, analytics snippet.

- `_sass/`: Sass/SCSS partials for styling.
Compiled into CSS during the build process.

- `assets/`: Static files like CSS, JavaScript, images, and fonts.
Copied verbatim to the generated site.

- `scripts/`: Utility scripts (Ruby, Bash, Python, etc.).
Used for automation, content generation, or deployment helpers.

## Getting Started With A Particular Web-Issue Of InScight
You'll typically be asked to design multiple pieces of content during the course any given issue. 

- When you are about to start designing the first item for an issue, create a folder with an appropriate name (say `Issue7`) within the `_posts` and `assets` folders (if it doesn't already exist). Note the capitalisation of names of existing folders and name the new folders accordingly.

- You should also have the latest version of the [typst version of the magazine](https://github.com/InScight-Magazine/Content) downloaded and extracted somewhere. It is important that you download the full repository because the upcoming steps assume a certain directory structure of these files.

## Designing Articles and Interviews
In order to convert the `.typ` articles and interviews, we have a convenience script `typst-to-markdown.py` in the `scripts` folder of the website repository. The script does a lot of the tedious conversion tasks. The following assumes that a working python-3 environment is available on the system.

- Open a terminal in the `scripts` folder, and run `python typst-to-markdown.py <full-path-of-typst-file> <issue-number>`. For example, if we are trying to convert the article `/home/arch/InScight-Documents/Issue7/subfiles/quantum.typ`, the appropriate command is
```bash
python typst-to-markdown.py /home/arch/InScight-Documents/Issue7/subfiles/quantum.typ 7
```
If things run correctly, the operation should generate (within the `scripts` folder) a markdown file for the article and a folder that contains all images used in the article, and (optionally) copy datafiles that are used in the article (such as references, tables, etc) from the typst repository into the folder.

- The operation should also output the location where the webpage for this article can be viewed (for example, `/issue7/quantum-article/`). Copy/note this location.

- The name of the markdown `.md` file should have the date at the beginning; check that it's sensible. Next, copy the generated/copied files into the appropriate folders of the website:
    - The `.md` file goes into the appropriate `_posts` folder for the issue (such as `_posts/issue7`) that you created in the previous section.
    - The images folder goes into the appropriate `assets/images` folder for the issue, that you created in the previous section.
    - Any datafiles generated go into the `_data` folder. For example, if it's a references file, it goes into `_data/references`.

- Having copied all generated files into their respective folders, fire up the server by running `bundle exec jekyll serve` in the root of the website folder (that is, where the `index.md` file resides).

- The output of the command should state where the website is being served:
```
Auto-regeneration: enabled for '/home/Storage/websites/inscight'
LiveReload address: http://127.0.0.1:35729
    Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
        LiveReload: Browser connected
      Regenerating: 1 file(s) changed at 2025-12-28 12:32:07
                    pages/web-design.md
                    ...done in 0.669932492 seconds.
```
Note the line `Server address: http://127.0.0.1:4000/`. Open the url `http://127.0.0.1:4000/` to see the website.

- In order to view the article you converted, append the article location that was output earlier ( `/issue7/quantum-article/`) to the server address: `http://127.0.0.1:4000/issue7/quantum-article/`. Open this location in your browser to view the article.

- View the webpage carefully to ensure that everything has been parsed correctly. In particular, verify that
    - All section headings are present.
    - All bold and italic are formatted appropriately.
    - The article metadata are displayed correctly: title, author name, author bio, author image, reviewer name, date, cover image and abstract.
    - All article images are visible with correct captions.
    - References, if any, are listed appropriately at the end.

One thing that the conversion script doesn't account for is mathematical equations (the script output should warn you of this). If the equations are already available in latex format, copy and paste these equations directly, and change the separators appropriately. For example, the inline latex equation `$x=y$` or `\(x=y\)` has to be changed into `$$x=y$$`. The block equation
```latex
\[ x=y \]
```
or
```latex
\begin{equation}
    x=y
\end{equation}
```
has to be similarly converted into
```mathjax

$$ x=y $$

```

Note the empty lines before and after the equation.

If the latex equations are not available, they will of course have to be written from scratch in the markdown file, using the above format.
