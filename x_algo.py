def solve(X, Y, total, types, numbers, solution=[]):
    if not X or total == len(solution):
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]) if (len(X[c]) > 0) else len(types))
        for r in list(X[c]):
            numbers[types[r]] -= 1
            solution.append(r)
            cols = select(X, Y, r)
            available = set()
            for i in X.values():
                available = available | i
            rows = []
            if numbers[types[r]] == 0:
                for p in types:
                    if types[p] == types[r] and p in available:
                        rows.append(select_rows(X, Y, p))
                        available.remove(p)
            for s in solve(X, Y, total, types, numbers, solution):
                yield s
            deselect_rows(X, Y, rows)
            deselect(X, Y, r, cols)
            solution.pop()
            numbers[types[r]] += 1


def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols


def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)


def select_rows(X, Y, p):
    row = p
    for j in Y[p]:
        X[j].remove(p)
    return row


def deselect_rows(X, Y, rows):
    for p in rows:
        for i in Y[p]:
            X[i].add(p)
