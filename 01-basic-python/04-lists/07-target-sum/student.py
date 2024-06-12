# Write your code here
def target_sum(ns, target):
    for firstValue in range(len(ns)):
        for secondValue in range(len(ns)):
            if(ns[firstValue] + ns[secondValue] == target):
                return True
    return False