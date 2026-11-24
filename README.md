# Say What Actually Broke

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
