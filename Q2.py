a=[]
i=0

print ('리스트를 입력받습니다')
print ('end를 입력받으면 역순 정렬이 시작됩니다.')

while True:
    
    answer = input(f'a[{i}]의 값을 입력해 주세요')
    
    if answer == 'end' :
        break
    else :
        a.append(int(answer))
        i += 1

n = len(a)

for c in range(n//2):
    a[c], a[n-c-1] = a[n-c-1], a[c]

print ('리스트 a를 역순 정렬한 값은', end='')
print (a)