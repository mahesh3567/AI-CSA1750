import numpy as np
def relu(n):
    if n<0:
        return 0
    else:
        return n

inp=np.array([[-1,2],[2,2],[3,3]])
weights=[np.array([3,3]),np.array([1,5]),np.array([3,3]),np.array([1,5]),np.array([2,-1])]
for x in inp :
    node0=relu((x*weights[0]).sum())#node0 weight
    node1=relu((x*weights[1]).sum())#node 1 weight
    node2=relu(([node0,node1]*weights[2]).sum())#node 2 using node 0 and node 1
    node3=relu(([node0,node1]*weights[3]).sum())#node 3 using node 0 and node 1
    op=relu(([node2,node3]*weights[4]).sum())#final output from  node2 and node 3 
    print(x,op)