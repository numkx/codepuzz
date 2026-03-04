# Title: Find The Index Of The First Occurrence In A String
# Difficulty: Medium
#
# Description:
# Return the index of the first occurrence in a string.
#
# Example: solve('sadbutsad', 'sad') -> 0.
# Example: solve('leetcode', 'leeto') -> -1.
#

def solve(s1, s2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('sadbutsad', 'sad'), 0),
        (('leetcode', 'leeto'), -1),
        (('a', 'a'), 0),
        (('aaa', 'aa'), 0),
        (('', 'a'), -1),
        (('abc', ''), 0),
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
