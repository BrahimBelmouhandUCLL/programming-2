# Write your code here
def drop_nth(xs, n):
    ys = xs[:n]
    zs = xs[n+1:]
    ys += zs
    return ys
#print(drop_nth([1,2,3,4,5], 3))