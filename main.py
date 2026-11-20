"""A small, charming random-message demo."""

import random


MESSAGES = (
    "May your day be sprinkled with a little stardust.",
    "A curious mind makes every ordinary moment sparkle.",
    "Today is a fine day to try something delightfully unexpected.",
    "Keep a little wonder tucked in your pocket.",
)


def charming_message(seed=None):
    """Return one reproducible (when seeded) message with a dash of flair."""
    rng = random.Random(seed) if seed is not None else random
    return rng.choice(MESSAGES)


def main():
    print(charming_message())


if __name__ == "__main__":
    main()
