pwd = 'a123456' #密碼
i = 3 #可輸入次數
while True:
	password = input('請輸入密碼')
	if password == pwd:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤,還有',i,'次機會')
		if i == 0:
			break
			
