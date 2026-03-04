# Title: Count Lines In Multiline Text
# Difficulty: Very Easy
#
# Description:
# Return the count of lines in multiline text.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('a\nb\nc') -> 3.
# Example: solve('') -> 0.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a\\nb\\nc',), 3),
        (('',), 0),
        (('one line',), 1),
        (('\\n',), 2),
        (('x\\n',), 2),
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
