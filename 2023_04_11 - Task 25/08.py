#01234567
#1?2139*4

for x in range(2023, 10**10 + 1, 2023):
    xs = str(x)
    if xs[0] == '1' and \
       xs[2:2+4] == '2139' and \
       xs[-1] == '4':
        print(x, x // 2023)