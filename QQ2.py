# Q2 Answer template

def solution(numbers):
    num_sum = 0
    for i in numbers:
        num_sum += i
    answer = 45-num_sum
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)