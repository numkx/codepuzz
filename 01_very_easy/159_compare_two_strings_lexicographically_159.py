# Title: Compare Two Strings Lexicographically
# Difficulty: Very Easy
#
# Description:
# Perform the required string operation for "compare two strings lexicographically" and return the result.
#
# Example: solve('abc', 'abd') -> -1.
# Example: solve('abd', 'abc') -> 1.
#

def solve(s1, s2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc', 'abd'), -1),
        (('abd', 'abc'), 1),
        (('abc', 'abc'), 0),
        (('', 'a'), -1),
        (('a', ''), 1),
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
