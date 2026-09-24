# 墨韵 Moyun

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live demo](https://img.shields.io/badge/Live-axtonliu.github.io%2Fmoyun-B03A2A.svg)](https://axtonliu.github.io/moyun/)

A sheet of rice paper that breathes. Ink runs on a real-time fluid simulation on your GPU, every stroke plays a guqin note, and an invisible hand paints a Chinese landscape that has never existed before — then signs it with a poem and a seal.

**[Open it →](https://axtonliu.github.io/moyun/)** · [中文说明](README.zh-CN.md)

![A generated ink landscape with a poem and a red sun](media/preview.jpg)

## What it does

- **Watch**: on load, a brush you can't see paints in the classical order — distant hills, main peak outline, texture strokes (皴), washes (染), moss dots, then pines, water, a fishing boat, birds, a cinnabar sun, a poem and a seal. Each painting is generated fresh.
- **Paint**: press and drag. Slow strokes are wet and heavy; fast strokes are thin and dry. Each stroke is one dip of ink, so it runs dry into flying-white (飞白) streaks.
- **Play**: `清水` (clear water) is a fluid brush — stir a finished painting and watch the ink swirl.
- **Listen**: strokes play a pentatonic guqin, so nothing you draw is ever out of tune.

## How it works

Everything is one HTML file. No libraries, no images, no audio files.

| Part | Technique |
|---|---|
| Fluid | Incompressible Navier–Stokes in WebGL2 fragment shaders: curl → vorticity confinement → divergence → 24 Jacobi pressure iterations → gradient subtraction → semi-Lagrangian advection |
| Ink bleeding | The ink texture stores free ink, cinnabar, water and settled ink in RGBA. Water diffuses anisotropically, modulated by procedural paper-fibre noise, then evaporates; dried ink settles and only moves again when re-wetted |
| Brush | Gaussian stamps at even spacing along the path, normalised by spacing. Speed sets width, ink load decays with distance, and bristle streaks are cut with 1-D noise across the stroke normal |
| Paper | Procedural fibres and granulation, baked once per resize/theme |
| Qin | Karplus–Strong plucked-string synthesis into AudioBuffers; slides and vibrato via `playbackRate` automation; procedural reverb impulse |
| Landscape | Seeded generator for ridgelines, texture strokes, trees and composition, with separate landscape and portrait layouts |

Light and dark themes follow the system: dark turns the paper to night and the ink to moonlight.

## Run locally

```bash
git clone https://github.com/axtonliu/moyun.git
cd moyun
python3 -m http.server 8000
# open http://127.0.0.1:8000/
```

Requires a browser with WebGL2 and half-float render targets (current Chrome, Edge, Safari, Firefox).

### Record a video

`scripts/record.py` captures the opening sequence (frames via CDP screencast, audio via a `MediaRecorder` tap on the page's WebAudio output) and muxes 16:9 and 9:16 MP4s with ffmpeg.

```bash
pip install playwright && python3 -m playwright install chromium
python3 scripts/record.py --url http://127.0.0.1:8000/ --out media
```

## File structure

```
moyun/
├── index.html          # the whole piece
├── scripts/record.py   # optional: record the opening sequence to MP4
└── media/              # preview images
```

## Status

A finished piece, maintained on a best-effort basis. Reproducible bug reports (browser + device + steps) and small fixes are welcome.

## Acknowledgments

- Jos Stam, *Stable Fluids* (SIGGRAPH 1999), and Mark Harris, *Fast Fluid Dynamics Simulation on the GPU* (GPU Gems, ch. 38) — the solver pipeline.
- Pavel Dobryakov's [WebGL-Fluid-Simulation](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation), which made this pipeline famous on the web and inspired the shader layout.
- Kevin Karplus & Alex Strong, *Digital Synthesis of Plucked-String and Drum Timbres* (1983).
- Fonts via Google Fonts: Ma Shan Zheng, Noto Serif SC, IBM Plex Mono (SIL Open Font License).

Written by Claude (Opus 5.5) in a single session, from one open-ended prompt: make something that amazes everyone who sees it.

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Author | 作者

**Axton Liu** — AI Educator & Creator

- Website: [axtonliu.ai](https://www.axtonliu.ai)
- YouTube: [@AxtonLiu](https://youtube.com/@AxtonLiu)
- Twitter/X: [@axtonliu](https://x.com/axtonliu)

### Learn More

- [MAPS™ AI Agent Course](https://www.axtonliu.ai/aiagent) - Systematic AI agent skills training
- [Claude Skills: A Systematic Guide](https://www.axtonliu.ai/newsletters/ai-2/posts/claude-agent-skills-maps-framework) - Complete methodology
- [AI Elite Weekly Newsletter](https://www.axtonliu.ai/newsletters/ai-2) - Weekly AI insights
- [Free AI Course](https://www.axtonliu.ai/axton-free-course) - Get started with AI

---

© AXTONLIU™ & AI 精英学院™ 版权所有
