import random  

def recursive_min(lst):  

    if len(lst) == 0: 
        return None  
    if len(lst) == 1: return lst[0]      
    
    first_num = lst[0]      
    remaining_lst = lst[1:]       
    min_from_remaining_lst = recursive_min(remaining_lst)      
    if first_num < min_from_remaining_lst:         
        return first_num     
    else:         
        return min_from_remaining_lst 

def recursive_max(lst): 
        
    if len(lst) == 0: 
        return None     
    if len(lst) == 1: 
        return lst[0]     
    first_num = lst[0]      
    remaining_lst = lst[1:]  
    max_from_remaining_lst = recursive_max(remaining_lst)     
    if first_num > max_from_remaining_lst:         
        return first_num     
    else:         
        return max_from_remaining_lst   

def main():     
    lst = [random.randint(1, 100) for _ in range(20)]    
    print(lst) # print the list     
    print('Minimum: {}'.format(recursive_min(lst)))    
    print('Maximum: {}'.format(recursive_max(lst)))  

main()