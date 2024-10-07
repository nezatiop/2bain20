def merge(S, T):
    allstock = S.copy()
    for item in T:
        if item in allstock:
            allstock[item]['quantity'] += T[item]['quantity']
        else:
            allstock[item] = T[item]
            
    return allstock
