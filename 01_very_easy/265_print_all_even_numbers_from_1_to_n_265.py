# Title: Print All Even Numbers From 1 To N
# Difficulty: Very Easy
#
# Description:
# Solve print all even numbers from 1 to n and return the result.
#
# Example: solve(1) -> [].
# Example: solve(2) -> [2].
#

def solve(n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((1,), []),
        ((2,), [2]),
        ((5,), [2, 4]),
        ((10,), [2, 4, 6, 8, 10]),
        ((0,), []),
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
