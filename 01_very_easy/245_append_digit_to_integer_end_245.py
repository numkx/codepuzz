# Title: Append Digit To Integer End
# Difficulty: Very Easy
#
# Description:
# Append digit to integer end and return the result.
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((12, 3), 123),
        ((0, 5), 5),
        ((7, 0), 70),
        ((-12, 3), -123),
        ((9, 9), 99),
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
