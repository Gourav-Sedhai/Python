num = int(input("Enter number: "))

lst = []

for i in range(num):
    if i % 2 == 1:
        lst.append(i)

print(lst)