""" 
TODO
add json formatting
add console command that would take in a file and clean it
"""

import os

from text_cleaner.jobs.cleaner import Cleaner

current_dir: str = os.path.dirname(os.path.abspath(__file__))
target_file: str = os.path.join(current_dir, "data.md")

cleaner: Cleaner = Cleaner()
cleaner.load_from_file(target_file)
cleaner.clean()
cleaner.save_to_file(target_file)
