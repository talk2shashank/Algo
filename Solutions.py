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
	
	
		
		
sol=Solutions()
# INPUT 1
#sol.question1('anagram','nagaram')
# INPUT 2
#sol.question1('','')				
		

	