# Title: Capitalize First Letter Of A String
# Difficulty: Very Easy
#
# Description:
# Given a string, capitalize its first character and return the updated string.
#
# Example: solve('hello') -> 'Hello'.
# Example: solve('') -> ''.
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('hello',), 'Hello'),
        (('',), ''),
        (('h',), 'H'),
        (('Hello',), 'Hello'),
        (('123abc',), '123abc'),
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
