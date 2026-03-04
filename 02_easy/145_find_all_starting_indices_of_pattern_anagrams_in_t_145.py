# Title: Find All Starting Indices Of Pattern Anagrams In Text
# Difficulty: Easy
#
# Description:
# Given a string (or strings) and any required parameters, find all starting indices of pattern anagrams in text.
# Return True when the condition holds; otherwise return False.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abba',), True),
        (('abc',), False),
        (('',), True),
        (('a',), True),
        (('ab',), False),
        (('racecar',), True),
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
