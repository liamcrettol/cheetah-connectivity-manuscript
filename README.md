# Cheetah connectivity manuscript (Overleaf mirror)

This repo is a **synced mirror**, not the canonical source. The real project,
including the analysis, protocol history, and Decision Log, lives at
[cheetah-connectivity](https://github.com/liamcrettol/cheetah-connectivity).
This repo exists only so Overleaf has something small and LFS-free to sync
against, the main repo carries a full ArcGIS project and Git LFS binaries
that Overleaf's GitHub integration cannot handle.

## Layout

    tex/       manuscript (main.tex + sections/)
    protocol/  predeclared analysis protocol
    refs/      bibliography

## Keeping this in sync

From the main `cheetah-connectivity` checkout:

    tools/sync_manuscript_repo.sh

Run it after any commit that touches `tex/`, `protocol/`, or `refs/`. It
mirrors those three directories here and pushes. Edits made directly in
Overleaf get pulled back into the main repo the same way, in reverse, see
that script's header comment.

## Building

    cd tex && latexmk -pdf main.tex
    cd protocol && latexmk -pdf protocol.tex

Requires TeX Live with biblatex-apa and biber, or open in a Codespace, the
devcontainer supplies both.
