from collections import deque


def add(encoded_deque, char):
    temp_char, num = encoded_deque[0]
    if char == temp_char:
        encoded_deque[0] = temp_char, num + 1
    else:
        encoded_deque.appendleft((char, 1))
    return encoded_deque


def compare(oe, encoded_deque, add_char):
    deque_temp_char, _ = encoded_deque[0]
    deque_prev_char, _ = encoded_deque[1]
    if oe == 1:
        if add_char == deque_temp_char:
            if deque_prev_char < add_char:
                return add(encoded_deque, add_char)
            else:
                return encoded_deque
        elif add_char > deque_temp_char:
            return add(encoded_deque, add_char)
        else:
            return encoded_deque
    if oe == 0:
        if add_char == deque_temp_char:
            if deque_prev_char > add_char:
                return add(encoded_deque, add_char)
            else:
                return encoded_deque
        elif add_char < deque_temp_char:
            return add(encoded_deque, add_char)
        else:
            return encoded_deque


def process(n_input, string):
    temp = deque()
    temp.append(("", 0))
    temp.append(("", 0))
    for i in range(n_input - 1, -1, -1):
        temp = compare(i % 2, temp, string[i])
    return ''.join(char * count for char, count in temp)

def main(n, text):
    return process(n, text)