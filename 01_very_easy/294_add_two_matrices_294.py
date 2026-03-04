# Title: Add Two Matrices
# Difficulty: Very Easy
#
# Description:
# Add two matrices and return the result.
#
# Example: solve([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[6, 8], [10, 12]].
# Example: solve([[0]], [[0]]) -> [[0]].
#

def solve(lst1, lst2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]]),
        (([[0]], [[0]]), [[0]]),
        (([[1]], [[2]]), [[3]]),
        (([[1, 1]], [[2, 2]]), [[3, 3]]),
        (([[1], [2]], [[3], [4]]), [[4], [6]]),
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
