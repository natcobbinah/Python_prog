# creating a telephone directory demo using tuple
def create_telephone_directory(list_of_tuples,phone_nums):
    d = dict()
    for x,y in list_of_tuples:
        d[x] = phone_nums[y]
    return d

   
demo_list = [('fred cobs',0), ('nat cobs',1)]
phone_nums = [100,200]
print(create_telephone_directory(demo_list,phone_nums))