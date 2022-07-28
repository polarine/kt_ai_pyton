data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = int(data[0])

print(result, end=' ')

for i in range(1, len(data)):
    if int(data[i])<=1 or result <=1:
        result += int(data[i])
        print('+ '+ data[i], end=' ')
    else:
        result = result*int(data[i])
        print('x '+ data[i], end=' ')

print(' = ' + str(result))