N = int(input('사이클을 알고 싶은 정수 N을 입력하시오. : '))
count=0

if N<0 or 99<N:
    print("정수의 입력이 잘못되었습니다.")
else:
    first_N = N
    N = ((N%10) * 10)+(((N//10)+(N%10))%10)
    count=1

while True:
    if first_N == N :
        break
    else :
        N = ((N%10) * 10)+(((N//10)+(N%10))%10)
        count += 1

print(count)