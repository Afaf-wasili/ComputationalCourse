
n = [12, 5, 8, 13, 19, 24, 7, 10]  # Example list of numbers
sum_even = 0
sum_odd = 0
count_even = 0
count_odd = 0

# 1. Complete the loop below
for i in range(len(n)):  # Hint: The loop iterates through the list n
    if n[i] % 2 == 0:
        # a) dd your logic here to update sum_even and count_even
        sum_even += n[i]
        count_even += 1
    else:
        # b) Add your logic here to update sum_odd and count_odd
        sum_odd += n[i]
        count_odd += 1

# c) Print the results
print ("The sum_even = ", sum_even)
print ("The count_even = ", count_even)
print ("The sum_odd = ", sum_odd)
print ("The count_odd = ", count_even)
