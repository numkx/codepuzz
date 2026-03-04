# Title: Convert Miles To Kilometers
# Difficulty: Very Easy
#
# Description:
# Convert miles to kilometers and return the converted result.
#
# Example: solve(1) -> 1.60934.
# Example: solve(0) -> 0.0.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), 1.60934),
        ((0,), 0.0),
        ((5,), 8.0467),
        ((10,), 16.0934),
        ((2.5,), 4.02335),
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
