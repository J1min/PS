import string
s_list = list(string.ascii_lowercase)

q = input()
while q != '*':
    sentence = set(q)
    s_sentence = sorted(sentence)
    if s_sentence[0] == ' ':
        s_sentence.pop(0)
    if s_sentence == s_list:
        print("Y")
    else:
        print("N")
    q = input()