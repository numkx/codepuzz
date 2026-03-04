# Title: Find Smallest Element Index
# Difficulty: Very Easy
#
# Description:
# Return smallest element index.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([3, 1, 2],), 1),
        (([5],), 0),
        (([-1, -5],), 1),
        (([0, 0],), 0),
        (([2, 9, 4],), 0),
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
