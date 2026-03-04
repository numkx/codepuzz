# Title: Integer Division Remainder
# Difficulty: Very Easy
#
# Description:
# Return integer division remainder.
#
# Example: solve(7, 3) -> 1.
# Example: solve(10, 2) -> 0.
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((7, 3), 1),
        ((10, 2), 0),
        ((5, 7), 5),
        ((0, 5), 0),
        ((9, 4), 1),
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
