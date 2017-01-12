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
		print mst	

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
class LinkedList:
# Function to initialize head
	def __init__(self):
		self.head = None

# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def question5(self, m):
		main_ptr = self.head
		ref_ptr = self.head 

		count = 0
		if(self.head is not None):
			while(count < m ):
				if(ref_ptr is None):
					print "%d is not in the list" %(m)
					return

				ref_ptr = ref_ptr.next
				count += 1

		while(ref_ptr is not None):
			main_ptr = main_ptr.next
			ref_ptr = ref_ptr.next
		print main_ptr.data
		

llist = LinkedList()
sol=Solutions()
# Q1 INPUT 1
#sol.question1('anagram','nagaram')
#Expected Output:false
# Q1 INPUT 2
#sol.question1('','')
#Expected Output: false
# Q1 INPUT 3
#sol.question1('323','323')
#Expected Output: true
# Q2 INPUT 1
#sol.question2('babcbabcbaccba')
#Expected Output:abcbabcba
# Q2 INPUT 2
#sol.question2('abaaba')	
#Expected Output: abaaba		
# Q2 INPUT 3
#sol.question2('abacdfgdcaba')
#Expected Output:aba			
# Q2 INPUT 4
#sol.question2('abacdedcaba')
#Expected Output:abacdedcaba
# Q3 INPUT 1
'''
nodes = list("ABCDEFG")
edges = [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
      ("C", "E", 5),
      ("D", "E", 15), ("D", "F", 6),
      ("E", "F", 8), ("E", "G", 9),
      ("F", "G", 11)]

sol.question3( nodes, edges )
#Expected Output:[('A', 'D', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'C', 5), ('E', 'G', 9)]
'''
# Q3 INPUT 2
'''
nodes = list("ABCDEFG")
edges = [ ("A", "B", 0), ("A", "D", 2),
          ("B", "C", 0), ("B", "D", 0), ("B", "E", 1),
      ("C", "E", 1),
      ("D", "E", 0), ("D", "F", 1),
      ("E", "F", 0), ("E", "G", 0),
      ("F", "G", 1)]

sol.question3( nodes, edges )
#Expected Output:[('A', 'B', 0), ('B', 'C', 0), ('B', 'D', 0), ('D', 'E', 0), ('E', 'F', 0), ('E', 'G', 0)]	  	  
'''
# Q3 INPUT 3
'''
nodes = list("ABCDE")
edges = [ ("A", "B", 0), ("A", "D", 2),
          ("B", "C", 1), ("B", "D", 0), ("D", "E", 1),
      ("C", "D", 1)]
  
sol.question3( nodes, edges )
#Expected Output:[('A', 'B', 0), ('B', 'D', 0), ('B', 'C', 1), ('D', 'E', 1)]	  	  
'''
# Q5 INPUT 1
'''
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.question5(3)
#Expected Output: 3	
'''
# Q5 INPUT 2
'''
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.question5(10)
#Expected Output: 10 is not in the list	
'''
# Q5 INPUT 3
'''
llist.push(0)
llist.push(0)
llist.push(3)
llist.push(4)
llist.push(5)
llist.question5(5)
#Expected Output: 0
'''	