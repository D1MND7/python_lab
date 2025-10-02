# python_lab
#lab2
### Задание1
### 1 arrays.py (min_max)
```python
def min_max(mns_mxs):
    if len(mns_mxs) != 0:
        return print (tuple([min(mns_mxs), max(mns_mxs)]))
    else:
        raise ValueError
min_max([3, -1, 5, 5, 0])
min_max([42])
min_max([-5, -2, -9])
min_max([])
min_max([1.5, 2, 2.0, -3.1])
```
![a1.png](images\lab02\a1.png)
### 2 arrays.py (unique_sorted)
```python
def unique_sorted(elements):
    elements = list(set(sorted(elements)))
    elements.sort(reverse=False)
    return elements
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![2.png]C:\Users\dimas\OneDrive\Рабочий стол\python_lab\images\lab02\a1.png)
### 3 arrays.py (flatten)
```python
def flatten(flatten_elem):
    result_sort = []
    for i in range(len(flatten_elem)):
        if type(flatten_elem[i]) in [list, tuple]:
            result_sort += list(flatten_elem[i])
        else:
            raise TypeError
    return result_sort
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![3.png]C:\Users\dimas\OneDrive\Рабочий стол\python_lab\images\lab02\a1.png)

#lab1
### Задание 1
```python
name = input("Имя: ")
age = input("Возраст: ")
print("Првиет, " + name + "!", "Через год тебе будет " + str(int(age)+1) + ".")
```
![1.png](images/lab01/1.png)


### Задание 2
```python
a = input()
b = float(input())
print("a: " + a.replace('.', ','))
print("b: " + str(b))
print("sum=" + f"{(float(a)+b):.2f}" + ";" + " avg=" + f"{(float(a)+b)/2:.2f}")
```
![2.png](images/lab01/2.png)

### Задание 3
```python
price=float(input())
discount=float(input())
vat=float(input())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print(f'База после скидки:{base:.2f}₽')
print(f'НДС:{vat_amount:.2f}₽')
print(f'Итого к оплате:{total:.2f}₽')
```
![3.png](images/lab01/3.png)

### Задание 4
```python
m = int(input("Минуты: "))
print(str(m//60) + ":" + f"{(m%60):02d}")
```
![4.png](images/lab01/4.png)

### Задание 5
```python
a, b, c = map(str, input().split())
print("ФИО: ", a, b, c)
print("Инициалы: ", a[0] + b[0] + c[0] + '.')
print("Длина (символов): " + str(len(a) + len(b) + len(c) + 2))
```
![5.png](images/lab01/5.png)
