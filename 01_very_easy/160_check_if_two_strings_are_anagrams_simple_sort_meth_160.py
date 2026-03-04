# Title: Check If Two Strings Are Anagrams (simple Sort Method)
# Difficulty: Very Easy
#
# Description:
# Return True if two strings are anagrams, otherwise return False.
#
# Example: solve('listen', 'silent') -> True.
# Example: solve('triangle', 'integral') -> True.
#

def solve(s1, s2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('listen', 'silent'), True),
        (('triangle', 'integral'), True),
        (('rat', 'car'), False),
        (('a', 'a'), True),
        (('ab', 'a'), False),
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
