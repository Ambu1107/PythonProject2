#Print numbers between 1 to 20 skip the numbers divisible by 3 or 5
for i in range(1,21):
    if i%3!=0 and i%5!=0:
        print(i)