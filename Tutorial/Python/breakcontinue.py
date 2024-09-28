'''
#The break statement ends the current loop and jumps to the statement immediately following the loop.
for i in range(2,8):
  #  print("i before",i)
    if i % 2 == 0:
       break     #terminate loop if i is 5 and stop
    print(i)
#print("Loop is over.")

'''



'''
#The continue statement ends the current iteration and jumps to the top of the loop and start next iteration.
for i in range (1,11):
    if i == 5:
       continue      #terminate loop if i is 5 and stop
    print(i)

'''

'''
for i in range (2,8):
    if i % 2 == 0:
        continue    # skip next statement if i is even and continue
    print(i)
print("Loop is over.")

'''

n = [1,2,3,4,5,6,7,8]
for i in range(len(n)):
    if n[i] % 2 ==0:
       continue
    print(n[i])
print("Loop is over.")  
