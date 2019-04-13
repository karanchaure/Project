def s2b (s):
	
	for i in s :
		val=ord(i)
		a=[]
		while val>0:
			if val%2==0 :
				a.append(0)
			else :
				a.append(1)
			val=val/2	
		a.reverse()
		print a,
		print "-",i	,
		a=None			
				
 

Str=raw_input("Enter the String")
s2b(Str	)
 
  
       
