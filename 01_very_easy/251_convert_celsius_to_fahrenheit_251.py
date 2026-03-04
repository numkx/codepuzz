# Title: Convert Celsius To Fahrenheit
# Difficulty: Very Easy
#
# Description:
# Convert celsius to fahrenheit and return the converted result.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve(0) -> 32.0.
# Example: solve(100) -> 212.0.
#
# Tags: [integer]
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((0,), 32.0),
        ((100,), 212.0),
        ((-40,), -40.0),
        ((37,), 98.6),
        ((10,), 50.0),
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
