# Title: Print Numbers From N To 1
# Difficulty: Very Easy
#
# Description:
# Return numbers from n to 1.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), [1]),
        ((3,), [3, 2, 1]),
        ((0,), []),
        ((5,), [5, 4, 3, 2, 1]),
        ((2,), [2, 1]),
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
