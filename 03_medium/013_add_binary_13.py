# Title: Add Binary
# Difficulty: Medium
#
# Description:
# Given the provided input, add binary.
# Return the computed result.
#

def solve(s1, s2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('11', '1'), '100'),
        (('1010', '1011'), '10101'),
        (('0', '0'), '0'),
        (('1', '0'), '1'),
        (('111', '1'), '1000'),
        (('10', '10'), '100'),
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
