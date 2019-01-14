card = False
target = False
Debug.on(3)
while 1:
	#出牌階段
	if has("1547480888345.png"):
		Debug.user("player phase")
		#還沒選牌
		if (card == False):
			Debug.user("choosing card")
			#選擇殺
			if has("1547480933529.png"):
				Debug.user("choose kill")
				click("1547480933529.png")
				card = True
				wait(1)
		else:
			#要選目標
			if (target == False and has(Pattern("1547481588637.png").similar(0.30))):
				Debug.user("choosing target")
				target = True
				click(Pattern("1547481588637.png").similar(0.30))
				wait(1)
			#已選牌
			elif has(Pattern("1547481300855.png").exact()):
				Debug.user("choosed card")
				click("1547481300855.png")
				card = False
				target = False
				wait(1)
	#非出牌階段
	else:
		Debug.user("other phase")
		#等我出牌
		if has("1547483951986.png"):
			Debug.user("wait for me")
			if (card == False):
				#點閃
				if has("1547483065372.png"):
					Debug.user("click dodge")
					card = True
					click("1547483065372.png")
					wait(1)
			#點確定
			else:
				Debug.user("click confirm")
				card = False
				target = False
				click("1547481300855.png")
				wait(1)