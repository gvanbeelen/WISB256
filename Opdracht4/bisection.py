def findRoot(f,a,b,epsilon):
    left=f(a)
    right=f(b)
    m=(a+b)/2
    mid=f(m)
    if left==0:
        return a
    if right==0:
        return b
    if mid==0:
        return m

    if (left>0 and right<0) or (left<0 and right>0):
        if (a-b)**2<epsilon**2:
                return m
        if (left>0 and mid<0) or (left<0 and mid>0):
            return findRoot(f,a,m,epsilon)
        elif (right>0 and mid<0) or (right<0 and mid>0):  
            return findRoot(f,m,b,epsilon)
    else:
        print('No roots in interval')
