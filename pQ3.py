def solution(left, right):
    answer = 0

    
    for i in range(left, right+1):
        count = 0
        for c in range(1, i+1):
            if i%c == 0:
                count+=1
        
        if count%2:
            answer -= i
        else :
            answer += i
    
    return answer

left = 13
right = 17
c = solution(left, right)
print(c)