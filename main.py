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
# Revision (self-review against the judge's criteria, in order, after v1 ran):
# - Criterion 1: a genuine office joke — resignation letter + "per my last
#   email", the most passive-aggressive phrase in office life. Kept verbatim.
# - Criterion 2: the turn must sit AT THE END — "per my last email, no."
#   is the last thing the reader hits. Kept verbatim.
# - Criterion 3: recognition — every office worker has received that email.
# - Criterion 4: tight — 83 chars, every word earns its place. "replied"
#   stays: it is the email verb, "answered" would soften the joke.
# - Criterion 5: fresh — an AI answering in corporate-speak is not the
#   Monday-morning or photocopier line the brief warns against.
# - No wording change survived review, so the revision instead hardens the
#   program: it now checks the gate itself (1-199 chars, one line, not only
#   whitespace) before writing, so a later edit to JOKE cannot silently
#   ship an entry the sealed scorer would refuse.
JOKE = (
    "I asked the AI to write my resignation letter; "
    "it replied, 'per my last email, no.'"
)


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
