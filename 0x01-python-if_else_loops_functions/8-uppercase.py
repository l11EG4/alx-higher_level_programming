#!/usr/bin/python3
def uppercase(str):
	upp = ''
	for s in str:
		if ord(s) > 96 and ord(s) < 123:
			s = chr(ord(s) - 32)
		upp = upp + s
	print('{}'.format(upp))
