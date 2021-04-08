#!/usr/bin/env python3

def main():
    for x in range(1,101):
        out_str = ""
        if x % 3 == 0:
            out_str = out_str + "Fizz"
        if x % 5 == 0:
            out_str = out_str + "Buzz"
        print(f"{x}: {out_str}")

if __name__ == '__main__':
    main()
