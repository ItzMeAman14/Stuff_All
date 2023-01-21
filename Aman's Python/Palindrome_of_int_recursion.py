def pal(n, l):
    if n == 0:
        return 0
    else:
        p = n % 10
        return p*(10**(l)) + pal(n//10, l-1)


n = int(input("Enter a number to reverse:"))
temp = n
l = -1
while(n != 0):
    n = n//10
    l += 1
print(pal(temp, l))
