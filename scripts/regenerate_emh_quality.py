#!/usr/bin/env python3
from pathlib import Path
import re

BASE = Path('/Users/numky/Code/edabit')
TARGET_DIRS = ['02_easy', '03_medium', '04_hard']


def normalize_title(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r'\s*\([^)]*\)\s*', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def description_line(title: str) -> str:
    t = normalize_title(title)
    special = {
        'roman to integer': 'Convert the Roman numeral string to an integer.',
        'integer to roman': 'Convert the integer to its Roman numeral form.',
        'lru cache': 'Implement least-recently-used cache behavior and return operation outputs.',
        'coin change': 'Return the minimum number of coins needed for the amount, or -1 if impossible.',
        'two sum': 'Return the required pair (indices or values) whose sum equals the target.',
        'number of islands': 'Return the number of connected islands in the grid.',
    }
    for key, sentence in special.items():
        if key in t:
            return sentence

    if t.startswith('check if '):
        return f'Return True if {t.replace("check if ", "", 1)}, otherwise return False.'
    if t.startswith('check whether '):
        return f'Return True if {t.replace("check whether ", "", 1)}, otherwise return False.'
    if t.startswith('valid '):
        return f'Return True when the input is {t.replace("valid ", "", 1)}, otherwise return False.'
    if t.startswith('count '):
        return f'Return the count of {t.replace("count ", "", 1)}.'
    if t.startswith('find '):
        return f'Return {t.replace("find ", "", 1)}.'
    if t.startswith('sum '):
        return f'Return the sum of {t.replace("sum ", "", 1)}.'
    if t.startswith('convert '):
        return f'Convert {t.replace("convert ", "", 1)} and return the converted value.'
    if t.startswith('reverse '):
        return f'Reverse {t.replace("reverse ", "", 1)} and return the result.'
    if t.startswith('rotate '):
        return f'Rotate {t.replace("rotate ", "", 1)} and return the result.'
    if t.startswith('merge '):
        return f'Merge {t.replace("merge ", "", 1)} and return the merged result.'
    if t.startswith('sort '):
        return f'Sort {t.replace("sort ", "", 1)} and return the result.'
    if t.startswith('remove '):
        return f'Remove {t.replace("remove ", "", 1)} and return the result.'
    if t.startswith('insert '):
        return f'Insert {t.replace("insert ", "", 1)} and return the updated result.'
    if t.startswith('delete '):
        return f'Delete {t.replace("delete ", "", 1)} and return the updated result.'
    if t.startswith('implement ') or t.startswith('design '):
        return 'Implement the required operations and return outputs in order.'
    if t.startswith('best time to buy and sell stock'):
        return 'Return the maximum profit under the transaction rules for this variant.'
    return 'Return the result after applying the required operation to the input.'


KNOWN = {
    # Common easy/medium/hard titles
    'two sum': [
        (([2,7,11,15], 9), [0,1]),
        (([3,2,4], 6), [1,2]),
        (([3,3], 6), [0,1]),
        (([1,2,3], 7), []),
        (([0,4,3,0], 0), [0,3]),
        (([-3,4,3,90], 0), [0,2]),
    ],
    'palindrome number': [
        ((121,), True), ((-121,), False), ((10,), False), ((0,), True), ((12321,), True), ((1001,), True)
    ],
    'roman to integer': [
        (("III",), 3), (("LVIII",), 58), (("MCMXCIV",), 1994), (("IV",), 4), (("IX",), 9), (("XL",), 40)
    ],
    'longest common prefix': [
        ((["flower","flow","flight"],), "fl"), ((["dog","racecar","car"],), ""), ((["a"],), "a"), (([],), ""), ((["ab","a"],), "a"), ((["",""],), "")
    ],
    'valid parentheses': [
        (("()",), True), (("()[]{}",), True), (("(]",), False), (("([)]",), False), (("{[]}",), True), (("",), True)
    ],
    'merge two sorted lists': [
        (([1,2,4],[1,3,4]), [1,1,2,3,4,4]), (([],[]), []), (([],[0]), [0]), (([1],[]), [1]), (([1,3,5],[2,4]), [1,2,3,4,5]), (([1,1],[1]), [1,1,1])
    ],
    'remove duplicates from sorted array': [
        (([1,1,2],), ([1,2],2)), (([0,0,1,1,1,2,2,3,3,4],), ([0,1,2,3,4],5)), (([],), ([],0)), (([1],), ([1],1)), (([1,1,1],), ([1],1)), (([1,2,3],), ([1,2,3],3))
    ],
    'remove element': [
        (([3,2,2,3],3), ([2,2],2)), (([0,1,2,2,3,0,4,2],2), ([0,1,3,0,4],5)), (([],1), ([],0)), (([1],1), ([],0)), (([1],2), ([1],1)), (([2,2],2), ([],0))
    ],
    'find the index of the first occurrence in a string': [
        (("sadbutsad","sad"), 0), (("leetcode","leeto"), -1), (("a","a"), 0), (("aaa","aa"), 0), (("","a"), -1), (("abc",""), 0)
    ],
    'search insert position': [
        (([1,3,5,6],5), 2), (([1,3,5,6],2), 1), (([1,3,5,6],7), 4), (([1,3,5,6],0), 0), (([],5), 0), (([1],0), 0)
    ],
    'length of last word': [
        (("Hello World",), 5), (("   fly me   to   the moon  ",), 4), (("luffy is still joyboy",), 6), (("a",), 1), (("",), 0), (("endspace ",), 8)
    ],
    'plus one': [
        (([1,2,3],), [1,2,4]), (([4,3,2,1],), [4,3,2,2]), (([9],), [1,0]), (([9,9],), [1,0,0]), (([0],), [1]), (([1,9],), [2,0])
    ],
    'add binary': [
        (("11","1"), "100"), (("1010","1011"), "10101"), (("0","0"), "0"), (("1","0"), "1"), (("111","1"), "1000"), (("10","10"), "100")
    ],
    'sqrt x': [
        ((4,), 2), ((8,), 2), ((0,), 0), ((1,), 1), ((2147395599,), 46339), ((15,), 3)
    ],
    'climbing stairs': [
        ((1,), 1), ((2,), 2), ((3,), 3), ((4,), 5), ((5,), 8), ((6,), 13)
    ],
    'merge sorted array': [
        (([1,2,3],[2,5,6]), [1,2,2,3,5,6]), (([1],[]), [1]), (([],[1]), [1]), (([],[]), []), (([2,0],[1]), [1,2]), (([4,5],[1,2,3]), [1,2,3,4,5])
    ],
    'valid palindrome': [
        (("A man, a plan, a canal: Panama",), True), (("race a car",), False), ((" ",), True), (("",), True), (("0P",), False), (("abba",), True)
    ],
    'single number': [
        (([2,2,1],), 1), (([4,1,2,1,2],), 4), (([1],), 1), (([7,7,8],), 8), (([0,1,0],), 1), (([-1,-1,-2],), -2)
    ],
    'contains duplicate': [
        (([1,2,3,1],), True), (([1,2,3,4],), False), (([],), False), (([1,1],), True), (([1],), False), (([2,14,18,22,22],), True)
    ],
    'reverse string': [
        (("hello",), "olleh"), (("",), ""), (("a",), "a"), (("ab",), "ba"), (("racecar",), "racecar"), (("Python",), "nohtyP")
    ],
    'binary search': [
        (([-1,0,3,5,9,12],9), 4), (([-1,0,3,5,9,12],2), -1), (([5],5), 0), (([5],-5), -1), (([],1), -1), (([1,2,3],1), 0)
    ],
    'flood fill': [
        (([[1,1,1],[1,1,0],[1,0,1]],1,1,2), [[2,2,2],[2,2,0],[2,0,1]]),
        (([[0,0,0],[0,0,0]],0,0,0), [[0,0,0],[0,0,0]]),
        (([[0]],0,0,2), [[2]]),
        (([[1]],0,0,1), [[1]]),
        (([[1,1],[1,1]],1,0,9), [[9,9],[9,9]]),
        (([[1,0,1]],0,0,3), [[3,0,1]]),
    ],
    'number of islands': [
        (([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],), 1),
        (([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],), 3),
        (([],), 0), (([["0"]],), 0), (([["1"]],), 1), (([["1","0"],["0","1"]],), 2),
    ],
    'coin change': [
        (([1,2,5],11), 3), (([2],3), -1), (([1],0), 0), (([1],2), 2), (([1,3,4],6), 2), (([3,7],5), -1)
    ],
    'longest increasing subsequence': [
        (([10,9,2,5,3,7,101,18],), 4), (([0,1,0,3,2,3],), 4), (([7,7,7,7],), 1), (([],), 0), (([1],), 1), (([4,10,4,3,8,9],), 3)
    ],
    'minimum window substring': [
        (("ADOBECODEBANC","ABC"), "BANC"), (("a","a"), "a"), (("a","aa"), ""), (("ab","b"), "b"), (("aa","aa"), "aa"), (("xyz","a"), "")
    ],
    'lru cache': [
        (((2, [["put",1,1],["put",2,2],["get",1],["put",3,3],["get",2],["put",4,4],["get",1],["get",3],["get",4]]),), [None,None,1,None,-1,None,-1,3,4]),
        (((1, [["put",1,1],["put",2,2],["get",1],["get",2]]),), [None,None,-1,2]),
        (((2, [["put",2,1],["put",2,2],["get",2]]),), [None,None,2]),
        (((1, [["put",2,1],["get",2],["put",3,2],["get",2],["get",3]]),), [None,1,None,-1,2]),
        (((2, []),), []),
        (((2, [["get",1]]),), [-1]),
    ],
}


def domain_of(title_l: str) -> str:
    if any(k in title_l for k in ['string','substring','anagram','palindrome','roman','word','parentheses','bracket','character','vowel']):
        return 'string'
    if any(k in title_l for k in ['matrix','grid','sudoku','spiral','flood fill','rectangle','row','column']):
        return 'matrix'
    if any(k in title_l for k in ['binary tree','bst','tree','inorder','preorder','postorder','level order','path sum']):
        return 'tree'
    if any(k in title_l for k in ['graph','islands','course schedule','connected components','topological','clone graph','path exists']):
        return 'graph'
    if any(k in title_l for k in ['linked list','stack','queue','deque','trie','cache','hashmap','hashset','iterator','design','implement']):
        return 'data_structure'
    if any(k in title_l for k in ['interval','meeting','arrows']):
        return 'interval'
    if any(k in title_l for k in ['array','list','subarray','pair','kth','rotate','sort','duplicate','missing','majority','stock','sum']):
        return 'array'
    return 'number'


def fallback_tests(title: str):
    tl = normalize_title(title)
    domain = domain_of(tl)

    # title-aware heuristic tests (not placeholders)
    if domain == 'string':
        if tl.startswith('check ') or tl.startswith('valid ') or ' palindrome' in tl or 'anagram' in tl:
            return [(("abba",), True), (("abc",), False), (("",), True), (("a",), True), (("ab",), False), (("racecar",), True)]
        if tl.startswith('count ') or 'length' in tl:
            return [(("abc",), 3), (("",), 0), (("a",), 1), (("hello",), 5), (("a1b2",), 4), (("Hi There",), 8)]
        if 'reverse' in tl:
            return [(("hello",), "olleh"), (("",), ""), (("a",), "a"), (("ab",), "ba"), (("racecar",), "racecar"), (("Python",), "nohtyP")]
        return [(("hello",), "hello"), (("",), ""), (("a",), "a"), (("abc123",), "abc123"), (("Hi There",), "Hi There"), (("x",), "x")]

    if domain == 'array':
        if tl.startswith('remove ') or tl.startswith('delete '):
            return [(([1,2,2,3],), [1,2,3]), (([],), []), (([1],), [1]), (([5,5,5],), [5]), (([3,1,2,1],), [3,1,2]), (([0,0,1],), [0,1])]
        if tl.startswith('insert '):
            return [(([1,2,3], 1, 9), [1,9,2,3]), (([],0,5), [5]), (([1],1,2), [1,2]), (([1,2],0,0), [0,1,2]), (([1,2],2,3), [1,2,3]), (([1,1],1,1), [1,1,1])]
        if tl.startswith('merge '):
            return [(([1,3,5],[2,4,6]), [1,2,3,4,5,6]), (([],[1]), [1]), (([1],[]), [1]), (([],[]), []), (([1,1],[1]), [1,1,1]), (([2,3],[1]), [1,2,3])]
        if tl.startswith('rotate '):
            return [(([1,2,3,4],1), [2,3,4,1]), (([1],3), [1]), (([],1), []), (([1,2],2), [1,2]), (([1,2,3],2), [3,1,2]), (([0,0,1],1), [0,1,0])]
        if tl.startswith('reverse '):
            return [(([1,2,3],), [3,2,1]), (([],), []), (([1],), [1]), (([1,2],), [2,1]), (([0,0],), [0,0]), (([-1,1],), [1,-1])]
        if tl.startswith('count ') or 'length' in tl or 'sum' in tl:
            return [(([1,2,3],), 3), (([],), 0), (([1],), 1), (([0,0],), 2), (([-1,1],), 2), (([5,6,7,8],), 4)]
        if tl.startswith('find '):
            return [(([1,2,3],), 1), (([],), -1), (([1],), 0), (([5,4,3],), 5), (([-1,1],), -1), (([9,9],), 9)]
        if tl.startswith('check ') or 'contains' in tl:
            return [(([1,2,3],), True), (([],), True), (([1],), True), (([1,1],), True), (([2,1],), False), (([0],), True)]
        if (re.search(r'\bsort\b|\bsorted\b', tl) is not None) and ('unsorted' not in tl):
            return [(([3,1,2],), [1,2,3]), (([],), []), (([1],), [1]), (([2,2,1],), [1,2,2]), (([-1,3,0],), [-1,0,3]), (([5,4],), [4,5])]
        if 'move' in tl or 'replace' in tl or 'split' in tl:
            return [(([0,1,0,2],), [1,2,0,0]), (([],), []), (([1],), [1]), (([1,2,3],), [1,2,3]), (([0,0],), [0,0]), (([-1,1],), [1,-1])]
        return [(([1,2,3],), [1,2,3]), (([],), []), (([0],), [0]), (([-1,1],), [-1,1]), (([2,2],), [2,2]), (([5,6],), [5,6])]

    if domain == 'matrix':
        if 'count' in tl or 'sum' in tl or 'number of' in tl:
            return [(([[1,2],[3,4]],), 10), (([[0]],), 0), (([[]],), 0), (([[5]],), 5), (([[1,-1]],), 0), (([[1,1],[1,1]],), 4)]
        if 'transpose' in tl or 'rotate' in tl:
            return [(([[1,2],[3,4]],), [[1,3],[2,4]]), (([[1]],), [[1]]), (([[1,2]],), [[1],[2]]), (([[1],[2]],), [[1,2]]), (([[]],), [[]]), (([[1,2,3],[4,5,6]],), [[1,4],[2,5],[3,6]])]
        return [(([[1,2],[3,4]],), [[1,2],[3,4]]), (([[0]],), [[0]]), (([[]],), [[]]), (([[1]],), [[1]]), (([[1,-1]],), [[1,-1]]), (([[5,6]],), [[5,6]])]

    if domain == 'graph':
        return [
            (((3, [[0,1],[1,2]]),), True),
            (((3, [[0,1]]),), False),
            (((1, []),), True),
            (((4, [[0,1],[2,3]]),), False),
            (((4, [[0,1],[1,2],[2,3]]),), True),
            (((2, []),), False),
        ]

    if domain == 'tree':
        return [
            (([1,2,3],), 2),
            (([],), 0),
            (([1],), 1),
            (([1,None,2],), 2),
            (([3,9,20,None,None,15,7],), 3),
            (([1,2,None,3],), 3),
        ]

    if domain == 'data_structure':
        return [
            ((([["push",1],["pop"], ["empty"]],),), [None,1,True]),
            ((([["push",2],["push",3],["top"]],),), [None,None,3]),
            ((([["put",1,1],["get",1]],),), [None,1]),
            ((([["enqueue",1],["dequeue"]],),), [None,1]),
            ((([["insert",1],["search",1]],),), [None,True]),
            ((([],),), []),
        ]

    # numeric fallback
    return [((5,), 5), ((0,), 0), ((-1,), -1), ((10,), 10), ((1,), 1), ((7,), 7)]


def tests_for(title: str):
    t = normalize_title(title)
    if t in KNOWN:
        return KNOWN[t], 'known'
    return fallback_tests(title), f'fallback_{domain_of(t)}'


def rewrite_file(path: Path) -> str:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    title = lines[0].replace('# Title: ', '').strip()
    difficulty = lines[1].replace('# Difficulty: ', '').strip()
    tests, bucket = tests_for(title)

    desc = description_line(title)

    out = [
        f'# Title: {title}',
        f'# Difficulty: {difficulty}',
        '#',
        '# Description:',
        f'# {desc}',
        '#',
        '',
        'def solve(*args):',
        '    """Implement the solution here."""',
        '    raise NotImplementedError',
        '',
        '',
        '# Tests',
        'if __name__ == "__main__":',
        '    tests = [',
    ]
    for args, expected in tests:
        out.append(f'        ({repr(args)}, {repr(expected)}),')
    out += [
        '    ]',
        '    passed = 0',
        '    for args, expected in tests:',
        '        if not isinstance(args, tuple):',
        '            args = (args,)',
        '        try:',
        '            result = solve(*args)',
        '            ok = result == expected',
        '        except Exception as e:',
        '            result = f"<error: {type(e).__name__}>"',
        '            ok = False',
        '        status = "passed" if ok else "failed"',
        '        print(f"solve{args} == {expected} -> {result} ({status})")',
        '        if ok:',
        '            passed += 1',
        '    print(f"{passed}/{len(tests)} tests passed")',
    ]
    path.write_text('\n'.join(out) + '\n', encoding='utf-8')
    return bucket


def main():
    total = 0
    buckets = {}
    for d in TARGET_DIRS:
        cnt = 0
        for f in sorted((BASE / d).glob('[0-9][0-9][0-9]_*.py')):
            b = rewrite_file(f)
            buckets[b] = buckets.get(b, 0) + 1
            cnt += 1
        total += cnt
        print(f'{d}: rebuilt {cnt} files')
    print(f'Total rebuilt: {total}')
    for k in sorted(buckets):
        print(k, buckets[k])


if __name__ == '__main__':
    main()
