# Title: Check Divisibility By 3
# Difficulty: Very Easy
#
# Description:
# Return True when divisibility by 3, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(3) -> True.
# Example: solve(4) -> False.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((3,), True),
        ((4,), False),
        ((0,), True),
        ((-6,), True),
        ((10,), False),
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
