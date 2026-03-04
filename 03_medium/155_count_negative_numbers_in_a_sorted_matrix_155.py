# Title: Count Negative Numbers In A Sorted Matrix
# Difficulty: Medium
#
# Description:
# Return the count of negative numbers in a sorted matrix.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([[1, 2], [3, 4]]) -> 10.
# Example: solve([[0]]) -> 0.
#
# Tags: [matrix] [sorting] [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 2], [3, 4]],), 10),
        (([[0]],), 0),
        (([[]],), 0),
        (([[5]],), 5),
        (([[1, -1]],), 0),
        (([[1, 1], [1, 1]],), 4),
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
