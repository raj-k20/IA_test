import sys

n = sys.stdin.readline()

class ReferenceInt:
	def __init__(self):
		self.val = 0
	def increment(self):
		self.val += 1


def build_ways(arr,fails,n):
	#print(arr)
	if len(arr) == n:
		if arr[-1] == 0:
			fails.increment()

		return 1
	if len(arr) >1 and arr[-2] == 0 and arr[-1] == 0:
			return build_ways(arr+[1],fails,n)
	
	return build_ways(arr+[1],fails,n) + build_ways(arr+[0],fails,n)

def get_ways(n):
	arr = [1,0]
	ways = 0
	fails = ReferenceInt()
	for k in arr : 
		tways = build_ways([arr[k]],fails,int(n))
		ways += tways
	print(ways, "%d/%d"%(fails.val,ways))
get_ways(n)
