---
layout: post
title: "My most amazing Makefile for CL papers"
tags: [en]
lang: en
---

Automation of stuff that does not need to be automated at all is one of my most
favorite procrastination activities. As an experienced (and most of the time
unsuccessful) submitter to conferences organized by ACL (ACL, NAACL, EACL,
EMNLP), I spent a lot of procrastinating time improving the Makefile compiling
the papers.

Here are few commented snippets from the Makefiles. Hopefully, someone finds that
useful.

## The normal LaTeX stuff

I compile the paper using `latexmk`.

```make
main.pdf: $(FILES)
	latexmk -pdflatex="$(LATEX) %O %S" -pdf -dvi- -ps- -halt-on-error main
```

I keep the dependencies in variable `FILES`, so I can use it in multiple
targets without recompiling the paper over and over. Variable `LATEX` contains
the LaTeX compiler. I mostly use `pdflatex`, so I do not have to deal with
unexpected problems when I upload pre-prints to arXive where only `pdflatex` is
allowed.

Currently, I draw most figures using tikz. Previously, I made the figure using
Inkscape which required converting the SVG files into PDF. I did that using a
wildcard target. First I defined a wildcard:

```make
SVGFILES := $(wildcard img/*.svg)
```

This is then listed among dependencies as `$(SVGFILES:%.svg=%.pdf)` in the
`FILES` variable. The target that converts the

```make
%.pdf : %.svg
	inkscape -A $*.pdf $*.svg
```

If the paper contains plots from matplotlib, I handle them similarly by keeping
one Python script per plot and by calling the scripts in the Makefile via a
wildcard.

For continuous building as I write, I have a special target `watch`:

```make
watch:
	latexmk -pdflatex="$(LATEX) %O %S" -pdf -dvi- -ps- -interaction=nonstopmode -synctex=1 -pvc main
```

Calling `make watch` starts a process that recompiles the paper every time the
source code changes, but of course, it does not monitor the changes in scripts
that generate images.

## Separating the paper from the appendix

The main body of the paper and the appendix should be submitted in two separate
pdf files. PDFs can be easily split in the terminal using for instance `pdftk`.
To do so, we need to know first where to cut the PDF.

The following LaTeX code creates a file a prints the page number where the
appendix starts into file `appendix.tmp`.

```latex
\clearpage
\appendix

\newwrite\outputstream
\immediate\openout\outputstream=appendix.tmp
\immediate\write\outputstream{\thepage}
\immediate\closeout\outputstream
```

Then, I can add two targets to the Makefile that create two separate PDFs for
the main paper and the appendix submission.

```make
paper_submission.pdf: main.pdf
	pdftk main.pdf cat 1-$$(( `cat appendix.tmp` - 1 )) output paper_submission.pdf

appendix_submission.pdf: main.pdf
	pdftk main.pdf cat `cat appendix.tmp`-end output appendix_submission.pdf
```

## Attaching source code

A good paper with reproducible results always comes with source code. Because I
always have the code in a separate git repository, I keep the updated code next
to the paper. The following Makefile snippet does the following:

1. Clones the repository if it does not exist.

2. Pulls if there is something new in the main branch.

3. Exports the code (it is the checkout-index thing), so I am sure I am
   submitting the full history of commit to the conference.

4. Creates a tarball for submission.

```make
.PHONY:code.tgz
code.tgz:
	if [ ! -e code_repository ]; then git clone $(REPO) code_repository; fi
	cd code_repository; \
	if `git fetch --dry-run | grep .`; then \
		git pull; \
		mkdir -p ../code \
		cd code_repository; git checkout-index -a -f --prefix=../code/; \
		cd ..; \
		tar zcvf code.tgz code; \
		rm -r code; \
	fi
```

Variable `REPO` contains the address to the remote repository. To make sure
this shell stuff works out, I also `SHELL=bash` at the beginning of the
Makefile, but it might not be necessary.

## Further tricks

When submitting the camera-ready version to the conference, we are also asked
to add the LaTeX source code as a zip file. I do it using the following target.

```make
latex_source.zip: $(FILES)
	zip latex_source.zip *.sty *.bst *.bib $(FILES)
```

And finally, if you plan to use an external grammar checker such as Grammarly,
you might want to compile the paper in such a way that you easily copy the text
without dealing with hyphenation and weird characters. For that, I tried to
compile the paper as HTML. Here is the snippet that does that, but it is far
from being perfect.

```make
html/$(NAME)_html.html: $(FILES)
	mkdir -p html
	sed -e 's/%\\aclfinalcopy/\\aclfinalcopy/' $(NAME).tex > main_html.tex
	make4ht -e mk4ht.mk4 --xetex --utf8 --jobname $(NAME)_html --output-dir html main_html.tex
	rm $(NAME)_html-*.{svg,png} $(NAME)_html*.* || true
```
