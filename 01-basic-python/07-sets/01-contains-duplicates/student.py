# Write your code here
def contains_duplicates(aList):
    seen = set()

    for item in aList:
        if item in seen:
            return True
        seen.add(item)
    return False