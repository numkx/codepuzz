# Title: Roman To Integer
# Difficulty: Hard
#
# Description:
# Convert the Roman numeral string to its integer value.
#
# Example: solve('III') -> 3.
# Example: solve('LVIII') -> 58.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('III',), 3),
        (('LVIII',), 58),
        (('MCMXCIV',), 1994),
        (('IV',), 4),
        (('IX',), 9),
        (('XL',), 40),
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
