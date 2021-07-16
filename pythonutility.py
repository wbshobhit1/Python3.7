import argparse
import sys


def faulty_calc(args):
    if args.o == '+':
        if args.a == 56 and args.b == 9:
            return 77
        elif args.a == 9 and args.b == 56:
            return 77
        else:
            return args.a + args.b

    elif args.o == "-":
        return args.a - args.b

    elif args.o == "*":
        if args.a == 45 and args.b == 3:
            return 555
        elif args.a == 3 and args.b == 45:
            return 555
        else:
            return args.a * args.b

    elif args.o == '/':
        if args.a == 56 and args.b == 6:
            return 4
        else:
            return args.a / args.b

    else:
        return "Something went worng"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', type=float, default=0,
                        help=" Enter the first number, This is utility calculation")

    parser.add_argument('--b', type=float, default=0,
                        help=" Enter the second number, This is utility calculation")

    parser.add_argument('--o', type=str, default="+",
                        help=" Enter the first number, This is utility calculation")

    args = parser.parse_args()
    sys.stdout.write(str(faulty_calc(args)))
