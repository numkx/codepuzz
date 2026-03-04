# Title: Rotate String Left By 1
# Difficulty: Very Easy
#
# Description:
# Rotate string left by 1 and return the result.
#
# Example: solve('abc') -> 'bca'.
# Example: solve('a') -> 'a'.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc',), 'bca'),
        (('a',), 'a'),
        (('',), ''),
        (('ab',), 'ba'),
        (('hello',), 'elloh'),
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
