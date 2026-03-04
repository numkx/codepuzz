# Title: Convert Decimal To Hexadecimal String
# Difficulty: Very Easy
#
# Description:
# Convert decimal to hexadecimal string and return the converted value.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('AbC',), 'abc'),
        (('HELLO',), 'hello'),
        (('',), ''),
        (('123',), '123'),
        (('Hi',), 'hi'),
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
