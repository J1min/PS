from pathlib import Path
from datetime import datetime
Number = input()
Make = Path(f"BOJ/{Number}.py")

if not Make.is_file():
    f = open(f"BOJ/{Number}.py", "w")
    f.write(f"# PROBLEM - \n")
    f.write(f"# TIER - G\n")
    f.write(f"# NUMBER - {Number}\n")
    f.write(f"# DATE - {str(datetime.today())[:16]}\n")
    f.write(f"# IDEA - \n")
    f.write(f"import sys\n")
    f.write(f"input = sys.stdin.readline\n")

    print(f"\n{Number}.py 만들엇서요\n")
    print(f"BOJ/{Number}.py")
    print(f"BOJ/{Number}.py")
    print(f"BOJ/{Number}.py")
    f.close()

else:
    print(f"\n{Number}.py 파일이 이미 존재합니다 ㅅㄱㅂㅇ\n")
    print(f"BOJ/{Number}.py")
    print(f"BOJ/{Number}.py")
    print(f"BOJ/{Number}.py")
