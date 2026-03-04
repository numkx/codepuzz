# Title: Count Occurrences Of A Value In A List
# Difficulty: Very Easy
#
# Description:
# Return the count of occurrences of a value in a list.
#
# Example: solve([1, 2, 2, 3], 2) -> 2.
# Example: solve([5, 5, 5], 5) -> 3.
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 2, 3], 2), 2),
        (([5, 5, 5], 5), 3),
        (([1, 2, 3], 4), 0),
        (([], 1), 0),
        (([9], 9), 1),
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
