# Title: Check If String Is All Letters
# Difficulty: Very Easy
#
# Description:
# Return True if string is all letters, otherwise return False.
#
# Example: solve('abba') -> True.
# Example: solve('abc') -> False.
#
# Tags: [string]
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
