from pathlib import Path
N = input()
Make = Path(f"백준/{N}.py")
if not Make.is_file():
    f = open(f"백준/{N}.py", "w")
    print()
    print(f"{N}.py 만들엇서요\n")
    print(f"백준/{N}.py")
    print(f"백준/{N}.py")
    print(f"백준/{N}.py")
    f.close()
else:
    print()
    print(f"{N}.py 파일이 이미 존재합니다 ㅅㄱㅂㅇ\n")
    print(f"백준/{N}.py")
    print(f"백준/{N}.py")
    print(f"백준/{N}.py")