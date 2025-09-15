cheklist = []
tr = fl = 0
for n in range(int(input())):
    data = input().split()

    f = data[0] if len(data) > 0 else ""
    nm = data[1] if len(data) > 1 else ""
    age = data[2] if len(data) > 2 else ""
    bol = data[3] if len(data) > 3 else ""

    cheklist.append([f, nm, age, bol])
for i in range(len(cheklist)):
    print(f"in_{i+1}:", cheklist[i][0], cheklist[i][1], cheklist[i][2], cheklist[i][3])
    if cheklist[i][3] == 'True': tr += 1
    elif cheklist[i][3] == 'False': fl += 1
print("out:", tr, fl)