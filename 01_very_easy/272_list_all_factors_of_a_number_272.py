# Title: List All Factors Of A Number
# Difficulty: Very Easy
#
# Description:
# Return the required output for the given input.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), [1]),
        ((6,), [1, 2, 3, 6]),
        ((10,), [1, 2, 5, 10]),
        ((13,), [1, 13]),
        ((12,), [1, 2, 3, 4, 6, 12]),
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
