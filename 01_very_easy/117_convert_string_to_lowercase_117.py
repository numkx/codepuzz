# Title: Convert String To Lowercase
# Difficulty: Very Easy
#
# Description:
# Convert string to lowercase and return the converted result.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('HELLO') -> 'hello'.
# Example: solve('AbC') -> 'abc'.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('HELLO',), 'hello'),
        (('AbC',), 'abc'),
        (('',), ''),
        (('123',), '123'),
        (('Hi There',), 'hi there'),
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
