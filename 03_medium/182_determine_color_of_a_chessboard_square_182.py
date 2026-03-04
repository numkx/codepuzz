# Title: Determine Color Of A Chessboard Square
# Difficulty: Medium
#
# Description:
# Given a chessboard coordinate, return True if the square color matches the required condition, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('a1', 'h3') -> False.
# Example: solve(0) -> 0.
#
# Tags: [math]
#

def solve(c1, c2):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a1', 'c3'), True),
        (('a1', 'h3'), False),
        (('c7', 'a2'), False),
        (('d4', 'f6'), True),
        (('h1', 'a8'), True),
        (('b2', 'c3'), True),
        (('', ''), False),
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
