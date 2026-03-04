# Title: Check If All Tasks Can Be Completed Given Prerequisites
# Difficulty: Easy
#
# Description:
# Return True if all tasks can be completed given prerequisites, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(2, [[1, 0], [0, 1]]) -> False.
# Example: solve(0) -> 0.
#
# Tags: [graph] [dfs]
#

def solve(n, prereqs):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2, [[1, 0]]), True),
        ((2, [[1, 0], [0, 1]]), False),
        ((4, [[1, 0], [2, 1], [3, 2]]), True),
        ((3, [[0, 1], [1, 2], [2, 0]]), False),
        ((5, []), True),
        ((1, [[0, 0]]), False),
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
