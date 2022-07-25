import string
N = list(input())
upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)


def java_cpp(String):
    insert_list = []
    if String[0] in upper or String[-1] in upper:
        print("Error!")
        return
    for i in range(len(String)):
        if String[i] in upper:
            String[i] = String[i].lower()
            insert_list.append(i)
    for i in range(len(insert_list)):
        String.insert(insert_list[i]+i, "_")
    print("".join(String))


def cpp_java(String):
    pop_list = []
    if String[-1] == "_" or String[0] == "_" or "__" in "".join(String) or String[0] in upper:
        print("Error!")
        return
    for i in String:
        if i in upper:
            print("Error!")
            return
    for i in range(len(String)):
        if String[i] == "_":
            pop_list.append(i)
    for i in range(len(pop_list)):
        String[pop_list[i]+1] = String[pop_list[i]+1].upper()
    String = "".join(String)
    String = String.replace("_", "")
    print(String)


if "_" in N:
    cpp_java(N)
else:
    java_cpp(N)
