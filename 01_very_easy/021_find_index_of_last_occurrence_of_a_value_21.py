# Title: Find Index Of Last Occurrence Of A Value
# Difficulty: Very Easy
#
# Description:
# Return index of last occurrence of a value.
#

def solve(lst, n):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 3, 2], 2), 3),
        (([5, 5, 5], 5), 2),
        (([1, 2, 3], 4), -1),
        (([], 1), -1),
        (([9], 9), 0),
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
