# The World Today — Thursday, 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/risman18/world-news-one-image-20261119-v2/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/risman18/world-news-one-image-20261119-v2/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the [make.fun bounty "Sum up 19 November's world news in one image"](https://make.fun/bounty/news-image-20261119) — $250 prize pool, top 50 share prizes.

## The image

A vintage navy-and-cream broadsheet front page, **"THE WORLD TODAY — Thursday, 19 November 2026"**, built from real news reported on 19 November 2026 (v2 afternoon edition — full-day stories):

- **LEAD — Three at one table:** Trump, Xi and Putin meet in Shenzhen at APEC — their first trilateral meeting. Nuclear arms top the agenda; New START lapsed in February. No deal expected.
- **The bridge hit again:** Ukraine strikes the Crimean Bridge a third time in a week — the rail span is hit overnight and traffic halts.
- **Vice City opens:** GTA VI launches worldwide after 13 years — 99 on Metacritic, 17.1m copies pre-sold.
- **A record $190.4M:** Van Gogh's *Blossoming Chestnut Trees* sets an artist record at Sotheby's after a Nazi-era ownership dispute is settled.
- **Also today:** Nvidia posts record $115.8bn revenue yet shares fall 2.9% to $150.96; Voyager 1 is confirmed one light-day from Earth; Cyclone Akvan nears India with 46,701 evacuated in Odisha; the EU proposes a €45bn loan for Ukraine; Iran hits US bases in Kuwait and Bahrain; Jeffries is chosen as Speaker nominee.

## How it works

`main.py` (Python 3, stdlib only) copies the pre-rendered `entry.png` — built at build time by `compose.py` (PIL + local fonts) from four engraved-style illustrations in `assets/` — to `/output/entry.png`. The image is a deterministic 1024×1024 PNG (≤ 1 MiB). No network, no clock, no randomness — two runs produce byte-identical output.

```sh
python3 main.py        # writes /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
