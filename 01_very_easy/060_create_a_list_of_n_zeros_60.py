# Title: Create A List Of N Zeros
# Difficulty: Very Easy
#
# Description:
# Create a list of n zeros and return the result.
#
# Example: solve(5) -> [0, 0, 0, 0, 0].
# Example: solve(1) -> [0].
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((5,), [0, 0, 0, 0, 0]),
        ((1,), [0]),
        ((0,), []),
        ((3,), [0, 0, 0]),
        ((2,), [0, 0]),
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
