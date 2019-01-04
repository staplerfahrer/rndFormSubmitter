import string
import random

def getForm(formTemplate):
	password = getPassword()
	randomized = \
	{
		'name':getName(),
		'email':getEmail(),
		'password':password,
		'passwordVerify':password,
	}
	return {**formTemplate, **randomized}

def getPassword():
	return idGenerator(size=rndLength(), chars=string.ascii_lowercase+string.ascii_uppercase+string.digits)

def getName():
	return idGenerator(size=rndLength(), chars=string.ascii_lowercase+string.ascii_uppercase+' ')

def getEmail():
	return idGenerator(size=rndLength(lower=7,upper=30), chars=string.ascii_lowercase+string.digits+'.'+'-'+'_') \
		+ '@' \
		+ idGenerator(size=rndLength(lower=7,upper=15), chars=string.ascii_lowercase+string.digits) \
		+ random.choice(['.com','.mx','.ca','.cn','.de','.be','.fr','.nl','.co.uk','.no'])

def rndLength(lower=5, upper=20):
	return random.choice(range(lower, upper))

def idGenerator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))