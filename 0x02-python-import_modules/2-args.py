#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_count = len(sys.argv) - 1
    print(f"{args_count} argument{'s' if args_count != 1 else ''}:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
