#!/usr/bin/env bash
# Build the manuscript. Requires TeX Live with biber.
#   ./build.sh           capstone version  -> main.pdf
#   ./build.sh journal   journal version   -> main_journal.pdf
set -e
cd "$(dirname "$0")"
if [ "$1" = "journal" ]; then
  latexmk -pdf -interaction=nonstopmode main_journal.tex
  echo "-> main_journal.pdf"
else
  latexmk -pdf -interaction=nonstopmode main.tex
  echo "-> main.pdf"
fi
