from datetime import datetime

year1, year2 = map(int, input().split())	#두년을 입력합니다.
DoW = input()	#요일을 입력합니다.

day = 0	#날짜 일수 값을 둔다.

for a in range(year1, year2):	#윤년이면 366일을 더하고 윤년이 아니라면 365일을 더한다.
	if ((a % 4 == 0) and (a % 100 !=0) or a % 400 == 0):
		day = day + 366
	else:
		day = day + 365

		
if year2 >= year1:	#입력받은 요일을 토대로 리스트를 만들어 그 요일이면 날짜일수의 값에 7를 나눈 나머지를 이용하여 요일을 구한다.
	if DoW == '월':
			days = ['월', '화', '수', '목', '금', '토', '일']
			i = day % 7
			print(days[i])
	elif DoW == '화':
			days = ['화', '수', '목', '금', '토', '일', '월']
			i = day % 7
			print(days[i])
	elif DoW == '수':
			days = ['수', '목', '금', '토', '일', '월', '화']
			i = day % 7
			print(days[i])
	elif DoW == '목':
			days = ['목', '금', '토', '일', '월', '화', '수']
			i = day % 7
			print(days[i])
	elif DoW == '금':
			days = ['금', '토', '일', '월', '화', '수', '목']
			i = day % 7
			print(days[i])
	elif DoW == '토':
			days = ['토', '일', '월', '화', '수', '목', '금']
			i = day % 7
			print(days[i])
	elif DoW == '일':
			days = ['일', '월', '화', '수', '목', '금', '토']
			i = day % 7
			print(days[i])
elif year2 == year1:
	print(DoW)
	