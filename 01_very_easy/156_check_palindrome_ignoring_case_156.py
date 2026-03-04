# Title: Check Palindrome Ignoring Case
# Difficulty: Very Easy
#
# Description:
# Given a string, return True if it is a palindrome ignoring case, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('RaceCar') -> True.
# Example: solve('Hello') -> False.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('RaceCar',), True),
        (('Hello',), False),
        (('A',), True),
        (('',), True),
        (('AbBa',), True),
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
