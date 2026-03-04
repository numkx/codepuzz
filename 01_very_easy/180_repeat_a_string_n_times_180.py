# Title: Repeat A String N Times
# Difficulty: Very Easy
#
# Description:
# Repeat a string n times and return the result.
#

def solve(s, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('ab', 3), 'ababab'),
        (('x', 1), 'x'),
        (('', 5), ''),
        (('a', 0), ''),
        (('hi', 2), 'hihi'),
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
