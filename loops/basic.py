# Loops :- it is used for iterating over a sequence (like a list, tuple, or string) or performing a task repeatedly.
# There are two types of loops in Python: for loops and while loops.

# 1. For Loops
# Syntax :- for variable in range(start, stop, step) step - skip

for i in range(1, 5):  # This will iterate from 1 to 4 :- last 
    print(i)


# 2. While Loops

j = 1
while j < 5:
    print(j)
    j += 1

# break , continue , pass
# 1. break :- Terminates the loop and transfers control to the statement following the loop.

for i in range(1, 5):
    if i == 3:
        break
    print(i)

# 2. continue :- Skips the current iteration and proceeds to the next iteration of the loop.

for i in range(1, 5):
    if i == 3:
        continue
    print(i)

# 3. pass :- Does nothing and is used as a placeholder.
# where pass is used :- In situations where the code requires a statement syntactically but you do not want to execute any code.
for i in range(1, 5):
    if i == 3:
        pass
    print(i)


