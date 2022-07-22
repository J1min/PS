from pathlib import Path
N = int(input())
Make = Path(f"백준/{N}.py")
if not Make.is_file():
    f = open(f"백준/{N}.py", "w")
    print("만들엇서요")
    f.close()
else:
    print("파일이 이미 존재합니다 ㅅㄱㅂㅇ")