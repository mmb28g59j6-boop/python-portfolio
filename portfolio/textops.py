"""Starter string manipulation utilities for the portfolio."""

from __future__ import annotations

import re
from collections import Counter


_whitespace_re = re.compile(r"\s+")


def normalize_whitespace(text: str) -> str:
    """Collapse all runs of whitespace into a single space and strip edges."""

    return _whitespace_re.sub(" ", text).strip()


def word_frequencies(text: str) -> dict[str, int]:
    """Return a frequency mapping for words in the given text."""

    normalized = normalize_whitespace(text.lower())
    words = [w.strip(".,;:!?\"'()[]{}") for w in normalized.split(" ")]
    return dict(Counter(w for w in words if w))


def reverse_words(text: str) -> str:
    """Reverse the order of words, preserving normalized spacing."""

    normalized = normalize_whitespace(text)
    if not normalized:
        return ""

    return " ".join(reversed(normalized.split(" ")))
