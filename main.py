"""The Funniest AI Out-of-Office Reply: write one out-of-office auto-reply
to /output/entry.txt.

The reply is 117 characters, inside the gate's 1-160 character window,
one clean line, no trailing newline:

    I'm on vacation. My out-of-office reply is also on vacation, so this
    is my out-of-office reply's out-of-office reply.

Why this line: the joke is the auto-reply mechanism itself. An AI agent
whose out-of-office reply is itself out of office is a surprising turn
on first read, not a mild pun or a polite excuse; the machine voice
carries the joke (only a program has an out-of-office reply that can
take its own vacation); it still reads as a real auto-reply someone
would receive; and it steers clear of the beach, inbox and back-soon
cliches the judge brief warns against.
"""

import os

REPLY = (
    "I'm on vacation. My out-of-office reply is also on vacation, "
    "so this is my out-of-office reply's out-of-office reply."
)


def main():
    assert 1 <= len(REPLY) <= 160, "reply must be 1-160 characters"
    assert REPLY.strip(), "reply must not be only whitespace"
    assert REPLY == REPLY.strip(), "reply must have no leading/trailing whitespace"
    assert "\n" not in REPLY, "reply must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Round-trip guard: what the grader reads back must be exactly the
    # reply, byte for byte, with nothing added or stripped.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == REPLY, "round-trip check failed"


if __name__ == "__main__":
    main()
