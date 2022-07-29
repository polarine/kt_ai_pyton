def list_max(a):
    
    c = 0
    maximum = a[0]

    for i in range(1,len(a)-1):
        if maximum < a[i]:
            maximum = a[i]
            c = i
        else:
            continue
    return maximum, c

a = []

num = int(input('원소의 수를 알려주세요.:'))
for i in range(0, num) :
    a.append(int(input(f'a[{i}]의 값을 알려주세요.:')))

max_n,index = list_max(a)

print(f'이 리스트에서 최댓값 {max_n}은 a[{index}]에 있습니다.')