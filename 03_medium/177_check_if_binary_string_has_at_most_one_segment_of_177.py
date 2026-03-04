# Title: Check If Binary String Has At Most One Segment Of Ones
# Difficulty: Medium
#
# Description:
# Return True if binary (base-2 representation using 0 and 1) string has at most one segment of ones, otherwise return False.
#
# Example: solve('abba') -> True.
# Example: solve('abc') -> False.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abba',), True),
        (('abc',), False),
        (('',), True),
        (('a',), True),
        (('ab',), False),
        (('racecar',), True),
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
