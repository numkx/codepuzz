# Title: Count Digits In A String
# Difficulty: Very Easy
#
# Description:
# Return the count of digits in a string.
#
# Example: solve('a1b2') -> 2.
# Example: solve('123') -> 3.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a1b2',), 2),
        (('123',), 3),
        (('abc',), 0),
        (('',), 0),
        (('a0z9',), 2),
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
