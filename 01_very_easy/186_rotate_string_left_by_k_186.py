# Title: Rotate String Left By K
# Difficulty: Very Easy
#
# Description:
# Rotate string left by k and return the result.
#

def solve(s, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc', 1), 'bca'),
        (('abc', 2), 'cab'),
        (('a', 5), 'a'),
        (('', 3), ''),
        (('hello', 2), 'llohe'),
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
