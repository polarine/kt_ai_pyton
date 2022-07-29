print('리스트를 역순으로 출력합니다.')
num = int(input('원소 수를 입력하세요.:'))
x = [None]*num

for i in range (num) :
    x[i] = int(input(f'x[{i}]값을 입력하세요.:'))
   
for i in range(num//2):
    x[i], x[num-i-1] = x[num-i-1], x[i]
 
print('리스트를 역순으로 출력합니다.')

for i in range(num):
    print(f'x[{i}] = {x[i]}')