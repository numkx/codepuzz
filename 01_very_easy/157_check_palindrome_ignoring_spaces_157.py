# Title: Check Palindrome Ignoring Spaces
# Difficulty: Very Easy
#
# Description:
# Solve check palindrome ignoring spaces and return the result.
#
# Example: solve('n u r s e s r u n') -> True.
# Example: solve('never odd or even') -> True.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('n u r s e s r u n',), True),
        (('never odd or even',), True),
        (('hello world',), False),
        (('a',), True),
        (('',), True),
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
