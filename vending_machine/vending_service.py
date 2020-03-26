from vending_machine.data0323 import Drink

balance=0  #使用者餘額
drinks = [
    Drink('可樂' ,25),      #{'name':'可樂','price': 25},
    Drink('雪碧' ,25),      #{'name':'雪碧','price': 25},
    Drink('奶茶' ,30),      #{'name':'奶茶','price': 30},
    Drink('紅茶' ,30),      #{'name':'紅茶','price': 30},
    Drink('BAR' , 49),       #{'name':'BAR','price': 49},
    Drink('18天生啤酒',60)  #{'name':'18天生啤','price': 60},
]    #飲料清單  #以上為全域變數

def add(x,y):
    """
    數字相加
    :param x: 數字!
    :param y: 數字2
    :return:  相加結果
    """
    return x+y

def deposit():      #函數是獨立的區塊
    """
    儲值功能
    :return: nothing
    """
    global balance      #告訴函數 外面的b可以去使用
    value = eval(input('儲值金額:'))
    while value < 1:      #錢不能是負數 所以要讓他一直重複問
        print('====儲值金額需大於零====')
        value = eval(input('儲值金額:'))
    balance += value
    print(f'儲值後金額為{balance}元')

def buy():
    global balance, drinks   #告訴此函數b,d可以用
    print('\n請選擇商品')  # 印出品項
    # for item in drinks:
    # print(f'{item["name"]}  {item["price"]}元')
    for i in range(0, len(drinks)):
        #print(f'({i + 1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')
        print(f'({i + 1})\t{drinks[i].name} \t {drinks[i].price}元')
    choose = eval(input('請選擇:'))

    while choose < 1 or choose > 6:
        print('====請輸入1-6之間====')
        choose = eval(input('請選擇'))

    buy_drink = drinks[choose - 1]
    #if balance < buy_drink['price']:
        #print('====餘額不足====')
    while balance < buy_drink.price:
        print('====餘額不足,需要儲值嗎?====')
        want_deposit = input('y/n : ')
        if want_deposit == 'y':
            deposit()   #呼叫儲值函數
        elif want_deposit == 'n':
            break      #不儲值就跳出迴圈
        else:
            print('====請重新輸入====')

    if balance >= buy_drink.price:
        print(f'已購買{buy_drink.name}  {buy_drink.price}元')
        balance -= buy_drink.price
        print(f'購買後的餘額為{balance}元')

    else:
        print(f'已購買{buy_drink.name}  {buy_drink.price}元')
        balance -= buy_drink.price
        print(f'購買後餘額為{balance}元')