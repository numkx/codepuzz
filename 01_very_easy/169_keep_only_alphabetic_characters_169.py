# Title: Keep Only Alphabetic Characters
# Difficulty: Very Easy
#
# Description:
# Return keep only alphabetic characters.
#
# Example: solve('a1b2!') -> 'ab'.
# Example: solve('') -> ''.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a1b2!',), 'ab'),
        (('',), ''),
        (('ABC',), 'ABC'),
        (('123',), ''),
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
