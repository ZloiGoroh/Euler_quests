sum = 0
for i in range(999):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)


#неудачная попытка
#sum = 0
#sum = (0 + 995) * 995 / 5 * 2
#sum += (0 + 999) * 999 / 3 * 2
#sum -= (0 + 990) * 990 / 15 * 2
#print(sum)
