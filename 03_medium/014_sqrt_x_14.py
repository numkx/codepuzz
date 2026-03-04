# Title: Sqrt X
# Difficulty: Medium
#
# Description:
# Solve sqrt x and return the result.
#
# Example: solve(4) -> 2.
# Example: solve(8) -> 2.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((4,), 2),
        ((8,), 2),
        ((0,), 0),
        ((1,), 1),
        ((2147395599,), 46339),
        ((15,), 3),
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
