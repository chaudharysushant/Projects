
dups = [1,1,2,3,4,4,4,5,6,6,7,7,8]

def deduplicate(dups):
    seen = set()
    result=[]
    for item in dups:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(deduplicate(dups))