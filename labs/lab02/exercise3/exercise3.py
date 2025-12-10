def validate_entry(name, pin):
    # TODO: Implement this function
    # Return True if valid, False otherwise
    if name == "Director" and pin == 1122:
        return True
    elif name == "Security" and pin == 9900:
        return True
    else:
        return False
# Test your code here
print("Testing Secure Vault System...")
