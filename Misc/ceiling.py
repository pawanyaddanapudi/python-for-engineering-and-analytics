
def solution(A):
    # write your code in Python 3.6
    all_postives = range(1,1000000)
    non_existing_list = [x for x in all_postives if x not in A]
    print(min(non_existing_list))
    pass

solution([1,2,3])

def solution(A):
    # write your code in Python 3.6
    i = 0
    A_sort = list(set(A))
    A_sort.sort()
    a = 1
    while i == 0:
        if a in A_sort:
            a+=1
        else:
            print(a)
            i = 1
    pass


def solution(A):
    B = list(filter(lambda x: x > 0, A))
    print(len(B))
    if len(B) == 0:
        return 1
    else:
        C = list(map(lambda x:x+1, B))
        print(C)
    pass

solution([1,2])

import math
import pulp as p
a = [1,0,0,1,1,1]
a = [1,0,0,1,1]
b = range(len(a))
list_values = []
for x in range(len(a)):
    c.append((-2) ** x)




print(c)
multi_output = [v * s for v, s in zip(a, c)]
total = sum(multi_output)
c_val = math.ceil(total/2)
b = []
for x in range(c_val):
    b.append((-2) ** x)

x = p.LpVariable("x", dicts=b)
y = p.LpVariable("y", lowBound = 0)



list_values = []
for x in range(len(A)):
    list_values.append((-2) ** x)

multi_output = [v * s for v, s in zip(A, list_values)]
c_val = math.ceil(total/2)
possible_vals = []
for x in range(c_val):
    possible_vals.append((-2) ** x)

all_ones = []
for x in range(c_val):
    all_ones.append(1)
prob = p.LpProblem("Find pattern",p.LpMinimize)
var_lp = p.LpVariable.dicts("possible_vals",possible_vals,lowBound=0,cat='Discrete')
prob += p.lpSum([possible_vals[i]*all_ones[i] for i in range(c_val)]) == c_val
prob.solve()
