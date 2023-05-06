students = [100,90,80,70,60,50,40,30,20,10,0]

passed_students = list(filter(lambda x: x>= 60 & x <= 40, students))

print(passed_students)