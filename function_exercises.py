# 1

def is_two(x):
	"It should accept one input and return True if the passed input is either the number or the string 2, False otherwise."
	if type(x)==int and x == 2:
		return True
	elif type(x)==str and x.lower() == 'two':
		return True
	else:
		return False

is_two(0)
is_two(2)
is_two('zero')
is_two('Two')
is_two('two')

# 2

def is_vowel(x):
	"should return True if the passed string is a vowel, False otherwise"
	if type(x)==str and x.lower() in ['a','e','i','o','u']:
		return True
	else:
		return False

is_vowel('a')
is_vowel('b')
is_vowel('D')
is_vowel('E')

# 3

def is_consonant(x):
	"should return True if the passed string is a consonant, False otherwise"
	if is_vowel(x):
		return False
	else:
		return True

is_consonant('a')
is_consonant('b')
is_consonant('D')
is_consonant('E')

# 4

def capitalizer(x):
	x=list(x)
	if x[0].islower and is_consonant(x[0]):
		x[0]=x[0].upper()
		x=' '.join(x)
		print(x)


capitalizer('frank')



