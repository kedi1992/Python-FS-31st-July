def add_num(a, b, c):
    return a + b + c



result = map(add_num, [10, 20, 30], (40, 50, 60), {70, 80, 90})
print(list(result))