def fibonacci(n):
    #if(n < 0){
    #    print("Input shpuld be >=0")
    #    return null
	#}
    number1 = 0
    number2 = 1
    sum = 0
    count = 2
    
    while count <= n:
        count += 1
        sum = number1 + number2
        number1, number2 = number2, sum
	
    return sum

print(fibonacci(9))
