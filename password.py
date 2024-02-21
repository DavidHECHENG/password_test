x = 3
pwd = 'lovezoe'
while True :
    password = input('請輸入密碼：')
    if password == pwd :
        print('恭喜答對！')
        break
    elif password != pwd and x >= 0 :
        x = x - 1
        if x == 0 :
            print('密碼錯誤！您已使用完所有機會')
            break
        print('密碼錯誤！您還有',x,'次機會')