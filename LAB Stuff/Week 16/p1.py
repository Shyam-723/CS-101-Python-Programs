def asterik(n):
    if n==0:
        return 0

    asterik(n-1)

    print("*" * n)

lines= int(input("How many lines do you want?"))
asterik(lines)
