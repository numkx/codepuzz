# Title: Find Common Characters Between Two Strings
# Difficulty: Very Easy
#
# Description:
# Return common characters between two strings.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('abc', 'bcd') -> 'bc'.
# Example: solve('abc', 'xyz') -> ''.
#
# Tags: [string]
#

def solve(s1, s2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc', 'bcd'), 'bc'),
        (('abc', 'xyz'), ''),
        (('', 'abc'), ''),
        (('aabb', 'ab'), 'ab'),
        (('hello', 'yellow'), 'ello'),
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
