##### 小技集

``` python
# 引数の肩を指定、戻り値はint
def is_int(s : str) -> int:
    try:
        num = int(s)
    except ValueError as e:
        print(e)
        return 1
    return 0

# リストのインデックスを同時に取得
L = ["aaa", "bbb", "ccc"]
for i,st in enumerate(L):
     print(i, st)

# 寄せ
print('left  : {:<10}'.format(100))
print('center: {:^10}'.format(100))
print('right : {:>10}'.format(100))
# left  : 100
# center:    100
# right :        100

# 0埋めprint('zero padding: {:0=10}'.format(100))
print('zero padding: {:010}'.format(100))
# zero padding: 0000000100
# zero padding: 0000000100

print('zero padding: {:0=10}'.format(-100))
print('zero padding: {:010}'.format(-100))
# zero padding: -000000100
# zero padding: -000000100

# ZIPで埋め合わせ
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
```
