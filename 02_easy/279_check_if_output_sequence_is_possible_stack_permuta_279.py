# Title: Check If Output Sequence Is Possible Stack Permutation
# Difficulty: Easy
#
# Description:
# Return True if output sequence is possible stack permutation, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([1, 2, 3], [3, 1, 2]) -> False.
# Example: solve(([['push', 2], ['push', 3], ['top']],)) -> [None, None, 3].
#
# Tags: [stack] [list]
#

def solve(inp, out):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3], [2, 1, 3]), True),
        (([1, 2, 3], [3, 1, 2]), False),
        (([1, 2, 3, 4], [2, 1, 4, 3]), True),
        (([1], [1]), True),
        (([1, 2, 3], [1, 3, 2]), True),
        (([1, 2, 3], [3, 2, 1]), True),
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
