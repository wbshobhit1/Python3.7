def iplnews (str):
    print(f"Today's match news is, {str} \nStay Tuned!!! ")

def resultbet (betlost, betgain):
    print(f"Bet lost is {betlost} and Bet gain is {betgain}")
    return betlost - betgain + 10

if __name__ == '__main__':
    print(iplnews("Mumbai lost"))
    o = resultbet(40,20)
    print(o)