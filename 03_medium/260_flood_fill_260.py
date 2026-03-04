# Title: Flood Fill
# Difficulty: Medium
#
# Description:
# Given the provided input, apply the required algorithm for this problem.
# Return the computed result.
#

def solve(lst, n1, n2, n3):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        (([[0, 0, 0], [0, 0, 0]], 0, 0, 0), [[0, 0, 0], [0, 0, 0]]),
        (([[0]], 0, 0, 2), [[2]]),
        (([[1]], 0, 0, 1), [[1]]),
        (([[1, 1], [1, 1]], 1, 0, 9), [[9, 9], [9, 9]]),
        (([[1, 0, 1]], 0, 0, 3), [[3, 0, 1]]),
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
