def audit_blocklists(list_a, list_b, list_c):
    A = set(list_a)
    B = set(list_b)
    C = set(list_c)

    Universal = A & B & C
    Redundant = (A & B) | (B & C) | (A & C)
    Unique_A_Only = A - B - C

    return Universal, Redundant, Unique_A_Only
    