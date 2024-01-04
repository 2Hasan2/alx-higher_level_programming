#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    handle_lang = 's' if len(args) != 1 else ''
    handle_lang += ':' if len(args) else '.'
    print(f"{len(args)} argument{handle_lang}")
    for i, arg in enumerate(args):
        print(f"{i + 1}: {arg}")
