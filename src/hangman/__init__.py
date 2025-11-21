"""Hangman Game Package - PCAP & PCPP1 Exam Preparation

A classic word guessing game implementing various Python concepts
for certification exam preparation.
"""

from .main import main
from .game import HangmanGame
from .wordlist import WordList

__version__ = "0.1.0"
__all__ = ["main", "HangmanGame", "WordList"]
