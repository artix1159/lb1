print("Завдання 1")

a = float(input("Введіть значення a: "))
while a <= 0:
    print("a має бути додатнім числом. Спробуйте ще раз.")
    a = float(input("Введіть значення a: "))

b = float(input("Введіть значення b: "))
while b <= 0:
    print("b має бути додатнім числом. Спробуйте ще раз.")
    b = float(input("Введіть значення b: "))

if a > b:
    x = 5 * a + b
elif a == b:
    x = -125
else:
    x = (a - 5) / b

print("Значення X: ", x)

print("Завдання 2")

for i in range(-1, -52, -1):
  if i % 5 == 0:
      print(i)

print("Завдання 3")

while True:
  N = int(input("Введіть число N (1 < N < 9): "))
  if 1 < N < 9:
      break
  else:
      print("Невірне значення. Спробуйте ще раз.")

for i in range(N):
  for j in range(i+1, N+1):
      print(j, end=" ")
  print()

