#2.2.1 Linear Search Technique
data=list(map(int,input().split()))
element=int(input())
for i in range(0,len(data)):
	#index=index+1
	if(data[i]==element):
		print(i)
		flag=1
		break
	else:
		flag=0
if (flag==0):
	print("Not found")
