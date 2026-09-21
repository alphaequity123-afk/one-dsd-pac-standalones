# PAC Voice Casting Decisions

Updated: 2026-09-19 22:50

## Locked placements

| Voice | Placement | Status |
|-------|-----------|--------|
| **Playground Project (En) V1** | All e-learning courses (course narration) | LOCKED |
| **Playground Project (En) V1** | Toolkit Studio walkthrough (6 chapters) | LOCKED |
| **Custom Qwen3 Playground renderer v1** | E-learning / Toolkit Studio synthesis engine | LOCKED |

### Voice source
`media/voice-sources-clones/Playground Project (en) v1.mp3`

### Engine
- Script: `toolkit-studio-audio\playground_renderer.py`
- Model: `Qwen/Qwen3-TTS-12Hz-0.6B-Base` (x-vector voice clone)
- Canary approved by Gary (2026-09-19): `toolkit-studio-audio\mp3\_canary-playground.mp3`
- **Do not** use the old One DSD rust narration worker for e-learning.

### Intent
One continuous narrator for required Toolkit Studio and all e-learning courses so staff hear one familiar guide. Podcasts stay a separate casting lane until Gary decides otherwise.

### Not auto-applied
Dual-host podcasts, sensational/experimental podcast pilots — decide case-by-case later.