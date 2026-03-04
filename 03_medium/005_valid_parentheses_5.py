# Title: Valid Parentheses
# Difficulty: Medium
#
# Description:
# Return True if valid parentheses, otherwise return False.
#
# Example: solve('()') -> True.
# Example: solve('()[]{}') -> True.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('()',), True),
        (('()[]{}',), True),
        (('(]',), False),
        (('([)]',), False),
        (('{[]}',), True),
        (('',), True),
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
