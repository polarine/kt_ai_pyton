
def line(a, key):
    i=0
    count = 0
    
    while True:
        count += 2
        if i == len(a):
            print('검색결과 없음')
            break
            
        if a[i] == key:
            print(f'검색결과 a[{i}]에 있음')
            print(f'선형 검색에서 if문은 {count}번 실행되었다.')
            break
        i += 1
    
    
        
def lineG(a, key):
    b = a.copy()
    b.append(key)
    i = 0
    count = 0
    
    
    while True:
        count += 1
        if a[i] == key:
            break
        i += 1
    
    if i==len(b):
        print('검색결과 없음')
    
    else :
        print(f'검색결과 a[{i}]에 있음')
        print(f'보초법을 쓴 선형 검색에서 if문은 {count}번 실행되었다.')


a = [2, 5, 1, 3, 9, 6, 7]
line(a, 7)
lineG(a, 7)
