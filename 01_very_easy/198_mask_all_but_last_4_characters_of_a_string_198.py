# Title: Mask All But Last 4 Characters Of A String
# Difficulty: Very Easy
#
# Description:
# Given string input, return the requested output for mask all but last 4 characters of a string.
#
# Example: solve('12345678') -> '****5678'.
# Example: solve('1234') -> '1234'.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('12345678',), '****5678'),
        (('1234',), '1234'),
        (('12',), '12'),
        (('',), ''),
        (('abcdef',), '**cdef'),
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
