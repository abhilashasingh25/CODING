# python program to safely create a nested directory using pathlib.path.mkdir

from pathlib import Path
Path("/root/dir A/dir B").mkdir(parents=True, exist_ok =True)

