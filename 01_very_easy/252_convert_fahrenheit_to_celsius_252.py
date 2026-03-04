# Title: Convert Fahrenheit To Celsius
# Difficulty: Very Easy
#
# Description:
# Convert fahrenheit to celsius and return the converted value.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((32,), 0.0),
        ((212,), 100.0),
        ((-40,), -40.0),
        ((98.6,), 37.0),
        ((50,), 10.0),
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
