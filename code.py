try:
    t = int(input()) #number of testcases

    if t<=10 and t>=1: #checking constraints of t
        for i in range(t):
            n = int(input())
            if n<=10**5 and n>=2: #checking constraints of n
                a = [int(a) for a in input().split()]
                sum = [(abs(a[i + 1] - a[i])-1) for i in range(len(a)-1)]
                tot = 0
                for k in sum:
                    tot = tot+k
                print(tot)
            else: print("number of cards cannot be more than 100")

    else: print("test cases cannot be more than 1000")
except:
    pass
