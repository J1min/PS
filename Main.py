def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer


if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))
