driving = input('請問您有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('請輸入有或沒有')
	raise SystemExit     #因為如果把輸入有或沒有放在最後，會在問完年齡才叫你改正
	                          #但我們想在問完有或沒有就改正，所以需要這個句子
age = input('請問您的年齡是?') #這個是字串，所以要轉換
age = int(age)
if driving == '有':
	if age >= 18:           #第二個if放後面是因為第一個if後面一定要有內容(if後面不能沒內容嘛)
		print('通過測驗')
	else:
		print('8可以8可以')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照')
	else:
		print('7414')
else:
	print('請輸入有或沒有')


