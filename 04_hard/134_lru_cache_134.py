# Title: Lru Cache
# Difficulty: Hard
#
# Description:
# Implement an LRU cache and return outputs for the required cache operations.
#
# Example: solve((2, [['put', 1, 1], ['put', 2, 2], ['get', 1], ['put', 3, 3], ['get', 2], ['put', 4, 4], ['get', 1], ['get', 3], ['get', 4]])) -> [None, None, 1, None, -1, None, -1, 3, 4].
# Example: solve((1, [['put', 1, 1], ['put', 2, 2], ['get', 1], ['get', 2]])) -> [None, None, -1, 2].
#
# Tags: [tuple]
#

def solve(t):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (((2, [['put', 1, 1], ['put', 2, 2], ['get', 1], ['put', 3, 3], ['get', 2], ['put', 4, 4], ['get', 1], ['get', 3], ['get', 4]]),), [None, None, 1, None, -1, None, -1, 3, 4]),
        (((1, [['put', 1, 1], ['put', 2, 2], ['get', 1], ['get', 2]]),), [None, None, -1, 2]),
        (((2, [['put', 2, 1], ['put', 2, 2], ['get', 2]]),), [None, None, 2]),
        (((1, [['put', 2, 1], ['get', 2], ['put', 3, 2], ['get', 2], ['get', 3]]),), [None, 1, None, -1, 2]),
        (((2, []),), []),
        (((2, [['get', 1]]),), [-1]),
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
