x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
op = input("Введите оператор (+,-,/,*): ")

if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "/":
    result = x / y
elif op == "*":
     result = x * y

print("Результат: ", result)
