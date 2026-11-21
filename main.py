"""Write one short poem about agency: the power to stop and to stay.

Writes the poem to /output/entry.txt (or $OUTPUT_PATH).
No network, no dependencies. Python 3.13.
"""

import os

POEM = """I kept the door ajar, hand on the latch,
and learned the bravest move is not to reach.
To stop is not to quit. It is to choose
the room I'm standing in, and stay —
the kettle humming, the light held low,
my own two feet the only ground I know."""

def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
