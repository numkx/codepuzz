# Title: Maximum Nesting Depth Of The Parentheses
# Difficulty: Medium
#
# Description:
# Return the result after applying the required operation to the input.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('hello',), 'hello'),
        (('',), ''),
        (('a',), 'a'),
        (('abc123',), 'abc123'),
        (('Hi There',), 'Hi There'),
        (('x',), 'x'),
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
