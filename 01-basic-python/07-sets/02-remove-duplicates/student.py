import copy

def remove_duplicates(xs):
    seen = set()
    result = []

    for item in xs:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result