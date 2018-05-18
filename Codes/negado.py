# 2750
traces = "-" * 39 + "\n"
names = "|  decimal  |  octal  |  Hexadecimal  |\n"

print(traces + names + traces, end = "")

for i in range(0, 16):
    if i < 8:
        print("|" + " "*6 + "%d" % i + " "*4 + "|" + " "*4 + "%o" % i + " "*4 + "|" + " "*7 + "%X" % i + " "*7 + "|")
    elif i == 8 or i == 9:
        print("|" + " "*6 + "%d" % i + " "*4 + "|" + " "*4 + "%o" % i + " "*3 + "|" + " "*7 + "%X" % i + " "*7 + "|")
    else:
        print("|" + " "*6 + "%d" % i + " "*3 + "|" + " "*4 + "%o" % i + " "*3 + "|" + " "*7 + "%X" % i + " "*7 + "|")
print(traces)