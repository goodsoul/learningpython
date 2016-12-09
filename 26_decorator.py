# -*- coding: utf-8 -*-

def now():
	print('YES')
	
f=now
f()

print(now.__name__)
print('\n')

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' %func.__name__)
		return func(*args, **kw)
	return wrapper
	
@log
def now():
	print('YES')


now()
print('\n')	

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator