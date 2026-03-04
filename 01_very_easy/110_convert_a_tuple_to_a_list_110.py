# Title: Convert A Tuple To A List
# Difficulty: Very Easy
#
# Description:
# Convert a tuple to a list and return the converted result.
#
# Example: solve((1, 2, 3)) -> [1, 2, 3].
# Example: solve(()) -> [].
#
# Tags: [list] [tuple]
#

def solve(t):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (((1, 2, 3),), [1, 2, 3]),
        (((),), []),
        (((5,),), [5]),
        ((('a', 'b'),), ['a', 'b']),
        (((0, 0),), [0, 0]),
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
