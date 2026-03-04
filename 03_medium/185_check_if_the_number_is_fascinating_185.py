# Title: Check If The Number Is Fascinating
# Difficulty: Medium
#
# Description:
# Return True if the number is fascinating, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(100) -> False.
# Example: solve(0) -> 0.
#
# Tags: [integer] [math]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((192,), True),
        ((100,), False),
        ((273,), True),
        ((783,), False),
        ((327,), True),
        ((219,), False),
        ((0,), False),
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
