data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = 1

for i in range(0, len(data)):
    if int(data[i])==0 or int(data[i])==1:
        result += int(data[i])
    else:
        result = result*int(data[i])

print(result)