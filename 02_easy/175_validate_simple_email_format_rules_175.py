# Title: Validate Simple Email Format Rules
# Difficulty: Easy
#
# Description:
# Given a string, return True if it matches the simplified email rules, otherwise return False.
#
# Constraints:
# Handle empty inputs, single-element inputs, and boundary values when applicable.
#
# Example: solve('@domain.com') -> False.
# Example: solve(0) -> 0.
#
# Tags: [string]
#

def solve(s):
    """Implement the solution here."""
    raise NotImplementedError


# Tests
if __name__ == "__main__":
    tests = [
        (('a@b.com',), True),
        (('@domain.com',), False),
        (('user@domain',), False),
        (('user@@domain.com',), False),
        (('user_name@site.org',), True),
        (('name.surname@mail.co',), True),
        (('',), False),
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
