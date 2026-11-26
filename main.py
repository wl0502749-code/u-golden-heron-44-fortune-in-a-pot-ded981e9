"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant to /output/entry.txt.
The fortune must be a single line of 1 to 120 characters, UTF-8,
with no trailing newline (the gate counts the file's characters).
"""

from pathlib import Path

# The fortune: a prediction ("By Friday ... will ...") written for this
# plant on this windowsill — a brave new leaf, the morning sun, and a
# small joke about the plant quietly taking credit for spring. Kind,
# warm, no doom or withering, and specific enough that it could not be
# said about just any plant in any room.
FORTUNE = (
    "By Friday, your windowsill plant will unfurl a brave new leaf, "
    "tilt to the sun, and quietly take credit for spring."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"fortune is {len(text)} characters, must be 1-120")
    if text != FORTUNE or "\n" in text:
        raise ValueError("fortune must be a single clean line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
