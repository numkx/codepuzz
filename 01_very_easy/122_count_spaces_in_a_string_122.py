# Title: Count Spaces In A String
# Difficulty: Very Easy
#
# Description:
# Return the count of spaces in a string.
#
# Example: solve('abc') -> 3.
# Example: solve('') -> 0.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc',), 3),
        (('',), 0),
        (('a a',), 3),
        (('123',), 3),
        (('Hello',), 5),
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
