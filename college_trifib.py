import sys

#Getting tribonacci for calculating the ways
def tribonacci(n):  
      
    #Possibilities from bottom, i.e. 2 at the leaf nodes of recursion tree .
    ways = [2, 4, 7]  
      
    for i in range(3, n): 
        ways.append(ways[i-1] + ways[i-2] + ways[i-3]) 
    print(ways)
    return ways[-1],ways[-2] 


#drivr function
def main():
	#taking input from the user      
	n = sys.stdin.readline()
	n1,n2 = tribonacci(int(n))
	ways = n1
	fails = n1-n2
	print(ways, "%d/%d"%(fails,ways)) 



if __name__ == '__main__':
	main()

