num = 24

for x in range (10, num+1):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                print(x, "bukan prima")
                break
        else:
            print(x,"adalah bilangan prima")