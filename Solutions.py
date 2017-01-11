from collections import defaultdict
from heapq import *
class Solutions:
	def question1(self,s, t):
		string1=sol.question1_helper(s)
		string2=sol.question1_helper(t)
		if string1==string2:
			print "true"
		else:
			print "false"
	def question1_helper(self,s):
		ascii_string_array=[]
		ascii_string_array = [ord(c) for c in s.lower()]
		ascii_multiply=1;
		for s in ascii_string_array:
			ascii_multiply = s * ascii_multiply
		return ascii_multiply
	
	def question2(self,a):
		N = len(a)
		if N == 0:
			return
		N = 2*N+1 # Position count
		L = [0] * N
		L[0] = 0
		L[1] = 1
		C = 1	 # centerPosition
		R = 2	 # centerRightPosition
		i = 0 # currentRightPosition
		iMirror = 0	 # currentLeftPosition
		maxLPSLength = 0
		maxLPSCenterPosition = 0
		start = -1
		end = -1
		diff = -1

		# Uncomment it to print LPS Length array
		# printf("%d %d ", L[0], L[1]);
		for i in xrange(2,N):
	
		# get currentLeftPosition iMirror for currentRightPosition i
			iMirror = 2*C-i
			L[i] = 0
			diff = R - i
		# If currentRightPosition i is within centerRightPosition R
			if diff > 0:
				L[i] = min(L[iMirror], diff)

		# Attempt to expand palindrome centered at currentRightPosition i
		# Here for odd positions, we compare characters and
		# if match then increment LPS Length by ONE
		# If even position, we just increment LPS by ONE without
		# any character comparison
			try:
				while ((i+L[i]) < N and (i-L[i]) > 0) and \
					(((i+L[i]+1) % 2 == 0) or \
					(a[(i+L[i]+1)/2] == a[(i-L[i]-1)/2])):
					L[i]+=1
			except Exception as e:
				pass

			if L[i] > maxLPSLength:	 # Track maxLPSLength
				maxLPSLength = L[i]
				maxLPSCenterPosition = i

		# If palindrome centered at currentRightPosition i
		# expand beyond centerRightPosition R,
		# adjust centerPosition C based on expanded palindrome.
			if i + L[i] > R:
				C = i
				R = i + L[i]

		
		start = (maxLPSCenterPosition - maxLPSLength) / 2
		end = start + maxLPSLength - 1
		print "LPS of string is " + a + " : ",
		print a[start:end+1],
		print "\n",
	def question3(self,nodes, edges ):
		conn = defaultdict( list )
		for n1,n2,c in edges:
			conn[ n1 ].append( (c, n1, n2) )
			conn[ n2 ].append( (c, n2, n1) )

		mst = []
		used = set( [nodes[ 0 ]] )
		usable_edges = conn[ nodes[0] ][:]
		heapify( usable_edges )

		while usable_edges:
			cost, n1, n2 = heappop( usable_edges )
			if n2 not in used:
				used.add( n2 )
				mst.append( ( n1, n2, cost ) )
				for e in conn[ n2 ]:
					if e[ 2 ] not in used:
						heappush( usable_edges, e )
		return mst	
		
sol=Solutions()
# Q1 INPUT 1
#sol.question1('anagram','nagaram')
# Q1 INPUT 2
#sol.question1('','')
# Q2 INPUT 1
#sol.question2('babcbabcbaccba')
# Q2 INPUT 2
#sol.question2('abaaba')			
# Q2 INPUT 3
#sol.question2('abacdfgdcaba')			
# Q2 INPUT 4
#sol.question2('abacdedcaba')
nodes = list("ABCDEFG")
edges = [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
      ("C", "E", 5),
      ("D", "E", 15), ("D", "F", 6),
      ("E", "F", 8), ("E", "G", 9),
      ("F", "G", 11)]			
#sol.prim( nodes, edges )
print "prim:", sol.question3( nodes, edges )
	