# Title: Find Longest Substring With At Most Two Distinct Characters
# Difficulty: Easy
#
# Description:
# Given a string, return the required longest-substring value described by the problem constraints.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('hello') -> 'hello'.
# Example: solve('') -> ''.
#
# Tags: [binary tree] [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('hello',), 'hello'),
        (('',), ''),
        (('a',), 'a'),
        (('abc123',), 'abc123'),
        (('Hi There',), 'Hi There'),
        (('x',), 'x'),
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
