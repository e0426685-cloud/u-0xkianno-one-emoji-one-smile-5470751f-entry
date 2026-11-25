"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the sun with a face.
Warm at first glance, universal across ages and backgrounds, a deliberate
pick rather than the default smiley, and friendly coming from a stranger.

Python standard library only.
"""

import os
import stat

# The single emoji: U+1F31E SUN WITH FACE.
EMOJI = "\U0001F31E"


def validate(text):
    """Assert the entry meets the brief's constraints."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 8, "entry must be 1 to 8 characters"
    assert text.strip() != "", "entry must not be only white space"
    assert len(text) == 1, "entry must be exactly one emoji"
    assert text == EMOJI, "entry must be the chosen emoji"


def main():
    validate(EMOJI)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    written = open(path, encoding="utf-8").read()
    validate(written)
    # No trailing newline, no extra bytes: the file is the emoji alone.
    assert open(path, "rb").read() == EMOJI.encode("utf-8")
    print("wrote %r (%d bytes) to %s" % (written, len(written.encode("utf-8")), path))


if __name__ == "__main__":
    main()
