'''
#The break statement ends the current loop and jumps to the statement immediately following the loop.
for i in range (1,11):
    if i == 5:
       break #terminate loop if i is 5 and stop
    print(i)
print("Loop is over.")
'''

#The continue statement ends the current iteration and jumps to the top of the loop and start next iteration.

for i in range (1,11):
    if i % 2 == 0:
        continue    # skip next statement if i is even and continue
    print(i)
print("Loop is over.")
