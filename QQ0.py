# Q0 Answer template

N, X = map(int, input().split())  # N, X 를 입력받음

data = list(map(int, input().split())) # 리스트를 입력받음

answer = []

for i in range(N):
    if data[i] < X:
        answer.append(data[i])
        
for j in range(len(answer)):        
    print(answer[j], end=' ')