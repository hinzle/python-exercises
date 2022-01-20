# 1.a
x=input('Enter day of the week: ')
if x in ['Monday', 'monday', 'mon']:
	print(f'Today is {x}.')
else:
	print('Today is not Monday.')

# 1.b
x=input('Enter day of the week: ')
if x in ['Saturday', 'Sunday' ]:
	print(f'Today is a weekend.')
else:
	print('Today is a weekday.')

# 1.c
hours_worked=50
hourly_rate=100
if hours_worked>40:
	weeks_pay=((hours_worked-40)*1.5*hourly_rate)+(40*hourly_rate)
else:
	weeks_pay=hours_worked*hourly_rate	
print(f'Weeks pay is ${weeks_pay}.')

# 2.a

#5 to 15
i=5
while i<=15:
	print(i)
	i+=1

# 0 to 100, by 2's
i=0
while i<=100:
	print(i)
	i+=2
	
# 100 to -10, by 5's
i=100
while i>=-10:
	print(i)
	i-=5

# fibonacci seq but with *
i=2
while i<1000000:
	print(i)
	i=i**2

# 100 to 5, by 5's
i=100
while i>=5:
	print(i)
	i-=5

# 2.b.i
x=input('Enter a number:')
x=float(x)
ints=list(range(1,11))
for n in ints:
	ans=x*n
	print(f'{x} x {n} = {ans}')
	
# 2.b.ii
ints=list(range(1,10))
for n in ints:
	ans=n*str(n)
	print(ans)

#2.c.i
n=input('Enter a number | 1<+n<=50 & n%2!=0: ')

while n>=1 and n<=50:
	print('Hi')	
	if n%2!=0:
		print('Number to skip is: {n}')

	break
	
n=10
x=n%3
print(x)






