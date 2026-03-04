# Title: Swap Two Numbers Using Temp Variable
# Difficulty: Very Easy
#
# Description:
# Swap two numbers using temp variable and return the result.
#
# Example: solve(2, 3) -> (3, 2).
# Example: solve(-1, 1) -> (1, -1).
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2, 3), (3, 2)),
        ((-1, 1), (1, -1)),
        ((0, 0), (0, 0)),
        ((5, -2), (-2, 5)),
        ((9, 9), (9, 9)),
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
