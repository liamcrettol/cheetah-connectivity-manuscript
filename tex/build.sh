#!/usr/bin/env bash
# Build the manuscript. Requires TeX Live with biber.
#   ./build.sh              capstone layout    -> main.pdf
#   ./build.sh article      article layout     -> main_article.pdf
#   ./build.sh submission   submission layout  -> main_submission.pdf
#   ./build.sh all          all three
set -e
cd "$(dirname "$0")"
case "$1" in
  article)    latexmk -pdf -interaction=nonstopmode main_article.tex ;;
  submission) latexmk -pdf -interaction=nonstopmode main_submission.tex ;;
  all)        for f in main main_article main_submission; do
                latexmk -pdf -interaction=nonstopmode "$f.tex"
              done ;;
  *)          latexmk -pdf -interaction=nonstopmode main.tex ;;
esac
