romanos = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
# 
N = int(input())
# 
while N > 0:
    try:
        print(romanos[N], end ="")
        break
    except KeyError:
        for i in romanos:
            if N >= i:
                print(romanos[i], end ="")
                N -= i

        # break
print()

# 4 = IV
# 9 = IX
# 400 = CD
# 900 = CM
# 990 = CMXC
# 480 = CDLXXX
