# Title: Keep Only Vowels From A String
# Difficulty: Very Easy
#
# Description:
# Given string input, return the requested output for keep only vowels from a string.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('alphabet') -> 'aae'.
# Example: solve('xyz') -> ''.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('alphabet',), 'aae'),
        (('xyz',), ''),
        (('',), ''),
        (('AEIOU',), 'AEIOU'),
        (('hello',), 'eo'),
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
