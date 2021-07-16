import time
from functools import lru_cache

@lru_cache(maxsize=3)
def covid_report(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Enter your file number:")
    inp = input()
    print("Waiting for the response for",inp)
    covid_report(3)
    print("Done....\nPress any key for", inp, "results")
    input()
    covid_report(3)
    print("You are clear")
