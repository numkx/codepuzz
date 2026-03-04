# Title: Keep Only Numeric Characters
# Difficulty: Very Easy
#
# Description:
# Return keep only numeric characters.
#
# Example: solve('a1b2!') -> '12'.
# Example: solve('') -> ''.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a1b2!',), '12'),
        (('',), ''),
        (('ABC',), ''),
        (('123',), '123'),
        (('a b',), ''),
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
