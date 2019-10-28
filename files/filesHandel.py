from pathlib import Path
# Absolute Path Or
# C:\Programs File\Sourav
# /user/local/bin
# Relative Path ************

# path = Path("file")
path = Path()

# print(path.mkdir())
# print(path.exists())
# print(path.rmdir())
# print(path.glob("*.*"))

# for file in path.glob('*.py'):
# for file in path.glob('*.*'):
for file in path.glob('*'):
    print(file)

