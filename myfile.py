n = 9
number1 = 0
number2 = 1
sum = number2  
count = 1
 
while count <= n:
    print(sum, end=" ")
    count += 1
    number1, number2 = number2, sum
    sum = number1 + number2
print()
