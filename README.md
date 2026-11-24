# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/ZQ051031/say-what-actually-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/ZQ051031/say-what-actually-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy for the make.fun competition
"Say What Actually Broke" (`u-po-pu-say-what-actually-broke-a2c153b5`).

## The entry

> The disk filled up mid-save, so your file is half-written. Free up space and retry; the logs that would have explained why were deleted to make room.

It names the real failure (the disk filled up in the middle of a save),
says what happened to the user's file, tells them what to do next, and
owns the embarrassing part: the logs that would have explained why are
gone, because they were deleted to make room.

## How it works

`main.py` (Python standard library only) writes the entry to
`/output/entry.txt` — exactly one line, no trailing newline.

Run it with:

```sh
python3 main.py
```

## License

MIT. See `LICENSE`.
