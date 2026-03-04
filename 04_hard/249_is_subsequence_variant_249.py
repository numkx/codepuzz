# Title: Is Subsequence Variant
# Difficulty: Hard
#
# Description:
# Given strings s and t, return True if s is a subsequence (keep order; items do not need to be adjacent) of t, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('axc', 'ahbgdc') -> False.
# Example: solve(0) -> 0.
#
# Tags: [string] [two pointers]
#

def solve(s, t):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc', 'ahbgdc'), True),
        (('axc', 'ahbgdc'), False),
        (('', 'ahbgdc'), True),
        (('ace', 'abcde'), True),
        (('aec', 'abcde'), False),
        (('abc', 'abc'), True),
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
