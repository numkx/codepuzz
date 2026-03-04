# Title: Create List Of First N Odd Numbers
# Difficulty: Very Easy
#
# Description:
# Create list of first n odd numbers and return it.
#
# Example: solve(5) -> [1, 3, 5, 7, 9].
# Example: solve(1) -> [1].
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((5,), [1, 3, 5, 7, 9]),
        ((1,), [1]),
        ((0,), []),
        ((3,), [1, 3, 5]),
        ((2,), [1, 3]),
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
