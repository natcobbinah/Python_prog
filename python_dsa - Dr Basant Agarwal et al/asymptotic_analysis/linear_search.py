def linearSearch(search_arr, x):
    for i in range(len(search_arr)):
        if search_arr[i] == x:
            return i 
    return - 1

search_arr = [3,4,1,6,16]
x = 4
print("Index Pos for the element x is: ", linearSearch(search_arr,x))

# Analysis
# Best Case = if the element is found in the first position Omega(1)
# Worst Case = if the element is found in the last position or not found BigOh(n)
# Average Case =  if  the element is found in index 1,2...n /n Theta(n^2/2)