# Write your code here
def median(ns):
    ns.sort()
    n = len(ns)
    if(n % 2 == 0):
        median = (ns[(n//2)-1] + ns[n//2])/2 
    else:
        median = ns[n//2] 
    return median