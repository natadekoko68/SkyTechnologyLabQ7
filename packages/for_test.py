from main import main
from time import time
import random
import string

def solver(n, S):
    text = ""
    for i in range(n - 1, -1, -1):
        if i % 2 == 1:
            if text < S[i] + text:
                text = S[i] + text
        else:
            if text > S[i] + text:
                text = S[i] + text
    return text


def string_generator(n):
    Letters = string.ascii_lowercase
    randlst = [random.choice(Letters) for _ in range(n)]
    return ''.join(randlst)


def test_generator():
    n = random.randint(1, 10 ** 6)
    text = string_generator(n)
    answer = solver(n, text)
    return [n, text, answer]

def main_with_test(testcases):
    for key in testcases:
        n = testcases[key][0]
        text = testcases[key][1]
        expect = testcases[key][2]
    assert (main(n,text) == expect)
    return True

def main_with_timer(testcases,print_time=False):
    time_sum = []
    print(" == Sample Case == ")
    for key in testcases:
        n = testcases[key][0]
        text = testcases[key][1]
        s = time()
        main(n, text)
        e = time()
        assert (2 >= (e-s))
        time_sum.append(e-s)
        print(f"Case{key} : {e-s:.5f} sec (letter_num={n})")
    if print_time:
        print(" == Overall == ")
        print(f"Max : {max(time_sum):.4f} sec")
        print(f"Ave : {sum(time_sum)/len(time_sum):.4f} sec")
    return True

def make_testcases(iter_num, sample_init=False):
    if sample_init:
        testcases = {"A": [2, "aa", "a"],
                     "B": [4, "abcd", "acd"],
                     "C": [10, "aaaaaaaabb", "aaaab"],
                     "D": [6, "xskszy", "sky"],
                     }
    else:
        testcases = {}
    for i in range(1,iter_num+1):
        testcases[i] = test_generator()
    return testcases

def test(iter_num=10, ans=True, time=True):
    testcases = make_testcases(iter_num)
    if ans:
        main_with_test(testcases)
    if time:
        main_with_timer(testcases, print_time=True)


if __name__ == "__main__":
    test(iter_num=3)