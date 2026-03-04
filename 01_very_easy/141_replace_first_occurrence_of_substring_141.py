# Title: Replace First Occurrence Of Substring
# Difficulty: Very Easy
#
# Description:
# Replace first occurrence of substring and return the result.
#
# Example: solve('a b') -> 'a_b'.
# Example: solve('') -> ''.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a b',), 'a_b'),
        (('',), ''),
        (('abc',), 'abc'),
        (('a  b',), 'a__b'),
        ((' x ',), '_x_'),
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
