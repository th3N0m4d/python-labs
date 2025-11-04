"""Python Labs - PCAP & PCPP1 Exam Preparation

A collection of Python games and exercises for learning programming
concepts in preparation for PCAP and PCPP1 certification exams.
"""

from .hangman_game import play as hangman
from .guessing_game import guessing_game

__version__ = "0.1.0"
__author__ = "Edielton Estrela Dantas"

# What gets imported with "from src import *"
__all__ = ["hangman", "guessing_game"]
