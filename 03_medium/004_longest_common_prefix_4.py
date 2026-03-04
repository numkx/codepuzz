# Title: Longest Common Prefix
# Difficulty: Medium
#
# Description:
# Return the longest common prefix.
#
# Example: solve(['flower', 'flow', 'flight']) -> 'fl'.
# Example: solve(['dog', 'racecar', 'car']) -> ''.
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((['flower', 'flow', 'flight'],), 'fl'),
        ((['dog', 'racecar', 'car'],), ''),
        ((['a'],), 'a'),
        (([],), ''),
        ((['ab', 'a'],), 'a'),
        ((['', ''],), ''),
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
