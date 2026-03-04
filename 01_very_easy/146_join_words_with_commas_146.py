# Title: Join Words With Commas
# Difficulty: Very Easy
#
# Description:
# Return a list/string result for the given input.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((['a', 'b', 'c'],), 'a,b,c'),
        (([],), ''),
        ((['one'],), 'one'),
        ((['hi', 'there'],), 'hi,there'),
        ((['x', 'y'],), 'x,y'),
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
