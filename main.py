#!/usr/bin/env python3
"""One-Line Office Joke — make.fun bounty u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes a single one-line joke about office life to /output/entry.txt (or
./output/entry.txt when run locally). The joke is the whole entry: one read,
a setup, and a surprise turn at the very end.

Deterministic: no randomness, no network, no timestamps, no input.
"""

import os

# The entry: one line, at most 199 characters.
#
# Why this joke lands: the setup is an employee asking an AI to quit for
# them, and the punchline is the AI answering in the most passive-aggressive
# office voice there is — "per my last email, no." — as if the AI itself
# were the manager refusing the resignation. The turn sits at the very end,
# so the reader only gets the joke on the last words. Reviewed against the
# judge's criteria after v1 ran: genuine office joke, turn at the end,
# instantly recognisable to anyone who has received that email, tight at
# 83 chars, and fresh (an AI answering in corporate-speak, not the
# Monday-morning or photocopier line the brief warns against).
JOKE = "I asked the AI to write my resignation letter; it replied, 'per my last email, no.'"


def main() -> None:
    # Gate self-check: the sealed scorer accepts 1-199 UTF-8 chars, not only
    # whitespace, one line. Fail loudly here instead of shipping a bad entry.
    assert 1 <= len(JOKE) <= 199, f"joke is {len(JOKE)} chars, gate needs 1-199"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    if os.path.isdir("/output"):
        out_dir = "/output"
    else:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
