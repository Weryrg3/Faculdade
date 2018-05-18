for i in range(0, int(input())):
    a, b = input().split(" ")
    c = ""
    n = ""

    l = list(zip(a, b))

    if len(a) < len(b):
        n = b[len(a):]
    elif len(a) > len(b):
        n = a[len(b):]

    for i in range(0, len(l)):
        c += l[i][0] + l[i][1]

    print(c + n)