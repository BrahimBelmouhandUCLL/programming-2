# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    for x,y in zip(ns, ms):
        if x > y:
            return False
    return True