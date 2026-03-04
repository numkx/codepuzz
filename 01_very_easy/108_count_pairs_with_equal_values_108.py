# Title: Count Pairs With Equal Values
# Difficulty: Very Easy
#
# Description:
# Return the count of pairs with equal values.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 1, 2, 2, 2],), 4),
        (([],), 0),
        (([1],), 0),
        (([1, 2, 3],), 0),
        (([5, 5],), 1),
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
