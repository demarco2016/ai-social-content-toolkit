#!/usr/bin/env python3
"""Basic tests for content toolkit."""

import unittest
from content_toolkit import format_for_x, generate_hashtags, quality_check

class TestToolkit(unittest.TestCase):
    def test_format_for_x_truncates(self):
        long_text = "a" * 300
        result = format_for_x(long_text)
        self.assertLessEqual(len(result), 280)

    def test_hashtags_not_empty(self):
        tags = generate_hashtags("AI Agents")
        self.assertTrue(len(tags) > 0)

    def test_quality_check_returns_score(self):
        check = quality_check("Hello world")
        self.assertIn("score", check)

if __name__ == "__main__":
    unittest.main()
