n = int(input())
perfect_numbers = []

for num in range(1, n + 1):
    if num <= 1:
        continue  # 1不是完数
    sum_divisors = 1  # 1是所有数的因子
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:  # 避免重复添加平方数因子
                sum_divisors += num // i
    if sum_divisors == num:
        perfect_numbers.append(str(num))

print(''.join(perfect_numbers))
