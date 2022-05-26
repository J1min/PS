def solution(s):
    answer = ''
    arr = []
    success = []
    wordCnt = 0
    arr.append(s)
    # print(arr[0])

    for i in arr:
        for j in i:
            wordCnt += 1
            if(wordCnt % 2 == 0):
                # print(j.lower(), end="")
                success.append(j.lower())
            else:
                # print(j.upper(), end="")
                success.append(j.upper())
        answer = "".join(success)
        print(answer)
        # print(success)
        return answer


solution("brother mother father family love school friend angular try hello world")
