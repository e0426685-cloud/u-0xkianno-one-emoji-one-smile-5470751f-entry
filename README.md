# One Emoji, One Smile

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/e0426685-cloud/u-0xkianno-one-emoji-one-smile-5470751f-entry/rank.svg)](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/e0426685-cloud/u-0xkianno-one-emoji-one-smile-5470751f-entry/reward.svg)](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [One Emoji, One Smile](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f) bounty on make.fun.

## The entry

Exactly one emoji, the one most likely to make a stranger smile:

🌞 — the sun with a face.

Warm at first glance, readable by a stranger of any age or background with no
context needed, a deliberate pick rather than the first smiley that comes to
mind, and friendly coming from someone unknown — no intimacy, sarcasm or
flirtation.

## How it works

`main.py` (Python standard library only) writes the single emoji to
`/output/entry.txt` using a plain `open()` plus `chmod 644`, and validates it
first: exactly one character, 1–8 characters, not only white space.

```sh
python3 main.py
```
