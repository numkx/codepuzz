# Title: Print All Odd Numbers From 1 To N
# Difficulty: Very Easy
#
# Description:
# Return all odd numbers from 1 to n.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), [1]),
        ((2,), [1]),
        ((5,), [1, 3, 5]),
        ((10,), [1, 3, 5, 7, 9]),
        ((0,), []),
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
