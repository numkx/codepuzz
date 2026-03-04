# Title: Longest Palindromic Subsequence
# Difficulty: Hard
#
# Description:
# Given a string, return the length of the longest palindromic (reads the same forward and backward) subsequence (keep order; items do not need to be adjacent).
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(5) -> 5.
# Example: solve(0) -> 0.
#
# Tags: [string]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((5,), 5),
        ((0,), 0),
        ((-1,), -1),
        ((10,), 10),
        ((1,), 1),
        ((7,), 7),
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
