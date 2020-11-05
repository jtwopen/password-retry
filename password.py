pwd = 'a123456' #密碼
i = 3 #可輸入次數
while i > 0:
	i = i - 1
	password = input('請輸入密碼')
	if password == pwd:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if i > 0:
			print('還有',i,'次機會')
		else:
			print('沒機會嘗試,要鎖帳號囉')
	

