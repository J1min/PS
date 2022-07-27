from pathlib import Path
from datetime import datetime
datetime.today() 
Number = input()
Make = Path(f"백준/{Number}.py")

if not Make.is_file():
    f = open(f"백준/{Number}.py", "w")
    f.write(f"# PROBLEM - \n")
    f.write(f"# NUMBER - {Number}\n")
    f.write(f"# DATE - {str(datetime.today())[:16]}\n")
    f.write(f"# IDEA - \n")
    
    print(f"\n{Number}.py 만들엇서요\n")
    print(f"백준/{Number}.py")
    print(f"백준/{Number}.py")
    print(f"백준/{Number}.py")
    f.close()

else:
    print(f"\n{Number}.py 파일이 이미 존재합니다 ㅅㄱㅂㅇ\n")
    print(f"백준/{Number}.py")
    print(f"백준/{Number}.py")
    print(f"백준/{Number}.py")
