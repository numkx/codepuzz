# Title: Expand Basic Char+count Text (e.g., A3b2)
# Difficulty: Very Easy
#
# Description:
# Return expand basic char+count text.
#
# Example: solve('a3b2') -> 'aaabb'.
# Example: solve('x1') -> 'x'.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a3b2',), 'aaabb'),
        (('x1',), 'x'),
        (('',), ''),
        (('a1b1',), 'ab'),
        (('z4',), 'zzzz'),
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
