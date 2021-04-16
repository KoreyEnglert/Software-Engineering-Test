import random

def password(a): #commit 1
    p = "";
    d = "";
    for x in range(a):
        a = random.randint(0, 61);
        print(a)
        a += 48;
        if(a > 57):
            a += 7
        if(a > 90):
            a += 6
        p += chr(a)
    print(p);
    print(d);

password(100)

print(chr(48))
