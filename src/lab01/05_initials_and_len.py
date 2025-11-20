a, b, c = map(str, input().split())
print("ФИО: ", a, b, c)
print("Инициалы: ", a[0] + b[0] + c[0] + ".")
print("Длина (символов): " + str(len(a) + len(b) + len(c) + 2))
