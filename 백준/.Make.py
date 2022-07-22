from pathlib import Path
N = int(input())
Make = Path(f"백준/{N}.py")
if not Make.is_file():
    f = open(f"백준/{N}.py", "w")
    f.close()
