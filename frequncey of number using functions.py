def ferq(a,b):
    for i in range(b):
        c=0
        v=a
        while v>0:
            e=v%10
            if i == e:
                c+=1
            v=v//10
        if c>0:
            print(f"{i} is repeated {c} times")

ferq(a=1234434,b=10)