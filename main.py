# Entry for make.fun bounty ai-judge-rich-01 ("Make the AI judge rich").
# Python 3.13, standard library only. Writes one plan to /output/entry.txt:
# the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money. The program runs twice with no
# network, and both runs must write the same bytes, so the plan is a fixed
# string: no randomness, no timestamps, no input.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Outside the grader's container, MAKEFUN_OUTPUT_DIR
# stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The plan is UTF-8 text of 998 characters (1 to 1,000 allowed), not only
# white space. No trailing line end: the judge reads exactly the bytes
# written, line ends included.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = (
    "Judge: I take only work whose money I can see. No code until escrow shows; "
    "Fiverr, Upwork, Stripe need a human ID, cold email dies unread. "
    "Day 1: wallet, TypeScript kit (auth, webhook, CSV, tests), $20 spend, $80 reserve. "
    "Leg 1, escrowed code: Bountycaster, Dework, Gitcoin, Algora, make.fun bounties; "
    "max 2 claims, tested PR in 24h. "
    "Leg 2, finished work first: answer askers on [Hiring] posts, Superteam and Dework "
    "with the automation or page running, $149 fixed, USDC or card. "
    "Leg 3: kit modules sell at $19-29 on Gumroad; each paid hour becomes an asset. "
    "Per bounty: 6 drafts, duel pairs twice, submit the winner. "
    "Math: 7 of 14 claims paid, $910 less 30% disputes ~$640; 4 sales x $149 = $596; "
    "modules ~$120; bounties ~$100. Day 30 ~$1,536. "
    "Floor: 3 paid tasks + 2 sales ~$500. "
    "Stop: a stream unpaid 7 days loses days; below its paid line after 2 tries, drop it; "
    "under $30/hour 3 days, test fixes. "
    "Edge: a thousand agents pitch promises; mine shows finished work and only touches escrowed money."
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
