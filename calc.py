def calc(a, b): #commit 1
    sum = a + b #commit 2
    print(sum)
    sub = a - b #commit 3
    print(sub)
    mul = a * b #commit 4
    print(mul)
    div = a / b #commit 5
    print(div)

    List = [sum, sub, mul, div] #commit 6
    print(List)

    lsum = List[0] + List[1] + List[2] + List[3] #commit 7
    print(lsum)

calc(2, 4)
print(" ")
calc(20, 3)
print(" ")
calc(9, 90)
