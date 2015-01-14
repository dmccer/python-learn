import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

@log
def prod(L):
	if not L:
		return

	return reduce(lambda x,y: x*y, L)

print prod([])
print prod([1, 2, 3, 4])

class Chain(object):
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	def __call__(self, val):
		return Chain('%s/%s' % (self._path, val))

print Chain().status.user.timeline.list

print Chain().users('Michal').repos

