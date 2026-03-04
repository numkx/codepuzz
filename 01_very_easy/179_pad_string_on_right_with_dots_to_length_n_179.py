# Title: Pad String On Right With Dots To Length N
# Difficulty: Very Easy
#
# Description:
# Given string input, return the result for pad string on right with dots to length n.
#
# Example: solve('42', 5) -> '42...'.
# Example: solve('123', 3) -> '123'.
#

def solve(s, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('42', 5), '42...'),
        (('123', 3), '123'),
        (('', 2), '..'),
        (('a', 1), 'a'),
        (('7', 4), '7...'),
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
