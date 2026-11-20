import unittest

from main import MESSAGES, charming_message


class CharmingMessageTests(unittest.TestCase):
    def test_seeded_message_is_reproducible_and_valid(self):
        first = charming_message(seed=42)
        second = charming_message(seed=42)

        self.assertEqual(first, second)
        self.assertIn(first, MESSAGES)


if __name__ == "__main__":
    unittest.main()
