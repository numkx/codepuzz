# Title: Minimum Window Substring
# Difficulty: Medium
#
# Description:
# Return the smallest substring of s that contains all characters of t.
#
# Example: solve('ADOBECODEBANC', 'ABC') -> 'BANC'.
# Example: solve('a', 'a') -> 'a'.
#

def solve(s1, s2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('ADOBECODEBANC', 'ABC'), 'BANC'),
        (('a', 'a'), 'a'),
        (('a', 'aa'), ''),
        (('ab', 'b'), 'b'),
        (('aa', 'aa'), 'aa'),
        (('xyz', 'a'), ''),
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
