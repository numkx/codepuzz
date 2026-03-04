# Title: Keep Every Second Character
# Difficulty: Very Easy
#
# Description:
# Return keep every second character.
#
# Example: solve('abcdef') -> 'ace'.
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
        (('abcdef',), 'ace'),
        (('',), ''),
        (('a',), 'a'),
        (('ab',), 'a'),
        (('12345',), '135'),
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
