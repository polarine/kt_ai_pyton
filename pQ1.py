
def solution(a, b):
    if a>b:
        a,b = b,a

    for i in range(b, a*b+1):
        if i%a==0 and i%b==0 :
            answer=i
            break
        
    return answer

a = 12
b = 16
c = solution(a, b)
print(c)