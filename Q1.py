a = []
n = 0

for i in range(2, 1001) :
    count = 0
    for j in range(2, i) :
        if i%j == 0:
            count = 1
            break
    if count == 0:
        a.append(i)
        n += 1
        
            
print(a)
print(f'리스트의 원소의 숫자는 {n}개 이다.')