def calc(a): #commit 1
    for x in range((int)(a/2) + 1):
        if(x !=0 and a % x == 0):
            print(x)

calc(60)
