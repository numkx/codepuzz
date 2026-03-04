# Title: Find First Repeating Character
# Difficulty: Very Easy
#
# Description:
# Return first repeating character.
#
# Example: solve('swiss') -> 's'.
# Example: solve('abc') -> None.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('swiss',), 's'),
        (('abc',), None),
        (('',), None),
        (('aabc',), 'a'),
        (('abca',), 'a'),
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
