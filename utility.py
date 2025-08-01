"""
utility.py

Helper functions that don't belong to any specific game domaon. This helps keep files clean and working on their main purpose.
"""

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')