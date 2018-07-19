import sys
menu = {
    'Drip Coffee': 280,
    'ColdBrewCoffee': 320,
    'CafeLatte': 330,
    'SoyLatte': 380,
    'Cappuccino': 330,
    'CaramelFrappuccino': 470,
    'MacchaCreamFrappuccino': 470
}

option = {
    'LowFatMilk': 0,
    'NonFatMilk': 0,
    'SoyMilk': 50,
    'DeepCoffee': 60,
    'WhipCream': 70,
    'CaramelShrup': 60,
    'ChocoSource': 0,
    'DeCafe': 50
}
menu_p = '''
 +------Coffee menu------+---Price---+
 | DripCoffee            |   280円   |
 | ColdBrewCoffee        |   320円   |
 | CafeLatte             |   330円   |
 | SoyLatte              |   380円   |
 | Cappuccino            |   330円   |
 | CaramelFrappuccino    |   470円   |
 | MacchaCreamFrappuccino|   470円   |
 +---------option--------+---Price---+
 | LowFatMilk            |    無料   |
 | NonFatMilk            |    無料   |
 | SoyMilk               |    50円   |
 | DeepCoffee            |    60円   |
 | WhipCream             |    70円   |
 | Caramelshrup          |    60円   |
 | ChocoSource           |    無料   |
 | DeCafe                |    50円   |
 +-----------------------------------+
'''
print(menu_p)
menu_v = []
menu_f = []

while True:
    user_main = input('メインメニューを入力してください:')
    if user_main in menu.keys():
        menu_v.append(user_main)
        menu_f.append(menu[user_main])
        break
    elif user_main == 'q' or user_main == '':
        print('注文をキャンセルします')
        sys.exit()
    else:
        print('存在しないメニューです。')

print('メインメニューを承りました。')

while True:
    user_option = input('オプションメニューを選んでくだし。:')
    if user_option in option.keys():
        menu_v.append(user_option)
        menu_f.append(option[user_option])
        continue
    elif user_option == 'q' or user_option == '':
        print('注文内容は、{}, '.format(menu_v))
        print('カウンターに戻ります')
        break
    else:
        print('ないです')
        continue

money = sum(menu_f)
print('注文内容は{}'.format(menu_v))
print('合計金額は{}円です。'.format(money))
