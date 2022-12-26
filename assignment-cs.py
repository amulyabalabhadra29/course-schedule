def order(n, pre):
    res = []
    # indegrees for a course
    # represents the number of courses needs to be completed before taking this course
    ind = [0 for i in range(n)]
    # a queue is used but we can also use a stack and by defalut list can be used as a stack
    stk = []
    for i in pre:
        # this course is prerequisite of the list present at it's index
        # incrementing one for all those courses(indegrees are calculated)
        for j in i:
            ind[j] += 1
    # Courses having no prerequisites can directly be taken so those will be added to stack
    for i in range(n):
        if ind[i] == 0:
            stk.append(i)
    # Iterating until all the courses with prerequisited completed are present
    while len(stk) > 0:
        # taking the top element from stack and removing it from stack
        x = stk[-1]
        stk.pop()
        # adding the course having no prerequisite to be completed to result
        res.append(x)
        # now if course x has been completed, a prerequisite has been completed for other courses
        # those courses can be taken from 'pre' list
        for i in pre[x]:
            ind[i] -= 1
            # adding the course to the stack if all of it's prerequisites has been completed
            if ind[i] == 0:
                stk.append(i)
    # if all the courses are not added to the result, it is impossible to have an order of courses in learning track
    if len(res) != n:
        res = []
    return res

# Count of number of Courses to be done
n = int(input())
# Count of Prerequisites as pairs to be taken
q = int(input())
# List to store Prerequisites for a course at a given index
pre = [[] for i in range(n)]
# Taking the inputs to create a preerequisite table
for i in range(q):
    x, y = list(map(int, input().split()))
    # Course x is prerequisite of y
    pre[x].append(y)
# Function called which returns the required order for completing the courses
res = order(n, pre)
# If a correct order of courses obtained, print the order otherwise printing as impossible
if len(res) > 0:
    # Printing the order of the courses
    print(*res)
else:
    print('Impossible')
