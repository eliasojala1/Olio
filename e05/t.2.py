class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
 
        määrä = {}        
        for item in my_list:
            if item in määrä:
                määrä[item] += 1  
            else:
                määrä[item] = 1  
        
        max = 0
        yleisin = None
        
        for key, value in määrä.items():
            if value > max: 
                max = value
                yleisin = key
        
        return yleisin
    
    @classmethod
    def doubles(cls, my_list):
        määrä = {}
        for item in my_list:
            if item in määrä:
                määrä[item] += 1
            else:
                määrä[item] = 1
        
        doubles = 0
        for key in määrä:
            if määrä[key] >= 2:
                doubles += 1 
        
        return doubles

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))  
print(ListHelper.doubles(numbers))
