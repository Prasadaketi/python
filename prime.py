num = 4
i = 1
res = True
while i<=num:
        if(i != 1 and num % i == 0 and i != num):
                res = False

        i += 1
if (res == True):
    print("prime number")
else:
    print("not a prime number")

