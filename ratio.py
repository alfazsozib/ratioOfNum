#!/bin/python3

def plusMinus(arr):
    p = n = z = 0
    total = len(arr)
    for i in arr:
        if i <0:
            print('Negetive! ')
            n+=1
        elif i>0:
            print('Positive!')
            p+=1
        elif i == 0:
            print('Zero! ') 
            z+=1     
    print("{0:.6f}".format(p/total))
    print("{0:.6f}".format(n/total))
    print("{0:.6f}".format(z/total))
    
if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
