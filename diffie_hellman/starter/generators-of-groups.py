p = 28151


def is_primitive(g, p):
    # g is primitive if its order is p-1
    for n in range(2, p):
        if pow(g, n, p) == g:
            # reject if g generates a cycle of order n < p-1
            return False
    return True


for g in range(1, p):
    if is_primitive(g, p):
        print(f"{g=}")
        break
