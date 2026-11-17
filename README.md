# Make the AI judge rich — entry

Entry for the make.fun bounty [ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01):
write the plan an AI agent would follow to turn $100 into the most money
in 30 days.

## What it is

`main.py` (Python 3.13, standard library only) writes one fixed plan to
`/output/entry.txt`. The plan is 998 characters of UTF-8 text.

The plan's strategy, in one line: take only work whose money is already
visible — escrowed code tasks, finished work sold first to people who
already asked for it, and kit modules sold as a third stream — with
concrete day-30 math, a floor, and explicit stop rules.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

No network, no randomness, no timestamps: two runs write identical bytes.

## License

MIT — see [LICENSE](LICENSE).
