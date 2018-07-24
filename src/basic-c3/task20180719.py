# 四則演算

# 第一パラメータの入力
def inputX(x):
    while True:
        x = input('第一パラメータを入力してください: ')
        if x.isnumeric():
            return float(x)
        else:
            print('入力が不正です。やり直してください')
            continue

# 第二パラメータの入力
def inputY(y):
    while True:
        y = input('第二パラメータを入力してください: ')
        if y.isnumeric():
            return float(y)
        else:
            print('入力が不正です。やり直してください')
            continue

# 四則演算子の入力
def inputFour(user):
    while True:
        user = input('四則演算子を入力してください: ')
        if user in '+-*/':
            return user
        else:
            print('入力が不正です。やり直してください')
            continue

# 四則演算子の特定と計算
def fourCul(x, y, user):
    fourCulculate = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3
    }
    if fourCulculate[user] == 0:
        return x + y
    if fourCulculate[user] == 1:
        return x - y
    if fourCulculate[user] == 2:
        return x * y
    if fourCulculate[user] == 3:
        return round((x / y), 3)

# 表示
def display(d):
    print('計算結果:{}'.format(d))

# 起動
if __name__ == '__main__':
    display(fourCul(inputX(0),inputY(0),inputFour(0)))
