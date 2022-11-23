def check_lottery():
    num = input() #str
    if 8>=(len(num))>= 2 and (len(num))%2==0:
        b = list(map(int, num)) #convert to numbers
        sumRight= 0
        sumLeft = 0
        half_list = int(len(b)/2)
        count = 0
        count_1 = half_list
    else: 
        print('invalid number')
        return False
                
    while count < half_list:
      sumRight = sumRight + b[count]
      count = count +1
    
    while  count_1 < len(b):
        sumLeft = sumLeft + b[count_1]
        count_1 = count_1 +1
            
    
    if sumLeft == sumRight:
        print("you won!")
        return True
    else:
        print('Bad luck, you lost!')
        return False
        
  
check_lottery()
  
    
   

