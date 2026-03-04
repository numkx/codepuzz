# Title: Word Pattern
# Difficulty: Medium
#
# Description:
# Given a pattern and a space-separated string, return True if they follow the same one-to-one (each item maps to one unique item) mapping, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('abba', 'dog cat cat fish') -> False.
# Example: solve('') -> ''.
#
# Tags: [string] [hash map]
#

def solve(pattern, s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abba', 'dog cat cat dog'), True),
        (('abba', 'dog cat cat fish'), False),
        (('aaaa', 'dog cat cat dog'), False),
        (('abba', 'dog dog dog dog'), False),
        (('abc', 'one two three'), True),
        (('ab', 'dog dog'), False),
        (('', ''), False),
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
