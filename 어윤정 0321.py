#a = input("2자리 숫자는 무엇입니까?")
#print(type(a))
#print(int(a[1]))
#print(int(a[0]))
#print(int(a[0]) + int(a[1]))

#height = input("당신의 키는 몇 cm :")
#weight = input("당신의 몸무게는 몇 kg :")
#bmi = int(weight) / float(height)**2
#bmi = int(70)/float(166)**2

#print(round(0.145676747234, 2))

#score = 0
#height = 1.6
#earth = True
#print(f"당신의 스코어는 {score}, 당신의 키는{height}, 당신은 지구인입니다.{earth}")

#age = input("당신의 나이는 몇살일까요?")
#age_as_int = int(age)
#years_remaining = 90 - age_as_int
#days_remaining = years_remaining * 365
#week_remaining = years_remaining * 52
#months_remaining = years_remaining * 12
#print(months_remaining)
#message = f"당신의 남은{days_remaining} 날, {week_remaining} 주, {months_remaining} 월"
#print(message)

#print(6+4/2-(1*2))

#print(150+(150*0.12))
#print(168/4)

# -- 팁계산기 --
# 총 얼마를 주문했을까? 150
# 팁은 몇% 12
# 팁을 포함해서 총 얼마를 내야할까? 168
# 몇명이 지불 해야될까? 4
# 1인당 지불 금액은? 42

#print("팁 계산기!")

#order = float(input("총 얼마를 주문했을까?"))
#tip = int(input("팁을 얼마나 주면 좋을까? 10, 12, or, 15 ?"))
#people = int(input("몇명이서 나눠서 낼까?"))

#tip_as_percent = tip / 100
#total_tip = order * tip_as_percent
#total_bill = total_tip + order
#bill_per_person = total_bill / people
# 소수점 둘째까지만
#final_bill = round(bill_per_person, 2)
#print(f("팁 포함해서 각자 내야되는 금액은:{final_bill} $"))

print("롤러코스터를 타러 오셨군요!")
height = int(input("키가 몇 cm입니까?"))

if height>=120:
    print("롤러코스터를 탈 수 있습니다!")
    age = int(input("당신은 몇 살입니까?"))
    if age < 12:
        print("무료입니다!")
    elif age <=18:
        print("7천원입니다")
    else:
        print("만2천원입니다")
else:
    print("죄송하지만 롤러코스터를 탈 수 없어요.")