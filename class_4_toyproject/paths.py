
from pathlib import Path
from os import path

# 이건 제 컴퓨터에만 해당하는 경로.
# ROOT_DIR = "/Users/eubinecto/Desktop/Projects/Toy/class_4_toyproject"
ROOT_DIR = Path().resolve().parent.__str__()
DATA_DIR = path.join(ROOT_DIR, "data")
