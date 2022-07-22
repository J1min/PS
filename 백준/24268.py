import string
year, notation = map(int, input().split())
the_legend_list = [i for i in range(notation)]
year += 1

tmp = string.digits+string.ascii_lowercase
def change(num, base) :
    if num == base:
        return -1
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return change(q, base) + tmp[r]


while True:
    the_number = change(year, notation)
    if the_number == -1:
        print
    number_change_list = list(map(int, the_number))
    if year > 381367044:
            print(-1)
            break
    year += 1
    print(sorted(number_change_list), the_legend_list, year)
    if sorted(number_change_list) == the_legend_list:
        number_change_list = map(str, number_change_list)
        print(int("".join(number_change_list), notation))
        break
        
