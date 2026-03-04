# Title: Count The Number Of Consistent Strings
# Difficulty: Medium
#
# Description:
# Return the count of the number of consistent strings.
#
# Example: solve('abc') -> 3.
# Example: solve('') -> 0.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc',), 3),
        (('',), 0),
        (('a',), 1),
        (('hello',), 5),
        (('a1b2',), 4),
        (('Hi There',), 8),
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
