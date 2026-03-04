# Title: Length Of Last Word
# Difficulty: Medium
#
# Description:
# Return the result after applying the required operation to the input.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('Hello World',), 5),
        (('   fly me   to   the moon  ',), 4),
        (('luffy is still joyboy',), 6),
        (('a',), 1),
        (('',), 0),
        (('endspace ',), 8),
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
