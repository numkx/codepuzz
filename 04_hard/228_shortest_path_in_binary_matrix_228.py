# Title: Shortest Path In Binary Matrix
# Difficulty: Hard
#
# Description:
# Given a binary matrix, return the length of the shortest clear path from top-left to bottom-right, or -1 if none exists.
#
# Example: solve([[1, 2], [3, 4]]) -> [[1, 2], [3, 4]].
# Example: solve([[0]]) -> [[0]].
#
# Tags: [matrix] [list] [array]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([[1, 2], [3, 4]],), [[1, 2], [3, 4]]),
        (([[0]],), [[0]]),
        (([[]],), [[]]),
        (([[1]],), [[1]]),
        (([[1, -1]],), [[1, -1]]),
        (([[5, 6]],), [[5, 6]]),
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
