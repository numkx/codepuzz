# Title: Keep Only Alphanumeric Characters
# Difficulty: Very Easy
#
# Description:
# Keep only alphanumeric characters and return the result.
#
# Example: solve('a1b2!') -> 'a1b2'.
# Example: solve('') -> ''.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a1b2!',), 'a1b2'),
        (('',), ''),
        (('ABC',), 'ABC'),
        (('123',), '123'),
        (('a b',), 'ab'),
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
