def calc(a, b):
    sum = a + b
    print(sum)
    sub = a - b
    print(sub)
    mul = a * b
    print(mul)
    div = a / b
    print(div)

    List = [sum, sub, mul, div]
    print(List)

    lsum = List[0] + List[1] + List[2] + List[3]
    print(lsum)

calc(2, 4)
