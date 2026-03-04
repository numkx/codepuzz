# Title: Count Even Digits In An Integer
# Difficulty: Very Easy
#
# Description:
# Return the count of even digits in an integer.
#
# Example: solve(1234) -> 2.
# Example: solve(0) -> 1.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1234,), 2),
        ((0,), 1),
        ((999,), 0),
        ((2468,), 4),
        ((-1203,), 2),
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
