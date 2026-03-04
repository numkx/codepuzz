# Title: Permutations
# Difficulty: Medium
#
# Description:
# Compute the required array/list result for "permutations" and return it.
#
# Example: solve(5) -> 5.
# Example: solve(0) -> 0.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((5,), 5),
        ((0,), 0),
        ((-1,), -1),
        ((10,), 10),
        ((1,), 1),
        ((7,), 7),
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
