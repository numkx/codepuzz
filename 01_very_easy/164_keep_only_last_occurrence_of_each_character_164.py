# Title: Keep Only Last Occurrence Of Each Character
# Difficulty: Very Easy
#
# Description:
# Keep only last occurrence of each character and return the result.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('banana',), 'bna'),
        (('',), ''),
        (('aaaa',), 'a'),
        (('abc',), 'abc'),
        (('aabbcc',), 'abc'),
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
