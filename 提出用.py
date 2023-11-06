from itertools import groupby
from collections import deque

def add(encoded_deque,char):
    temp_char,num = encoded_deque[0]
    if char == temp_char:
        encoded_deque[0] = temp_char,num+1
    else:
        encoded_deque.appendleft((char,1))
    return encoded_deque

def compare(oe,encoded_deque,add_char):
    deque_temp_char, _ = encoded_deque[0]
    deque_prev_char,_ = encoded_deque[1]
    if oe == 1:
        if add_char == deque_temp_char:
            if deque_prev_char < add_char:
                return add(encoded_deque,add_char)
            else:
                return encoded_deque
        elif add_char > deque_temp_char:
            return add(encoded_deque,add_char)
        elif add_char < deque_temp_char:
            return encoded_deque
    if oe == 0:
        if add_char == deque_temp_char:
            if deque_prev_char > add_char:
                return add(encoded_deque,add_char)
            else:
                return encoded_deque
        elif add_char < deque_temp_char:
            return add(encoded_deque,add_char)
        elif add_char > deque_temp_char:
            return encoded_deque

def main(n,string):
    temp = deque()
    temp.append(("",0))
    temp.append(("",0))
    for i in range(n-1,-1,-1):
        temp = compare(i%2,temp,string[i])
    return ''.join(char * count for char, count in temp)

n = int(input())
text = input()
print(main(n,text))


"""以下テスト"""

# n = 6*10**5
# text = "xskszy"*10**5
# import time
# s = time.time()
# print(main(n,text))
# e = time.time()
# print(e-s)

