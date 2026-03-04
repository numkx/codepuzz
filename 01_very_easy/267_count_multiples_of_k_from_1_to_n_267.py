# Title: Count Multiples Of K From 1 To N
# Difficulty: Very Easy
#
# Description:
# Return the count of multiples of k from 1 to n.
#

def solve(n1, n2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((10, 2), 5),
        ((10, 3), 3),
        ((5, 7), 0),
        ((0, 2), 0),
        ((12, 4), 3),
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
