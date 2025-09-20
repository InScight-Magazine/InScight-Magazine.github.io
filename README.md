# Source files for InScight Website

[**InScight**](https://scicomm.iiserkol.ac.in/) is a student-run science magazine hosted by the Indian Institute of Science Education and Research Kolkata. This repository contains source files for generating the website. This repository updates the [development server](https://inscight-magazine.github.io/).

## Repository Layout

- **`_config.yml`** — Main Jekyll configuration file.
- **`README.md`** — Project overview and contribution guide.
- **`index.md`** — Homepage content.

### Core Jekyll Directories
- **`_includes/`** — Reusable HTML snippets (navbar, footer, figures, tables, etc.).
- **`_layouts/`** — Page/post layouts (`default`, `home`, `quiz`, `crossword`, `whoami`, etc.).
- **`_sass/`** — Sass partials for modular stylesheets (home, posts, navbar, tables, etc.).
- **`_posts/`** — Magazine articles grouped by issue, written in Markdown with front matter.
- **`_data/`** — Structured data in YAML/JSON/CSV:
  - `magazines.yaml`, `members.yaml`, `socials.yml`
  - Per-issue data: `crosswords/`, `digest/`, `linkedlists/`, `quizzes/`, `whoami/`
  - References (`references/`) and tables (`tables/`).

### Content Pages
- **`pages/`** — Standalone site pages:
  - About, Archives, Comics, Crossword Generator, Games, Opportunities, Submit, etc.
  - `issues/` contains landing pages for each magazine issue.
  - `latest-html.md` and `latest-pdf.md` link to the most recent release.

### Assets
- **`assets/`** — All static files:
  - **CSS:** global styles and syntax highlighting.
  - **JS:** interactive scripts (crosswords, quizzes, linked lists, etc.).
  - **Images:** article images (`_articles/`), per-issue images (`issue1/… issue5/`), banners, hero images.
  - **Magazines:** published PDFs (`issue1.pdf … issue5.pdf`).
  - **Magazine thumbnails:** cover images per issue.
  - **Members:** profile images of contributors.
  - **Posts metadata:** JSON schemas for articles, crosswords, digests, etc.
  - **Webfonts:** font families (`Hero New`, `Lato`, `Lilex`, `Roboto`, `SymbolsNF`).
  - Miscellaneous: favicons, banners, logos.

### Generated Website
- **`docs/`** — Built site (static HTML + assets).
  - Mirrors site structure: `issue1/…issue5/`, `comics/`, `games/`, `magazine/`, `submit/`, etc.
  - Contains compiled CSS/JS, images, and magazine PDFs.

### Scripts
- **`scripts/`** — Utility scripts:
  - `crossword.py` (crossword generation).
  - `typst-to-markdown.py` (conversion tool).
  - JSON input/output files for crossword generation.

## Getting Started
- Dependencies: Ruby, Jekyll

- Building and serving website:
```sh
$ git clone https://github.com/InScight-Magazine/InScight-Magazine.github.io.git
$ cd InScight-Magazine.github.io
$ jekyll serve
```
The site should be accessible at `http://localhost:4000)`.

## Contributors
- [Abhirup Mukherjee](https://github.com/abhirup-m)
- [Thushiyantheswaran G](https://github.com/thushi308)

## TODO
- add light/dark mode switching
- start using a Gemfile
