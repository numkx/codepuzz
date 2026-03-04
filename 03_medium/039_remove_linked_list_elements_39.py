# Title: Remove Linked List Elements
# Difficulty: Medium
#
# Description:
# Given a linked list and any required parameters, remove linked list elements.
# Return the resulting list/collection.
#

def solve(t):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        ((([['push', 1], ['pop'], ['empty']],),), [None, 1, True]),
        ((([['push', 2], ['push', 3], ['top']],),), [None, None, 3]),
        ((([['put', 1, 1], ['get', 1]],),), [None, 1]),
        ((([['enqueue', 1], ['dequeue']],),), [None, 1]),
        ((([['insert', 1], ['search', 1]],),), [None, True]),
        ((([],),), []),
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
