# Title: Count Zeros In Matrix
# Difficulty: Very Easy
#
# Description:
# Return the count of zeros in matrix.
#
# Example: solve([[0, 1], [0, 0]]) -> 3.
# Example: solve([[1]]) -> 0.
#
# Tags: [matrix] [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[0, 1], [0, 0]],), 3),
        (([[1]],), 0),
        (([[]],), 0),
        (([[0]],), 1),
        (([[1, 1], [1, 1]],), 0),
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
