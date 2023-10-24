def rotate_list(input_list, k):
   arr_size = len(input_list)
   reverse_array(input_list, 0, arr_size - 1)
   reverse_array(input_list, 0, k - 1)
   reverse_array(input_list, k, arr_size - 1)
   return input_list

def reverse_array(arr, start, end):
   i  = start 
   j  = end 
   while i < j:
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp 
      i = i + 1
      j = j - 1
   return arr

user_input = [1,2,3,4,5,6,7,8,9,10]
print(rotate_list(user_input, 2))
