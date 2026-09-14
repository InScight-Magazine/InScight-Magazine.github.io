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
bundle exec jekyll serve -wl
```
to build and serve the website. The output should state the url (usually [http://127.0.0.1:4000/](http://127.0.0.1:4000/)) at which the website is being served; open the url in a web browser to check what the served website looks like. `bundle exec` indicates that we want to use the environment specified by the Gemfile. `jekyll serve` builds and serves the website at the specified location. The flags `-wl` ensure that Jekyll Watches the files and recompiles automatically if there are any changes and automatically reLoads the browser to display the updated website.

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

## Designing "Web Content" For A Particular Web-Issue Of InScight
You'll typically be asked to design multiple pieces of content during the course of any given issue. When you are about to start designing the first item for an issue, download the latest version of the [typst version of the magazine](https://github.com/InScight-Magazine/Content) and extract it somewhere. It is important that you download the full repository because the upcoming steps assume a certain directory structure of these files.

The workflow here is to convert the `.typ` files that were created while designing the PDF version of the magazine into markdown files with the appropriate conventions and helper inclusions. For this, we have a convenience script `parseTypst.py` in the `scripts` folder of the website repository. The script does a lot of the tedious conversion tasks. In order to run the script, the python environment must have the packages `typst`, `pyyaml` and `pypandoc` installed. If the `uv` package manager is installed on the system, the following commands can prepare a working environment:
```shell
uv venv --python 3.13 ~/.inscight-venv ## create a python virtual environment
source ~/.inscight-venv ## activate the environment
uv pip install pyyaml pypandoc typst ## install necessary packages
```
The package installation is a one-time thing; from here on, the environment needs only be activated in order to start working.

In order to start working, open a terminal in the `scripts` folder, and then activate the virtual environment and run the parser:
```shell
source ~/.inscight-venv ## activate the environment
python parseTypst.py <PATH TO MAIN TYPST FILE> <ISSUE NUMBER>
#### python parseTypst.py ~/storage/InScight-documents/Issue9.5/issue95.typ 9.5
```

The meaning of the variables are self-explanatory. If the script runs without any errors, it should generate a number of folders in the current working directory. These have to be be copied into the appropriate locations within the main website folder. The generated website should now be inspected using Jekyll as described above.
