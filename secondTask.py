#Cчитает сумму всех чётных чисел фибонначи, которыее меньше 4 000 000
sum = 0
k = 1
a = [0, 1]
i = a[k] + a[k - 1]
while i < 3.5e+6:
    i = a[k] + a[k - 1]
    a.append(i)
    k += 1
    if i % 2 == 0:
        sum += i
print(sum)          #что-то мне подсказывает, что второй способ быстрее
print(a)
sum = 0
for j in range(0, len(a), 3):
    sum += a[j]
print(sum)
