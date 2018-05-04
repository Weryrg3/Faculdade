try:
    s = input()
    while s:
        print(int(s) - 1)
        s = input()
except EOFError:
    pass