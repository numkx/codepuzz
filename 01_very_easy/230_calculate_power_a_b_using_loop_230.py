# Title: Calculate Power A^b Using Loop
# Difficulty: Very Easy
#
# Description:
# Calculate power a^b using loop and return the result.
#
# Example: solve(2, 3) -> 8.
# Example: solve(5, 0) -> 1.
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((2, 3), 8),
        ((5, 0), 1),
        ((3, 1), 3),
        ((1, 9), 1),
        ((10, 2), 100),
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
