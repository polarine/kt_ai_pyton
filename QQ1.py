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
    
    answer.append(hit)
    answer.append(hit+z_num)
    return answer
                
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)