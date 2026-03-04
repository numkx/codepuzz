# Title: Palindrome Linked List Variant
# Difficulty: Hard
#
# Description:
# Given linked-list values, return True if they form a palindrome, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve([1, 2]) -> False.
# Example: solve('') -> ''.
#
# Tags: [linked list]
#

def solve(lst):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (([1, 2, 2, 1],), True),
        (([1, 2],), False),
        (([1],), True),
        (([],), True),
        (([1, 2, 3, 2, 1],), True),
        (([1, 2, 3],), False),
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
