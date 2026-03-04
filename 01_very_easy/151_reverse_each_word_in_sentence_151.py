# Title: Reverse Each Word In Sentence
# Difficulty: Very Easy
#
# Description:
# Reverse each word in sentence and return the result.
#
# Example: solve('hello') -> 'olleh'.
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
        (('hello',), 'olleh'),
        (('',), ''),
        (('a',), 'a'),
        (('ab',), 'ba'),
        (('racecar',), 'racecar'),
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
