#!/usr/bin/env python3
"""Rewrite challenge descriptions with simple, specific problem-style wording."""

from pathlib import Path
import re

BASE = Path('/Users/numky/Code/edabit')
DIFF_DIRS = ['01_very_easy', '02_easy', '03_medium', '04_hard']


def subject_from_title(title_l: str) -> str:
    if any(k in title_l for k in ['string', 'substring', 'anagram', 'palindrome', 'roman', 'word', 'parentheses', 'bracket', 'character', 'vowel']):
        return 'one or more strings'
    if any(k in title_l for k in ['matrix', 'grid', 'sudoku', 'spiral', 'flood fill', 'rectangle', 'row', 'column']):
        return 'a 2D grid/matrix'
    if any(k in title_l for k in ['interval', 'meeting', 'arrows']):
        return 'a list of intervals'
    if any(k in title_l for k in ['binary tree', 'bst', 'tree', 'inorder', 'preorder', 'postorder', 'level order', 'path sum']):
        return 'a tree input'
    if any(k in title_l for k in ['graph', 'islands', 'course schedule', 'connected components', 'topological', 'clone graph', 'path exists']):
        return 'graph-style input'
    if any(k in title_l for k in ['linked list', 'stack', 'queue', 'deque', 'trie', 'cache', 'hashmap', 'hashset', 'iterator']):
        return 'data-structure input'
    if any(k in title_l for k in ['array', 'list', 'subarray', 'pair', 'kth', 'rotate', 'sort', 'duplicate', 'missing', 'majority', 'stock', 'sum', 'coin', 'robber', 'paths', 'lis', 'subsequence']):
        return 'an array/list and optional parameters'
    return 'one or more input values'


def goal_from_title(title: str) -> str:
    t = title.lower()

    special = {
        'two sum': 'find the pair that satisfies the target-sum condition',
        'three sum': 'find triplets that satisfy the required sum condition',
        'four sum': 'find quadruplets that satisfy the required sum condition',
        'merge intervals': 'merge overlapping intervals',
        'insert interval': 'insert the new interval and merge overlaps if needed',
        'number of islands': 'count connected islands using 4-direction adjacency',
        'flood fill': 'recolor the connected region starting at the given cell',
        'binary search': 'locate the target in sorted order',
        'valid parentheses': 'check whether brackets are balanced and correctly ordered',
        'add binary': 'add binary values and build the binary sum',
        'coin change': 'compute the minimum number of coins needed (or report impossible)',
        'longest increasing subsequence': 'compute the length of the longest increasing subsequence',
        'minimum window substring': 'find the shortest substring that covers all required characters',
        'lru cache': 'support cache operations with least-recently-used eviction',
        'rotate image': 'rotate the square matrix by 90 degrees',
        'set matrix zeroes': 'set row and column to zero when a zero cell appears',
    }
    for key, text in special.items():
        if key in t:
            return text

    # Verb-based fallback
    for prefix in ['find ', 'count ', 'check ', 'is ', 'can ', 'convert ', 'reverse ', 'rotate ', 'merge ', 'sort ', 'remove ', 'delete ', 'insert ', 'add ', 'search ', 'build ', 'design ', 'implement ']:
        if t.startswith(prefix):
            return t

    return title.lower()


def output_from_title(title_l: str) -> str:
    if any(k in title_l for k in ['two sum', 'three sum', 'four sum', 'group anagrams', 'top k', 'subsets', 'permutations', 'combination', 'merge intervals', 'insert interval', 'interval intersection']):
        return 'a list/collection result'
    if any(k in title_l for k in ['design ', 'implement ', 'cache']):
        return 'outputs for the required operations'
    if any(k in title_l for k in ['check', 'valid', ' is ', ' can ', 'contains', 'equal', 'palindrome', 'anagram']):
        return 'a boolean result'
    if any(k in title_l for k in ['count', 'number of', 'sum', 'minimum', 'maximum', 'length', 'profit', 'depth', 'distance', 'area']):
        return 'a numeric result'
    if any(k in title_l for k in ['index', 'position', 'search', 'kth']):
        return 'the requested index/value'
    if any(k in title_l for k in ['group', 'merge', 'insert', 'sort', 'reverse', 'rotate', 'subsets', 'permutations', 'combination', 'interval', 'top k']):
        return 'a list/collection result'
    if any(k in title_l for k in ['design', 'implement', 'cache']):
        return 'outputs for the required operations'
    return 'the final result'


def build_description(title: str) -> list[str]:
    tl = title.lower()
    return [
        f'Task: {title}.',
        f'Given {subject_from_title(tl)}.',
        f'Goal: {goal_from_title(title)}.',
        f'Return {output_from_title(tl)}.',
    ]


def rewrite_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    m = re.search(r'^# Title:\s*(.+)$', text, flags=re.M)
    if not m:
        return False

    title = m.group(1).strip()
    lines = build_description(title)
    block = '# Description:\n' + '\n'.join(f'# {line}' for line in lines) + '\n#\n'

    pattern = re.compile(r'# Description:\n(?:#.*\n)*?#\n\ndef solve\(\*args\):', flags=re.M)
    if not pattern.search(text):
        return False

    updated = pattern.sub(block + '\ndef solve(*args):', text, count=1)
    path.write_text(updated, encoding='utf-8')
    return True


def main() -> None:
    total = 0
    for d in DIFF_DIRS:
        folder = BASE / d
        changed = 0
        for f in sorted(folder.glob('[0-9][0-9][0-9]_*.py')):
            if rewrite_file(f):
                changed += 1
        total += changed
        print(f'{d}: updated {changed} files')
    print(f'Total updated: {total}')


if __name__ == '__main__':
    main()
