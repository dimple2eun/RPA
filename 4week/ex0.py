def sumfunc(num):
    sum = 0
    for j in range(1,num+1):
        sum = sum + j
    return sum

num = int(input("1이상의 정수를 입력하시오 : "))
sum = sumfunc(num)
print(f"1부터 {num}까지의 합은 {sum}입니다.")

if num <= 1:
    print("1이상의 정수를 입력하여 주세요")