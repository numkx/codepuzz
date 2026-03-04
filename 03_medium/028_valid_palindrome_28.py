# Title: Valid Palindrome
# Difficulty: Medium
#
# Description:
# Perform the required string operation for "valid palindrome" and return the result.
#
# Example: solve('A man, a plan, a canal: Panama') -> True.
# Example: solve('race a car') -> False.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('A man, a plan, a canal: Panama',), True),
        (('race a car',), False),
        ((' ',), True),
        (('',), True),
        (('0P',), False),
        (('abba',), True),
    ]
    passed = 0
    for args, expected in tests:
        if not isinstance(args, tuple):
            args = (args,)
        try:
            result = solve(*args)
            ok = result == expected
        except Exception as e:
            result = f"<error: {type(e).__name__}>"
            ok = False
        status = "passed" if ok else "failed"
        print(f"solve{args} == {expected} -> {result} ({status})")
        if ok:
            passed += 1
    print(f"{passed}/{len(tests)} tests passed")
