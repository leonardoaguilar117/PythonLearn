from pathlib import Path

path = Path("Basic Py")

"""
    path.exists()
    path.mkdir()
    path.rmdir()
    path.rename()
"""

# A way to iterate elements inside list
listOfFiles = [p for p in path.iterdir()]
FilesWithCondition = [p for p in path.glob("1-*.py")]

print(FilesWithCondition)
