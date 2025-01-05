#leetcode
#485. Max Consecutive Ones

#my solution
nums = [1,1,0,1,1,1]
counter = 0
max_count = 0
for i in nums:
    if i==1:
        counter+=1
    else:
        if counter > max_count:
            max_count = counter
        counter=0
if counter > max_count:
    print(counter)
else:
    print(max_count)


#Optimal code(Above code is already optimal but the code can be optimized)
#chatgpt solution
nums = [1,1,0,1,1,1]
counter = 0
max_count = 0
for i in nums:
    if i == 1:
        counter += 1
        max_count = max(max_count, counter)  # Update max_count directly
    else:
        counter = 0  # Reset counter when 0 is encountered
        
print(max_count)