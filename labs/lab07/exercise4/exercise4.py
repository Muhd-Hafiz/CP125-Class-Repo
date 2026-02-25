def apply_upgrade(current, upgrade):
    # TODO: Your code here
        result = {}
        for key in current:
            if key in upgrade:
                result[key] = max(current[key], upgrade[key])
            else:
                result[key] = current[key]
        for key in upgrade:
            if key not in current:
                result[key] = upgrade[key]
        return result

current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   # Should be unchanged
