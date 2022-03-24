
#created list of roll numbers
roll_nums = [2,5,6,8,1]

# target roll number have to find in list 
roll_num = 9

#created function, passing list and target roll number in it
def find_roll_number(lst,num):

# Used for loop to iterate on list, one by one element will be sent to i
    for i in lst:
    
    # checking if i is equals to target roll number
       if i == num:
            return 1
            
    # if list dont contain target roll number 0 will be returned
    return 0

# calling function and passed roll numbers list as well as targeted roll number and printing returned value from function 
# after  linear search
print(find_roll_number(roll_nums, roll_num))

