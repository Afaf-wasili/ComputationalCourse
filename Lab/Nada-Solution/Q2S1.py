'''
n = [12, 5, 8, 13, 19, 24, 7, 10]  # Example list of numbers
sum_even = 0
sum_odd = 0
count_even = 0
count_odd = 0

# 1. Complete the loop below
for i in range(1, 8, 1):  # Hint: The loop iterates through the list n
    if n[i] % 2 == 0:
        # a) dd your logic here to update sum_even and count_even
    else:
        # b) Add your logic here to update sum_odd and count_odd

# c) Print the results
'''
n = [12, 5, 8, 13, 19, 24, 7, 10]  # Example list of numbers                                                                                                                                                    
sum_even = 0
sum_odd = 0
count_even = 0
count_odd = 0


for i in range(len(n)): 
    if n[i] % 2 == 0:
        # a) Update sum_even and count_even                                                                                                                                                                     
        sum_even += n[i]
        count_even += 1
    else:
        # b) Update sum_odd and count_odd                                                                                                                                                                       
        sum_odd += n[i]
        count_odd += 1

# c) Print the results                                                                                                                                                                                          
print(f"Sum of even numbers: {sum_even}")
print(f"Count of even numbers: {count_even}")
print(f"Sum of odd numbers: {sum_odd}")
print(f"Count of odd numbers: {count_odd}")


