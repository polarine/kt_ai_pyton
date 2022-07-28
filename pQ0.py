a= int(input('a : '))
b= int(input('b : '))


def solution(a, b):
    if a>b:
        a,b = b,a

    for i in range(a, 0, -1):
        if a%i==0 and b%i==0 :
            answer=i
            break
    
    return answer


c=solution(a,b)
print(c)
