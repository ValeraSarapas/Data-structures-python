from sys import stdin
n = int(next(stdin))
#print("n",n)
A = list(map(int,next(stdin).split()))
#print("A",A)
m = int(next(stdin))
#print("m",m)

inp = []
i_max = []
out = []
o_max = []

def m_stack(stack,maxes,com):
    if com[0] == "push":
        new = com[1]
        stack.append(new)
        maxes.append(max(new,maxes[-1]) if maxes else new)
    elif com[0] == "pop":
        return stack.pop(), maxes.pop()
    elif com[0] == "max":
        return maxes[-1] if maxes else None
    
for a in A[:m-1]:
    m_stack(inp,i_max,('push',a))
#print(inp,i_max)  
    

#print(out,o_max)  

for a in A[m-1:]:
    m_stack(inp,i_max,('push',a))
#    print("--",inp,i_max)  
    if len(inp) >= m and len(out) == 0:
        for _ in range(len(inp)):
            a = m_stack(inp,i_max,('pop',None))
            m_stack(out,o_max,('push',a[0]))
    a = m_stack(out,o_max,('pop',None))
    i_m =  m_stack(inp,i_max,('max',None))
    o_m = max(i_m,a[1]) if inp else a[1]
    print(o_m, end = " ")
