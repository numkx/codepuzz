#!/usr/bin/env python3
from pathlib import Path
import re

BASE = Path('/Users/numky/Code/edabit')
TARGET_DIRS = ['02_easy', '03_medium', '04_hard']


def out_kind(title_l: str) -> str:
    if any(k in title_l for k in ['check ', 'is ', 'are ', 'can ', 'contains', 'equal', 'palindrome', 'anagram', 'valid']):
        return 'a boolean value'
    if any(k in title_l for k in ['count', 'sum', 'average', 'median', 'minimum', 'maximum', 'length', 'profit', 'depth', 'distance', 'area', 'kth', 'index', 'position']):
        return 'a numeric value'
    if any(k in title_l for k in ['print', 'reverse', 'sort', 'merge', 'split', 'interleave', 'rotate', 'move', 'replace', 'remove', 'insert', 'delete', 'create', 'convert', 'flatten', 'transpose', 'join', 'group']):
        return 'a list/string result'
    return 'the required output'


def description_lines(title: str) -> list[str]:
    tl = re.sub(r'\s*\([^)]*\)\s*', '', title.lower()).strip()

    special = {
        'two sum': 'Return the indices or values of two elements whose sum equals the target.',
        'three sum': 'Return triplets that satisfy the required sum condition.',
        'four sum': 'Return quadruplets that satisfy the required sum condition.',
        'coin change': 'Return the minimum number of coins needed to make the target amount, or -1 if impossible.',
        'lru cache': 'Implement least-recently-used cache behavior and return outputs for required operations.',
        'number of islands': 'Return the number of connected islands in the grid.',
        'merge intervals': 'Merge overlapping intervals and return the merged list.',
        'insert interval': 'Insert the interval, merge overlaps, and return the final intervals.',
        'binary search': 'Return the target index in the sorted array, or -1 when it is not present.',
        'valid parentheses': 'Return True when brackets are balanced and correctly ordered, otherwise return False.',
        'minimum window substring': 'Return the shortest substring that contains all required characters.',
        'longest increasing subsequence': 'Return the length of the longest strictly increasing subsequence.',
        'product of array except self': 'Return an array where each index is the product of all other elements.',
        'group anagrams': 'Group words that are anagrams and return the grouped lists.',
        'course schedule': 'Return whether all courses can be finished under the prerequisite constraints.',
        'flood fill': 'Recolor the connected region starting from the given cell and return the updated grid.',
        'set matrix zeroes': 'Set rows and columns to zero when a cell is zero, then return the updated matrix.',
        'rotate image': 'Rotate the square matrix by 90 degrees and return the result.',
    }
    for key, sentence in special.items():
        if key in tl:
            return [sentence]

    if tl.startswith('check if '):
        return [f'Return True if {tl.replace("check if ", "", 1)}, otherwise return False.']
    if tl.startswith('check whether '):
        return [f'Return True if {tl.replace("check whether ", "", 1)}, otherwise return False.']
    if tl.startswith('count '):
        return [f'Return the count of {tl.replace("count ", "", 1)}.']
    if tl.startswith('find '):
        return [f'Return {tl.replace("find ", "", 1)}.']
    if tl.startswith('sum '):
        return [f'Return the sum of {tl.replace("sum ", "", 1)}.']
    if tl.startswith('print '):
        return [f'Return {tl.replace("print ", "", 1)}.']
    if tl.startswith('convert '):
        return [f'Convert {tl.replace("convert ", "", 1)} and return the converted value.']
    if tl.startswith('create '):
        return [f'Create {tl.replace("create ", "", 1)} and return it.']
    if tl.startswith('replace '):
        return [f'Replace {tl.replace("replace ", "", 1)} and return the updated result.']
    if tl.startswith('remove '):
        return [f'Remove {tl.replace("remove ", "", 1)} and return the result.']
    if tl.startswith('insert '):
        return [f'Insert {tl.replace("insert ", "", 1)} and return the updated result.']
    if tl.startswith('delete '):
        return [f'Delete {tl.replace("delete ", "", 1)} and return the updated result.']
    if tl.startswith('reverse '):
        return [f'Reverse {tl.replace("reverse ", "", 1)} and return the result.']
    if tl.startswith('rotate '):
        return [f'Rotate {tl.replace("rotate ", "", 1)} and return the result.']
    if tl.startswith('sort '):
        return [f'Sort {tl.replace("sort ", "", 1)} and return the result.']
    if tl.startswith('merge '):
        return [f'Merge {tl.replace("merge ", "", 1)} and return the merged result.']
    if tl.startswith('swap '):
        return [f'Swap {tl.replace("swap ", "", 1)} and return the updated result.']
    if tl.startswith('calculate '):
        return [f'Calculate {tl.replace("calculate ", "", 1)} and return the result.']
    if tl.startswith('get '):
        return [f'Return {tl.replace("get ", "", 1)}.']
    if tl.startswith('keep '):
        return [f'Keep {tl.replace("keep ", "", 1)} and return the result.']
    if tl.startswith('split '):
        return [f'Split {tl.replace("split ", "", 1)} and return the result.']
    if tl.startswith('compare '):
        return [f'Compare {tl.replace("compare ", "", 1)} and return the result.']
    if tl.startswith('interleave '):
        return [f'Interleave {tl.replace("interleave ", "", 1)} and return the result.']
    if tl.startswith('flatten '):
        return [f'Flatten {tl.replace("flatten ", "", 1)} and return the flattened output.']
    if tl.startswith('transpose '):
        return [f'Transpose {tl.replace("transpose ", "", 1)} and return the transposed result.']
    if tl.startswith('integer division quotient'):
        return ['Return the integer quotient after division.']
    if tl.startswith('integer division remainder'):
        return ['Return the remainder after division.']

    return ['Return the result after applying the required operation to the input.']


def rewrite_description(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    m = re.search(r'^# Title:\s*(.+)$', text, flags=re.M)
    if not m:
        return False
    title = m.group(1).strip()

    block = '# Description:\n' + '\n'.join(f'# {line}' for line in description_lines(title)) + '\n#\n'
    pattern = re.compile(r'# Description:\n(?:#.*\n)*?#\n\ndef solve\(\*args\):', flags=re.M)
    if not pattern.search(text):
        return False

    updated = pattern.sub(block + '\ndef solve(*args):', text, count=1)
    path.write_text(updated, encoding='utf-8')
    return True


def main() -> None:
    total = 0
    for d in TARGET_DIRS:
        changed = 0
        for f in sorted((BASE / d).glob('[0-9][0-9][0-9]_*.py')):
            if rewrite_description(f):
                changed += 1
        total += changed
        print(f'{d}: updated {changed} files')
    print(f'Total updated: {total}')


if __name__ == '__main__':
    main()
