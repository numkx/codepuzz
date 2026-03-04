# Title: Calculate Total Marks From 5 Subjects
# Difficulty: Very Easy
#
# Description:
# Calculate total marks from 5 subjects and return the result.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([10, 20, 30, 40, 50],), 150),
        (([0, 0, 0, 0, 0],), 0),
        (([100, 100, 100, 100, 100],), 500),
        (([50, 50, 50, 50, 50],), 250),
        (([1, 2, 3, 4, 5],), 15),
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
