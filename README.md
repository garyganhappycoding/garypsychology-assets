# garypsychology-assets

Slides and design templates for @garypsychology07.

- `tools/common.py` – brand CSS (cream/indigo/coral, Fraunces + Manrope + Noto Sans CJK), icons, helpers (`z()` Chinese glosses, `zs()`, `foot()`, `write()`)
- `tools/toons.py` – original cartoon SVGs (psychiatrist, psychologist, counsellor, social worker, quiz pill, badge, rat, bang, crying baby, exam paper)
- `tools/render.js` – `node tools/render.js carousels/NN-name` renders slide-*.html → PNG (1080×1350) and flags overflow
- `tools/contact.py` – one contact sheet of all slides for quick review
- `carousels/NN-name/gen.py` – the content of each carousel; copy the closest one to start a new carousel

Setup once per machine: `cd tools && npm i` (Chinese font: system Noto Sans CJK SC).
