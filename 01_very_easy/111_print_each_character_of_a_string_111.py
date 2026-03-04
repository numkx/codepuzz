# Title: Print Each Character Of A String
# Difficulty: Very Easy
#
# Description:
# Return each character of a string.
#
# Example: solve('abc') -> ['a', 'b', 'c'].
# Example: solve('') -> [].
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc',), ['a', 'b', 'c']),
        (('',), []),
        (('a',), ['a']),
        (('Hi',), ['H', 'i']),
        (('12',), ['1', '2']),
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
