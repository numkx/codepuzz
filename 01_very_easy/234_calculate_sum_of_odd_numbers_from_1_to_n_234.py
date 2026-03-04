# Title: Calculate Sum Of Odd Numbers From 1 To N
# Difficulty: Very Easy
#
# Description:
# Calculate sum of odd numbers from 1 to n and return the result.
#
# Example: solve(1) -> 1.
# Example: solve(2) -> 1.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), 1),
        ((2,), 1),
        ((5,), 9),
        ((10,), 25),
        ((0,), 0),
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
