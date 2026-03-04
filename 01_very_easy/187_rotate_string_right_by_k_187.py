# Title: Rotate String Right By K
# Difficulty: Very Easy
#
# Description:
# Rotate string right by k and return the result.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('abc', 1) -> 'cab'.
# Example: solve('abc', 2) -> 'bca'.
#
# Tags: [string]
#

def solve(s, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('abc', 1), 'cab'),
        (('abc', 2), 'bca'),
        (('a', 5), 'a'),
        (('', 3), ''),
        (('hello', 2), 'lohel'),
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
