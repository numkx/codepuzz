# Title: Validate Simple Arithmetic Expression With +,-,*,/ And Spaces
# Difficulty: Easy
#
# Description:
# Given an expression string with numbers, +, -, *, /, and spaces, return True if the token/order format is valid, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('3 + * 4') -> False.
# Example: solve(0) -> 0.
#
# Tags: [string] [stack]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('1 + 2 * 3',), True),
        (('3 + * 4',), False),
        (('10/2-3',), True),
        (('',), False),
        (('42',), True),
        (('7 / 0',), True),
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
