def list_search(a, key):
    ll = 0
    lr = len(a)
    
    while ll<lr:
        lc = (ll+lr)//2
        
        if a[lc] == key :
            return lc
        elif lc < key :
            lr = lc+1
        elif lc > key :
            ll = lc-1
    
    return -1
        
a = []

num = int(input('원소의 수를 알려주세요.:'))
for i in range(0, num) :
    a.append(int(input(f'a[{i}]의 값을 알려주세요.:')))
key = int(input('검색해야 하는 값을 입력해 주세요.:'))

index = list_search(a, key)

if index == -1:
    print('검색해야 하는 값이 리스트에 없습니다!')
else:
    print(f'검색해야 하는 값 {key}는 a[{index}]에 있습니다.')