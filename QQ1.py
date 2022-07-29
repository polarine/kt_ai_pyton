def solution(lottos, win_nums):
    answer = []
    hit = 0
    z_num = 0
    
    for i in lottos:
        if i == 0:
            z_num+=1
        else :
            for j in win_nums:
                if i == j:
                    hit += 1
    
    max_hit = z_num+hit
    
    if hit <=1:
        minimum = 6
    elif hit == 2:
        minimum = 5
    elif hit == 3:
        minimum = 4
    elif hit == 4:
        minimum = 3
    elif hit == 5:
        minimum = 2
    elif hit == 6:
        minimum = 1
    
    if max_hit <=1:
        maximum = 6
    elif max_hit == 2:
        maximum = 5
    elif max_hit == 3:
        maximum = 4
    elif max_hit == 4:
        maximum = 3
    elif max_hit == 5:
        maximum = 2
    elif max_hit == 6:
        maximum = 1
    
    answer.append(maximum)
    answer.append(minimum)
    return answer
                
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)