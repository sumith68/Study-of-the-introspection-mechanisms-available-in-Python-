import cll  #cll.py contain a base class bcd and a class which inheirted the 		base class	
import types
def f():
	"""  it checks class type and checks the inherited class and if it contains a method start with 'test' that method execute """
	res,b,c=[],[],[]
	s=dir(cll)
	for i in s:
		if type(getattr(cll,i))==types.ClassType:
			c.append(i)
	for i in c:
		bas=getattr(cll,i).__bases__
		if getattr(cll,'bcd') in bas:
	      		res.append(i)
	for j in res:
		result=dir(getattr(cll,j))
		for i in result:
			if type(getattr(getattr(cll,j),i))==types.MethodType:
				if i[:4]=='test':
					inst=getattr(cll,j)()
					getattr(inst,i)()		
				
		
f()
