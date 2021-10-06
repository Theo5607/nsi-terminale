class Polynomial:
    def __init__(self, polylist):
        if not isinstance(polylist, list):
            raise ValueError("Ceci n'est pas une liste",str(polylist))
            
            self.lpolynome = polylist

#x**3  +  4x**2  +     +9  =  [9,0,4,1]  * [8,9,5,0]
def multiplication(p1,p2):
    new = [0]*(len(p2)+len(p1)-1)
    
    for i in range (len(p2)):
        for x in range(p2[i]):
            for el in p1:
                new+=el 

        
        
new=[0,0,0,0,0,0,0]
