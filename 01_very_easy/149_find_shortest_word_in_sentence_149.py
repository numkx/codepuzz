# Title: Find Shortest Word In Sentence
# Difficulty: Very Easy
#
# Description:
# Return shortest word in sentence.
#
# Example: solve('a bb ccc') -> 'a'.
# Example: solve('') -> ''.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a bb ccc',), 'a'),
        (('',), ''),
        (('one',), 'one'),
        (('hi there friend',), 'hi'),
        (('to be or not',), 'to'),
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
