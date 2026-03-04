# Title: Generate Multiplication Table Of N (1 To 10)
# Difficulty: Very Easy
#
# Description:
# Generate multiplication table of n and return it.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2,), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),
        ((1,), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ((0,), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ((3,), [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]),
        ((5,), [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),
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
