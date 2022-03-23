
roll_nums = [2,5,6,8,1]

roll_num = 9

def find_roll_number(lst,num):

    for i in lst:
       if i == num:
            return 1
    return 0

print(find_roll_number(roll_nums, roll_num))


