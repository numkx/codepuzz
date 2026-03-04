# Title: Print All Indices Of A Character In String
# Difficulty: Very Easy
#
# Description:
# Return all indices of a character in string.
#

def solve(s1, s2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('banana', 'a'), [1, 3, 5]),
        (('abc', 'd'), []),
        (('', 'a'), []),
        (('aaa', 'a'), [0, 1, 2]),
        (('test', 't'), [0, 3]),
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
