# Title: Replace Tabs With Spaces
# Difficulty: Very Easy
#
# Description:
# Replace tabs with spaces and return the result.
#
# Example: solve('a\tb') -> 'a b'.
# Example: solve('\t') -> ' '.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a\\tb',), 'a b'),
        (('\\t',), ' '),
        (('no tab',), 'no tab'),
        (('a\\t\\tb',), 'a  b'),
        (('',), ''),
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
