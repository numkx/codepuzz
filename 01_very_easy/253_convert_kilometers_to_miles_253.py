# Title: Convert Kilometers To Miles
# Difficulty: Very Easy
#
# Description:
# Convert kilometers to miles and return the result.
#
# Example: solve(1) -> 0.621371.
# Example: solve(0) -> 0.0.
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), 0.621371),
        ((0,), 0.0),
        ((5,), 3.106855),
        ((10,), 6.21371),
        ((2.5,), 1.5534275),
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
