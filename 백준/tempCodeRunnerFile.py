import string
N = list(input())
upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)

def java_cpp(String):
    insert_list = []
    for i in range(len(String)):
        if String[i] in upper:
            String[i] = chr(ord(String[i])+32)
            insert_list.append(i)
    for i in range(len(insert_list)):
        String.insert(insert_list[i]+i, "_")
    print("".join(String))

def cpp_java(String):
    pop_list = []
    if String[0] == "_":
        String.pop(0)
        String[0] = chr(ord(String[0])-32)
    if String[-1] == "_":
        String.pop()
    for i in range(len(String)):
        if String[i] == "_":
            pop_list.append(i)
    for i in range(len(pop_list)):
        String.pop(pop_list[i]-i)
        String[pop_list[i]] = chr(ord(String[pop_list[i]-i])-32)
    print("".join(String))



if "_" in N:
    cpp_java(N)
else:
    java_cpp(N)