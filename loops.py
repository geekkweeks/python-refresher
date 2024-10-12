numbers = [1,2,4,5,6,7,8,9,10,11,12,13,14]

sum_for_loop = 0

for x in numbers:
    sum_for_loop += x

print(sum_for_loop)

sum_for_loop = 0

i = 0
while i < len(numbers):
    sum_for_loop += numbers[i]
    i+=1

print(sum_for_loop)

y = 0
while y < 5:
    y += 1
    if y == 2:
        continue
    print(y)
    if y == 4:
        break
else:
    print("y is now larger or equal 5")
