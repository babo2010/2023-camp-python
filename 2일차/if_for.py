password=2010
masterpw=1234567899

num=int(input('비밀번호를 입력해주세요:'))
if password==num:
    print('문이 열렸습니다')
elif masterpw==num:
    print('다른 사람들은 못 들어오는 문이 열렸습니다.')
else: 
    print('번호가 맞지 않습니다. 다시 입력 해주세요')
