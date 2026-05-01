#1.2.1 Pass or Fail
def result(courses,marks):
	if any (i<40 for i in marks):
		print("Fail")
	else:
		percentage=sum(marks)/(courses*100)*100
		if(percentage>75):
			grade="Distinction"
		elif(percentage>=60):
			grade="First Division"
		elif(percentage>=50):
			grade="Second Division"
		else:
			grade="Third Division"
		print(f"Aggregate Percentage: {percentage:.2f}")
		print(f"Grade: {grade}")
courses=int(input())
marks=list(map(int,input().split()))
result(courses,marks)
