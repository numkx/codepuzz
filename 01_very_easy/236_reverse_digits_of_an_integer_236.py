# Title: Reverse Digits Of An Integer
# Difficulty: Very Easy
#
# Description:
# Reverse digits of an integer and return the result.
#
# Example: solve(123) -> 321.
# Example: solve(-123) -> -321.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((123,), 321),
        ((-123,), -321),
        ((0,), 0),
        ((120,), 21),
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
