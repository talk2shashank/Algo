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
	def uniquechars(self,str):
		if len(str) > 256:
			return False
		dupes=[]
		for n in str:
			if n in dupes:
				return False
			else:
				dupes.append(n)
		return dupes 
	def replceString(self,string1):
		stringlength= len(string1)
		spaces = 0
		newstr=[]
		#print(new_length)
		for n in string1:
			if n !=" ":
				newstr.append(n)
			else:
				newstr.append("0")
				newstr.append("2")
				newstr.append("%")
		return ''.join(newstr)		
	def question2(self,string):
		maxLength = 1
		start = 0
		length = len(string)
		low = 0
		high = 0
		for i in xrange(1, length):
			low = i - 1
			high = i
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
			low = i - 1
			high = i + 1
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
		print string[start:start + maxLength]
		
	
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
			cost, n1, n2 = heap( usable_edges )
			if n2 not in used:
				used.add( n2 )
				mst.append( ( n1, n2, cost ) )
				for e in conn[ n2 ]:
					if e[ 2 ] not in used:
						heappush( usable_edges, e )
		return mst	
	def findlongestString(self,string):
		maxLength = 1
		start = 0
		length = len(string)
		low = 0
		high = 0
		for i in xrange(1, length):
			low = i - 1
			high = i
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
			low = i - 1
			high = i + 1
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
		print string[start:start + maxLength]
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = next
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
class Node1:
    
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
	def findPath( root, path, k):
		if root is None:
			return False
		path.append(root.key)
    
		if root.key == k :
			return True
		if ((root.left != None and findPath(root.left, path, k)) or
				(root.right!= None and findPath(root.right, path, k))):
			return True
		path.pop()
		return False
	def DeleteNode(self,string):
		maxLength = 1
		start = 0
		length = len(string)
		low = 0
		high = 0
		for i in xrange(1, length):
			low = i - 1
			high = i
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
			low = i - 1
			high = i + 1
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
		print string[start:start + maxLength]
	def Removeuniquechars(self,str):
		if len(str) > 256:
			return False
		dupes=[]
		for n in str:
			if n in dupes:
				return False
			else:
				dupes.append(n)
		return dupes 	
	def longestPath( root, path, k):
		if root is None:
			return False
		path.append(root.key)
    
		if root.key == k :
			return True
		if ((root.left != None and findPath(root.left, path, k)) or
				(root.right!= None and findPath(root.right, path, k))):
			return True
		path.pop()
		return False	
	def findPath_helper1( root):
		if root is None:
			return False
		path.append(root.key)
    
		if root.key == k :
			return True
		if ((root.left != None and findPath(root.left, path, k)) or
				(root.right!= None and findPath(root.right, path, k))):
			return True
		path.pop()
		return False
	def findPath_helper2( root):
		if root is None:
			return False
		path.append(root.key)
    
		if root.key == k :
			return True
		if ((root.left != None and findPath(root.left, path, k)) or
				(root.right!= None and findPath(root.right, path, k))):
			return True
		path.pop()
		return False	
	def findPath_helper3( root1):
		if root is None:
			return False
		path.append(root.key)
    
		if root.key == k :
			return True
		if ((root.left != None and findPath(root.left, path, k)) or
				(root.right!= None and findPath(root.right, path, k))):
			return True
		path.pop()
		return False
	def findnode(self,string):
		maxLength = 1
		start = 0
		length = len(string)
		low = 0
		high = 0
		for i in xrange(1, length):
			low = i - 1
			high = i
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
			low = i - 1
			high = i + 1
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
		print string[start:start + maxLength]
	def Addnode_helper(self,string):
		maxLength = 1
		start = 0
		length = len(string)
		low = 0
		high = 0
		for i in xrange(1, length):
			low = i - 1
			high = i
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
			low = i - 1
			high = i + 1
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
		print string[start:start + maxLength]	
class Node2:
    
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
	def findPath_helper( root, path, k):
		if root is None:
			return False
		path.append(root.key)
    
		if root.key == k :
			return True
		if ((root.left != None and findPath(root.left, path, k)) or
				(root.right!= None and findPath(root.right, path, k))):
			return True
		path.pop()
		return False
	def AddNode(self,string):
		maxLength = 1
		start = 0
		length = len(string)
		low = 0
		high = 0
		for i in xrange(1, length):
			low = i - 1
			high = i
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
			low = i - 1
			high = i + 1
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
		print string[start:start + maxLength]	
	
	def findnode_helper(self,string):
		maxLength = 1
		start = 0
		length = len(string)
		low = 0
		high = 0
		for i in xrange(1, length):
			low = i - 1
			high = i
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
			low = i - 1
			high = i + 1
			while low >= 0 and high < length and string[low] == string[high]:
				if high - low + 1 > maxLength:
					start = low
					maxLength = high - low + 1
				low -= 1
				high += 1
		print string[start:start + maxLength]
	
		
llist = LinkedList()
sol=Solutions()
n=Node1(1)
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
#sol.question2('abaabaabaabaabaabaabaabaabaabaabaadbaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaba')	
#Expected Output: baabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaab		
# Q2 INPUT 3
#sol.question2('abacdfgdcaba')
#Expected Output:aba			
# Q2 INPUT 4
#sol.question2('abacded')
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
edges = [ ("A", "B", 1), ("A", "D", 1),
          ("B", "C", 1), ("B", "D", 1), ("D", "E", 1),
      ("C", "D", 1)]
  
sol.question3( nodes, edges )
#Expected Output:[('A', 'B', 0), ('B', 'D', 0), ('B', 'C', 1), ('D', 'E', 1)]	  	  
'''

# Q4 INPUT 1
'''
n.question4([0, 1, 1, 0, 1],[0, 0, 0, 1, 0],[1, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]],3,1,4)
#Expected Output:3
'''
# Q4 INPUT 2
'''
n.question4([0, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 1],[0, 0, 0, 0, 0]],2,1,1)
#Expected Output:1
'''
# Q4 INPUT 3
'''
n.question4([0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 0],[0, 0, 0, 0, 0]],1,1,0)
#Expected Output:0
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
