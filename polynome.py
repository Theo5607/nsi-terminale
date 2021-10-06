class Polynomial:
    def __init__(self, polylist):
        if not isinstance(polylist, list):
            raise ValueError("Ceci n'est pas une liste",str(polylist))
            
            self.lpolynome = polylist
