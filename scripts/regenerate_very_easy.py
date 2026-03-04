#!/usr/bin/env python3
from pathlib import Path
import re

DIR = Path('/Users/numky/Code/edabit/01_very_easy')


def out_kind(title_l: str) -> str:
    if any(k in title_l for k in ['check ', 'is ', 'are ', 'can ', 'contains', 'equal', 'palindrome', 'anagram', 'sorted', 'unique']):
        return 'a boolean value'
    if any(k in title_l for k in ['count', 'sum', 'average', 'median', 'middle', 'index', 'largest', 'smallest', 'length', 'number of', 'gcd', 'lcm', 'factorial', 'power', 'percentage']):
        return 'a numeric value'
    if any(k in title_l for k in ['print', 'reverse', 'sort', 'merge', 'split', 'interleave', 'rotate', 'move', 'replace', 'remove', 'insert', 'delete', 'create', 'convert', 'flatten', 'transpose', 'join']):
        return 'a list/string result'
    return 'the required output'


def description(title: str) -> list[str]:
    tl = title.lower()
    clean = re.sub(r'\s*\([^)]*\)\s*', '', tl).strip()

    if clean.startswith('check if '):
        cond = clean.replace('check if ', '', 1)
        return [f'Return True if {cond}, otherwise return False.']

    if clean.startswith('count '):
        what = clean.replace('count ', '', 1)
        return [f'Return the count of {what}.']

    if clean.startswith('find '):
        what = clean.replace('find ', '', 1)
        return [f'Return {what}.']

    if clean.startswith('sum '):
        what = clean.replace('sum ', '', 1)
        return [f'Return the sum of {what}.']

    if clean.startswith('print '):
        what = clean.replace('print ', '', 1)
        return [f'Return {what}.']

    if clean.startswith('convert '):
        what = clean.replace('convert ', '', 1)
        return [f'Convert {what} and return the converted value.']

    if clean.startswith('create '):
        what = clean.replace('create ', '', 1)
        return [f'Create {what} and return it.']

    if clean.startswith('replace '):
        what = clean.replace('replace ', '', 1)
        return [f'Replace {what} and return the updated result.']

    if clean.startswith('remove '):
        what = clean.replace('remove ', '', 1)
        return [f'Remove {what} and return the result.']

    if clean.startswith('insert '):
        what = clean.replace('insert ', '', 1)
        return [f'Insert {what} and return the updated result.']

    if clean.startswith('delete '):
        what = clean.replace('delete ', '', 1)
        return [f'Delete {what} and return the updated result.']

    if clean.startswith('reverse '):
        what = clean.replace('reverse ', '', 1)
        return [f'Reverse {what} and return the result.']

    if clean.startswith('rotate '):
        what = clean.replace('rotate ', '', 1)
        return [f'Rotate {what} and return the result.']

    if clean.startswith('sort '):
        what = clean.replace('sort ', '', 1)
        return [f'Sort {what} and return the result.']

    if clean.startswith('merge '):
        what = clean.replace('merge ', '', 1)
        return [f'Merge {what} and return the merged result.']

    if clean.startswith('swap '):
        what = clean.replace('swap ', '', 1)
        return [f'Swap {what} and return the updated result.']

    if clean.startswith('calculate '):
        what = clean.replace('calculate ', '', 1)
        return [f'Calculate {what} and return the result.']

    if clean.startswith('get '):
        what = clean.replace('get ', '', 1)
        return [f'Return {what}.']

    if clean.startswith('keep '):
        what = clean.replace('keep ', '', 1)
        return [f'Keep {what} and return the result.']

    if clean.startswith('split '):
        what = clean.replace('split ', '', 1)
        return [f'Split {what} and return the result.']

    if clean.startswith('compare '):
        what = clean.replace('compare ', '', 1)
        return [f'Compare {what} and return the result.']

    if clean.startswith('interleave '):
        what = clean.replace('interleave ', '', 1)
        return [f'Interleave {what} and return the result.']

    if clean.startswith('flatten '):
        what = clean.replace('flatten ', '', 1)
        return [f'Flatten {what} and return the flattened output.']

    if clean.startswith('transpose '):
        what = clean.replace('transpose ', '', 1)
        return [f'Transpose {what} and return the transposed result.']

    if clean.startswith('integer division quotient'):
        return ['Return the integer quotient after division.']

    if clean.startswith('integer division remainder'):
        return ['Return the remainder after division.']

    return [f'Return {out_kind(tl)} for the given input.']


def tests_for(title: str):
    t = title.lower()

    # Core list operations
    if 'print all elements of a list' in t:
        return [(( [1,2,3], ), [1,2,3]), (([],), []), (((-1,0,1),), [-1,0,1]), (([5],), [5]), (([2,2],), [2,2])], 'specific'
    if 'print list elements in reverse order' in t:
        return [(([1,2,3],), [3,2,1]), (([],), []), (([5],), [5]), (([-1,0,1],), [1,0,-1]), (([2,2],), [2,2])], 'specific'
    if 'find list length' in t:
        return [(([1,2,3],), 3), (([],), 0), (([5],), 1), ((['a','b'],), 2), (([None,None,None],), 3)], 'specific'
    if 'find first element of a list' in t:
        return [(([1,2,3],), 1), ((['a','b'],), 'a'), (([0],), 0), (([-5,-4],), -5), (([None,1],), None)], 'specific'
    if 'find last element of a list' in t:
        return [(([1,2,3],), 3), ((['a','b'],), 'b'), (([0],), 0), (([-5,-4],), -4), (([1,None],), None)], 'specific'
    if 'sum all elements in a list' in t:
        return [(([1,2,3],), 6), (([],), 0), (([-1,1,5],), 5), (([0,0],), 0), (([10],), 10)], 'specific'
    if 'find maximum element in a list' in t:
        return [(([1,2,3],), 3), (([-1,-5,-3],), -1), (([7],), 7), (([0,0],), 0), (([2,9,4],), 9)], 'specific'
    if 'find minimum element in a list' in t:
        return [(([1,2,3],), 1), (([-1,-5,-3],), -5), (([7],), 7), (([0,0],), 0), (([2,9,4],), 2)], 'specific'

    # Count-based list patterns
    if 'count even numbers in a list' in t:
        return [(([1,2,3,4],), 2), (([],), 0), (([2,4,6],), 3), (([1,3,5],), 0), (([0,1],), 1)], 'specific'
    if 'count odd numbers in a list' in t:
        return [(([1,2,3,4],), 2), (([],), 0), (([2,4,6],), 0), (([1,3,5],), 3), (([0,1],), 1)], 'specific'
    if 'count positive numbers in a list' in t:
        return [(([-1,0,1,2],), 2), (([],), 0), (([1,2,3],), 3), (([-1,-2],), 0), (([0],), 0)], 'specific'
    if 'count negative numbers in a list' in t:
        return [(([-1,0,1,2],), 1), (([],), 0), (([1,2,3],), 0), (([-1,-2],), 2), (([0],), 0)], 'specific'
    if 'count zeros in a list' in t:
        return [(([0,1,0,2],), 2), (([],), 0), (([1,2,3],), 0), (([0,0,0],), 3), (([-1,0],), 1)], 'specific'

    # Simple transforms
    if 'replace all negative numbers with 0' in t:
        return [(([-1,2,-3],), [0,2,0]), (([],), []), (([1,2],), [1,2]), (([-1,-2],), [0,0]), (([0,-1],), [0,0])], 'specific'
    if 'replace all zeros with -1' in t:
        return [(([0,1,0],), [-1,1,-1]), (([],), []), (([1,2],), [1,2]), (([0,0],), [-1,-1]), (([-1,0],), [-1,-1])], 'specific'
    if 'multiply each list element by 2' in t:
        return [(([1,2,3],), [2,4,6]), (([],), []), (([-1,0],), [-2,0]), (([5],), [10]), (([2,2],), [4,4])], 'specific'
    if 'add 1 to each list element' in t:
        return [(([1,2,3],), [2,3,4]), (([],), []), (([-1,0],), [0,1]), (([5],), [6]), (([2,2],), [3,3])], 'specific'
    if 'square each list element' in t:
        return [(([1,2,3],), [1,4,9]), (([],), []), (([-1,0],), [1,0]), (([5],), [25]), (([2,2],), [4,4])], 'specific'
    if 'cube each list element' in t:
        return [(([1,2,3],), [1,8,27]), (([],), []), (([-1,0],), [-1,0]), (([5],), [125]), (([2,2],), [8,8])], 'specific'
    if 'find index of first occurrence of a value' in t:
        return [(([1,2,3,2],2), 1), (([5,5,5],5), 0), (([1,2,3],4), -1), (([],1), -1), (([9],9), 0)], 'specific'
    if 'find index of last occurrence of a value' in t:
        return [(([1,2,3,2],2), 3), (([5,5,5],5), 2), (([1,2,3],4), -1), (([],1), -1), (([9],9), 0)], 'specific'
    if 'count occurrences of a value in a list' in t:
        return [(([1,2,2,3],2), 2), (([5,5,5],5), 3), (([1,2,3],4), 0), (([],1), 0), (([9],9), 1)], 'specific'
    if 'check if a value exists in a list' in t:
        return [(([1,2,3],2), True), (([1,2,3],4), False), (([],1), False), (([0],0), True), ((['a','b'],'c'), False)], 'specific'
    if 'remove all occurrences of a value' in t:
        return [(([1,2,2,3],2), [1,3]), (([5,5,5],5), []), (([1,2,3],4), [1,2,3]), (([],1), []), (([9],9), [])], 'specific'
    if 'remove first occurrence of a value' in t:
        return [(([1,2,2,3],2), [1,2,3]), (([5,5,5],5), [5,5]), (([1,2,3],4), [1,2,3]), (([],1), []), (([9],9), [])], 'specific'
    if 'insert a value at the beginning of a list' in t:
        return [(([1,2,3],0), [0,1,2,3]), (([],5), [5]), (([9],8), [8,9]), ((['b'],'a'), ['a','b']), (([1,1],1), [1,1,1])], 'specific'
    if 'insert a value at the end of a list' in t:
        return [(([1,2,3],0), [1,2,3,0]), (([],5), [5]), (([9],8), [9,8]), ((['a'],'b'), ['a','b']), (([1,1],1), [1,1,1])], 'specific'
    if 'insert a value at a given index' in t:
        return [(([1,2,3],1,9), [1,9,2,3]), (([],0,5), [5]), (([9],1,8), [9,8]), ((['a','c'],1,'b'), ['a','b','c']), (([1,1],2,1), [1,1,1])], 'specific'
    if 'delete element at a given index' in t:
        return [(([1,2,3],1), [1,3]), (([5],0), []), (([9,8],1), [9]), ((['a','b','c'],2), ['a','b']), (([1,1,1],1), [1,1])], 'specific'
    if 'delete first element of a list' in t:
        return [(([1,2,3],), [2,3]), (([5],), []), (([],), []), ((['a','b'],), ['b']), (([1,1],), [1])], 'specific'
    if 'delete last element of a list' in t:
        return [(([1,2,3],), [1,2]), (([5],), []), (([],), []), ((['a','b'],), ['a']), (([1,1],), [1])], 'specific'
    if 'swap first and last list elements' in t:
        return [(([1,2,3],), [3,2,1]), (([5],), [5]), (([],), []), ((['a','b'],), ['b','a']), (([1,1],), [1,1])], 'specific'
    if 'swap two given indices in a list' in t:
        return [(([1,2,3],0,2), [3,2,1]), (([5,6],0,1), [6,5]), ((['a','b','c'],1,2), ['a','c','b']), (([1],0,0), [1]), (([1,1,2],0,1), [1,1,2])], 'specific'
    if 'reverse a list in-place' in t:
        return [(([1,2,3],), [3,2,1]), (([],), []), (([5],), [5]), ((['a','b'],), ['b','a']), (([1,1],), [1,1])], 'specific'
    if 'create a copy of a list' in t:
        return [(([1,2,3],), [1,2,3]), (([],), []), (([5],), [5]), ((['a'],), ['a']), (([1,1],), [1,1])], 'specific'
    if 'compare two lists for equality' in t:
        return [(([1,2],[1,2]), True), (([1,2],[2,1]), False), (([],[]), True), (([1],[1,1]), False), ((['a'],['a']), True)], 'specific'
    if 'merge two lists' in t and 'sorted' not in t:
        return [(([1,2],[3,4]), [1,2,3,4]), (([],[1]), [1]), (([1],[]), [1]), (([],[]), []), ((['a'],['b']), ['a','b'])], 'specific'
    if 'merge two sorted lists' in t:
        return [(([1,3,5],[2,4,6]), [1,2,3,4,5,6]), (([],[1]), [1]), (([1],[]), [1]), (([1,2],[3,4]), [1,2,3,4]), (([1,1],[1]), [1,1,1])], 'specific'
    if 'sort a list ascending' in t:
        return [(([3,1,2],), [1,2,3]), (([],), []), (([1],), [1]), (([2,2,1],), [1,2,2]), (([-1,3,0],), [-1,0,3])], 'specific'
    if 'sort a list descending' in t:
        return [(([3,1,2],), [3,2,1]), (([],), []), (([1],), [1]), (([2,2,1],), [2,2,1]), (([-1,3,0],), [3,0,-1])], 'specific'
    if 'find second largest element' in t:
        return [(([1,2,3],), 2), (([5,5,4],), 4), (([9,1],), 1), (([-1,-2,-3],), -2), (([1,1,1,2],), 1)], 'specific'
    if 'find second smallest element' in t:
        return [(([1,2,3],), 2), (([5,5,4],), 5), (([9,1],), 9), (([-1,-2,-3],), -2), (([1,1,1,2],), 1)], 'specific'
    if 'find difference between max and min' in t:
        return [(([1,2,3],), 2), (([5],), 0), (([-1,1],), 2), (([0,0],), 0), (([2,9,4],), 7)], 'specific'
    if 'find sum of first k elements' in t:
        return [(([1,2,3,4],2), 3), (([1,2,3],0), 0), (([5],1), 5), (([],0), 0), (([1,1,1],2), 2)], 'specific'
    if 'find sum of last k elements' in t:
        return [(([1,2,3,4],2), 7), (([1,2,3],0), 0), (([5],1), 5), (([],0), 0), (([1,1,1],2), 2)], 'specific'
    if 'find average of list elements' in t:
        return [(([1,2,3],), 2.0), (([5],), 5.0), (([0,0],), 0.0), (([-1,1],), 0.0), (([2,4],), 3.0)], 'specific'
    if 'find median of a sorted odd-length list' in t:
        return [(([1,2,3],), 2), (([5],), 5), (([1,3,5,7,9],), 5), (([-3,-2,-1],), -2), (([0,1,2],), 1)], 'specific'
    if 'find middle element of odd-length list' in t:
        return [(([1,2,3],), 2), (([5],), 5), (([1,3,5,7,9],), 5), (([-3,-2,-1],), -2), (([0,1,2],), 1)], 'specific'
    if 'get all even-indexed elements' in t:
        return [(([1,2,3,4],), [1,3]), (([],), []), (([5],), [5]), ((['a','b','c'],), ['a','c']), (([1,1,1],), [1,1])], 'specific'
    if 'get all odd-indexed elements' in t:
        return [(([1,2,3,4],), [2,4]), (([],), []), (([5],), []), ((['a','b','c'],), ['b']), (([1,1,1],), [1])], 'specific'
    if 'sum elements at even indices' in t:
        return [(([1,2,3,4],), 4), (([],), 0), (([5],), 5), (([1,1,1],), 2), (([-1,2,-3],), -4)], 'specific'
    if 'sum elements at odd indices' in t:
        return [(([1,2,3,4],), 6), (([],), 0), (([5],), 0), (([1,1,1],), 1), (([-1,2,-3],), 2)], 'specific'
    if 'count elements greater than x' in t:
        return [(([1,2,3],2), 1), (([],1), 0), (([5,5],4), 2), (([-1,0],0), 0), (([1,1,1],1), 0)], 'specific'
    if 'count elements less than x' in t:
        return [(([1,2,3],2), 1), (([],1), 0), (([5,5],4), 0), (([-1,0],0), 1), (([1,1,1],1), 0)], 'specific'
    if 'replace elements greater than x with x' in t:
        return [(([1,5,3],3), [1,3,3]), (([],1), []), (([5,5],4), [4,4]), (([-1,0],0), [-1,0]), (([1,1],1), [1,1])], 'specific'
    if 'replace elements less than x with 0' in t:
        return [(([1,5,3],3), [0,5,3]), (([],1), []), (([5,5],4), [5,5]), (([-1,0],0), [0,0]), (([1,1],1), [1,1])], 'specific'
    if 'move all zeros to the end' in t:
        return [(([0,1,0,2],), [1,2,0,0]), (([],), []), (([0,0],), [0,0]), (([1,2],), [1,2]), (([0,1],), [1,0])], 'specific'
    if 'move all zeros to the front' in t:
        return [(([0,1,0,2],), [0,0,1,2]), (([],), []), (([0,0],), [0,0]), (([1,2],), [1,2]), (([1,0],), [0,1])], 'specific'
    if 'move all even numbers before odd numbers' in t:
        return [(([1,2,3,4],), [2,4,1,3]), (([],), []), (([2,4],), [2,4]), (([1,3],), [1,3]), (([0,1],), [0,1])], 'specific'
    if 'move all odd numbers before even numbers' in t:
        return [(([1,2,3,4],), [1,3,2,4]), (([],), []), (([2,4],), [2,4]), (([1,3],), [1,3]), (([0,1],), [1,0])], 'specific'
    if 'count adjacent equal pairs' in t:
        return [(([1,1,2,2,2],), 3), (([],), 0), (([1],), 0), (([1,2,3],), 0), (([5,5],), 1)], 'specific'
    if 'count increasing adjacent pairs' in t:
        return [(([1,2,2,3],), 2), (([],), 0), (([1],), 0), (([3,2,1],), 0), (([1,3,2],), 1)], 'specific'
    if 'count decreasing adjacent pairs' in t:
        return [(([3,2,2,1],), 2), (([],), 0), (([1],), 0), (([1,2,3],), 0), (([3,1,2],), 1)], 'specific'
    if 'find largest adjacent difference' in t:
        return [(([1,4,2],), 3), (([5],), 0), (([1,1],), 0), (([-1,2,-3],), 5), (([2,9,4],), 7)], 'specific'
    if 'find smallest adjacent difference' in t:
        return [(([1,4,2],), 2), (([5],), 0), (([1,1],), 0), (([-1,2,-3],), 3), (([2,9,4],), 5)], 'specific'
    if 'replace each element with absolute value' in t:
        return [(([-1,2,-3],), [1,2,3]), (([],), []), (([0],), [0]), (([1,-1],), [1,1]), (([-5],), [5])], 'specific'
    if 'find nearest value to target' in t:
        return [(([1,4,7],5), 4), (([1,4,7],6), 7), (([5],2), 5), (([-2,-1,3],0), -1), (([1,2],2), 2)], 'specific'
    if 'find farthest value from target' in t:
        return [(([1,4,7],5), 1), (([1,4,7],6), 1), (([5],2), 5), (([-2,-1,3],0), 3), (([1,2],2), 1)], 'specific'
    if 'check if all elements are same' in t:
        return [(([1,1,1],), True), (([1,2,1],), False), (([5],), True), (([],), True), ((['a','a'],), True)], 'specific'
    if 'remove duplicate elements (keep first)' in t:
        return [(([1,2,2,3,1],), [1,2,3]), (([],), []), (([1,1,1],), [1]), ((['a','b','a'],), ['a','b']), (([2,3],), [2,3])], 'specific'
    if 'remove duplicate elements (keep last)' in t:
        return [(([1,2,2,3,1],), [2,3,1]), (([],), []), (([1,1,1],), [1]), ((['a','b','a'],), ['b','a']), (([2,3],), [2,3])], 'specific'
    if 'find first non-repeating element' in t:
        return [(([1,2,2,3],), 1), (([2,2,3,3],), None), (([],), None), ((['a','b','a'],), 'b'), (([5],), 5)], 'specific'
    if 'find first repeating element' in t:
        return [(([1,2,2,3],), 2), (([2,2,3,3],), 2), (([],), None), ((['a','b','a'],), 'a'), (([5],), None)], 'specific'
    if 'find all indices of a value' in t:
        return [(([1,2,2,3],2), [1,2]), (([5,5,5],5), [0,1,2]), (([1,2,3],4), []), (([],1), []), (([9],9), [0])], 'specific'
    if 'find smallest element index' in t:
        return [(([3,1,2],), 1), (([5],), 0), (([-1,-5],), 1), (([0,0],), 0), (([2,9,4],), 0)], 'specific'
    if 'find largest element index' in t:
        return [(([3,1,2],), 0), (([5],), 0), (([-1,-5],), 0), (([0,0],), 0), (([2,9,4],), 1)], 'specific'
    if 'find pair with sum equal to target' in t:
        return [(([1,2,3,4],5), [1,4]), (([2,2],4), [2,2]), (([1,2],10), None), (([],3), None), (([-1,1],0), [-1,1])], 'specific'
    if 'count pairs with equal values' in t:
        return [(([1,1,2,2,2],), 4), (([],), 0), (([1],), 0), (([1,2,3],), 0), (([5,5],), 1)], 'specific'

    # String essentials
    if 'count vowels in a string' in t:
        return [(("hello",), 2), (("AEIOU",), 5), (("xyz",), 0), (("",), 0), (("Alphabet",), 3)], 'specific'
    if 'count consonants in a string' in t:
        return [(("hello",), 3), (("AEIOU",), 0), (("xyz",), 3), (("",), 0), (("Alphabet",), 5)], 'specific'
    if 'count digits in a string' in t:
        return [(("a1b2",), 2), (("123",), 3), (("abc",), 0), (("",), 0), (("a0z9",), 2)], 'specific'
    if 'convert string to uppercase' in t:
        return [(("hello",), "HELLO"), (("AbC",), "ABC"), (("",), ""), (("123",), "123"), (("hi there",), "HI THERE")], 'specific'
    if 'convert string to lowercase' in t:
        return [(("HELLO",), "hello"), (("AbC",), "abc"), (("",), ""), (("123",), "123"), (("Hi There",), "hi there")], 'specific'
    if 'check if string is palindrome' in t and 'ignoring' not in t:
        return [(("racecar",), True), (("abba",), True), (("hello",), False), (("a",), True), (("",), True)], 'specific'
    if 'check if two strings are anagrams' in t:
        return [(("listen","silent"), True), (("triangle","integral"), True), (("rat","car"), False), (("a","a"), True), (("ab","a"), False)], 'specific'
    if 'reverse a string' in t:
        return [(("hello",), "olleh"), (("",), ""), (("a",), "a"), (("ab",), "ba"), (("racecar",), "racecar")], 'specific'
    if 'count uppercase letters' in t:
        return [(("AbC",), 2), (("abc",), 0), (("ABC",), 3), (("",), 0), (("A1b2",), 1)], 'specific'
    if 'count lowercase letters' in t:
        return [(("AbC",), 1), (("abc",), 3), (("ABC",), 0), (("",), 0), (("A1b2",), 1)], 'specific'
    if 'trim leading and trailing spaces' in t:
        return [(("  hi  ",), "hi"), (("hi",), "hi"), (("   ",), ""), (("",), ""), ((" a b ",), "a b")], 'specific'
    if 'replace spaces with underscores' in t:
        return [(("a b c",), "a_b_c"), (("",), ""), (("no-space",), "no-space"), (("  a",), "__a"), (("a  ",), "a__")], 'specific'
    if 'check palindrome ignoring case' in t:
        return [(("RaceCar",), True), (("Hello",), False), (("A",), True), (("",), True), (("AbBa",), True)], 'specific'
    if 'check palindrome ignoring spaces' in t:
        return [(("n u r s e s r u n",), True), (("never odd or even",), True), (("hello world",), False), (("a",), True), (("",), True)], 'specific'
    if 'count lines in multiline text' in t:
        return [(("a\\nb\\nc",), 3), (("",), 0), (("one line",), 1), (("\\n",), 2), (("x\\n",), 2)], 'specific'
    if 'replace tabs with spaces' in t:
        return [(("a\\tb",), "a b"), (("\\t",), " "), (("no tab",), "no tab"), (("a\\t\\tb",), "a  b"), (("",), "")], 'specific'
    if 'convert spaces to snake_case' in t:
        return [(("hello world",), "hello_world"), (("a b c",), "a_b_c"), (("",), ""), (("noSpace",), "noSpace"), (("  a",), "__a")], 'specific'
    if 'convert spaces to kebab-case' in t:
        return [(("hello world",), "hello-world"), (("a b c",), "a-b-c"), (("",), ""), (("noSpace",), "noSpace"), (("  a",), "--a")], 'specific'
    if 'compress repeated chars as char+count' in t:
        return [(("aaabb",), "a3b2"), (("a",), "a1"), (("",), ""), (("ab",), "a1b1"), (("xxxx",), "x4")], 'specific'
    if 'expand basic char+count text' in t:
        return [(("a3b2",), "aaabb"), (("x1",), "x"), (("",), ""), (("a1b1",), "ab"), (("z4",), "zzzz")], 'specific'

    # Numeric basics
    if t == 'add two integers':
        return [((2,3), 5), ((-1,1), 0), ((0,0), 0), ((7,-2), 5), ((-5,-6), -11)], 'specific'
    if t == 'subtract two integers':
        return [((5,3), 2), ((-1,1), -2), ((0,0), 0), ((7,-2), 9), ((-5,-6), 1)], 'specific'
    if t == 'multiply two integers':
        return [((2,3), 6), ((-1,1), -1), ((0,8), 0), ((7,-2), -14), ((-5,-6), 30)], 'specific'
    if 'check if number is even' in t:
        return [((2,), True), ((3,), False), ((0,), True), ((-4,), True), ((-5,), False)], 'specific'
    if 'check if number is odd' in t:
        return [((2,), False), ((3,), True), ((0,), False), ((-4,), False), ((-5,), True)], 'specific'
    if 'find absolute value of number' in t:
        return [((5,), 5), ((-5,), 5), ((0,), 0), ((-1,), 1), ((9,), 9)], 'specific'
    if 'check if year is leap year' in t:
        return [((2000,), True), ((1900,), False), ((2024,), True), ((2023,), False), ((2400,), True)], 'specific'
    if 'integer division quotient' in t:
        return [((7,3), 2), ((10,2), 5), ((5,7), 0), ((-7,3), -2), ((0,5), 0)], 'specific'
    if 'integer division remainder' in t:
        return [((7,3), 1), ((10,2), 0), ((5,7), 5), ((0,5), 0), ((9,4), 1)], 'specific'
    if 'check if number is positive' in t:
        return [((1,), True), ((0,), False), ((-1,), False), ((99,), True), ((-99,), False)], 'specific'
    if 'check if number is negative' in t:
        return [((1,), False), ((0,), False), ((-1,), True), ((99,), False), ((-99,), True)], 'specific'
    if 'check if number is zero' in t:
        return [((0,), True), ((1,), False), ((-1,), False), ((99,), False), ((-99,), False)], 'specific'
    if 'find larger of two numbers' in t:
        return [((2,3), 3), ((3,2), 3), ((-1,-2), -1), ((5,5), 5), ((0,-1), 0)], 'specific'
    if 'find smaller of two numbers' in t:
        return [((2,3), 2), ((3,2), 2), ((-1,-2), -2), ((5,5), 5), ((0,-1), -1)], 'specific'
    if 'find largest of three numbers' in t:
        return [((1,2,3), 3), ((3,2,1), 3), ((-1,-2,-3), -1), ((5,5,4), 5), ((0,0,0), 0)], 'specific'
    if 'find smallest of three numbers' in t:
        return [((1,2,3), 1), ((3,2,1), 1), ((-1,-2,-3), -3), ((5,5,4), 4), ((0,0,0), 0)], 'specific'
    if 'swap two numbers using temp variable' in t or 'swap two numbers without temp' in t:
        return [((2,3), (3,2)), ((-1,1), (1,-1)), ((0,0), (0,0)), ((5,-2), (-2,5)), ((9,9), (9,9))], 'specific'
    if 'calculate square of a number' in t:
        return [((3,), 9), ((0,), 0), ((-3,), 9), ((5,), 25), ((1,), 1)], 'specific'
    if 'calculate cube of a number' in t:
        return [((3,), 27), ((0,), 0), ((-3,), -27), ((5,), 125), ((1,), 1)], 'specific'
    if 'calculate power a^b using loop' in t:
        return [((2,3), 8), ((5,0), 1), ((3,1), 3), ((1,9), 1), ((10,2), 100)], 'specific'
    if 'calculate factorial of n' in t:
        return [((0,), 1), ((1,), 1), ((3,), 6), ((5,), 120), ((7,), 5040)], 'specific'
    if 'calculate sum from 1 to n' in t:
        return [((1,), 1), ((3,), 6), ((5,), 15), ((0,), 0), ((10,), 55)], 'specific'
    if 'calculate sum of even numbers from 1 to n' in t:
        return [((1,), 0), ((2,), 2), ((5,), 6), ((10,), 30), ((0,), 0)], 'specific'
    if 'calculate sum of odd numbers from 1 to n' in t:
        return [((1,), 1), ((2,), 1), ((5,), 9), ((10,), 25), ((0,), 0)], 'specific'
    if 'count digits in an integer' in t:
        return [((0,), 1), ((7,), 1), ((123,), 3), ((-456,), 3), ((1000,), 4)], 'specific'
    if 'reverse digits of an integer' in t:
        return [((123,), 321), ((-123,), -321), ((0,), 0), ((120,), 21), ((7,), 7)], 'specific'
    if 'sum digits of an integer' in t:
        return [((123,), 6), ((0,), 0), ((999,), 27), ((-123,), 6), ((1000,), 1)], 'specific'
    if 'product of digits of an integer' in t:
        return [((123,), 6), ((0,), 0), ((999,), 729), ((-123,), 6), ((1000,), 0)], 'specific'
    if 'find largest digit in an integer' in t:
        return [((123,), 3), ((0,), 0), ((907,), 9), ((-321,), 3), ((555,), 5)], 'specific'
    if 'find smallest digit in an integer' in t:
        return [((123,), 1), ((0,), 0), ((907,), 0), ((-321,), 1), ((555,), 5)], 'specific'
    if 'count even digits in an integer' in t:
        return [((1234,), 2), ((0,), 1), ((999,), 0), ((2468,), 4), ((-1203,), 2)], 'specific'
    if 'count odd digits in an integer' in t:
        return [((1234,), 2), ((0,), 0), ((999,), 3), ((2468,), 0), ((-1203,), 2)], 'specific'
    if 'check if integer is palindrome' in t:
        return [((121,), True), ((123,), False), ((0,), True), ((-121,), False), ((1221,), True)], 'specific'
    if 'remove last digit from integer' in t:
        return [((123,), 12), ((5,), 0), ((0,), 0), ((-123,), -12), ((10,), 1)], 'specific'
    if 'append digit to integer end' in t:
        return [((12,3), 123), ((0,5), 5), ((7,0), 70), ((-12,3), -123), ((9,9), 99)], 'specific'
    if 'check divisibility by 2' in t:
        return [((2,), True), ((3,), False), ((0,), True), ((-4,), True), ((-5,), False)], 'specific'
    if 'check divisibility by 3' in t:
        return [((3,), True), ((4,), False), ((0,), True), ((-6,), True), ((10,), False)], 'specific'
    if 'check divisibility by 5' in t:
        return [((5,), True), ((4,), False), ((0,), True), ((-10,), True), ((12,), False)], 'specific'
    if 'check divisibility by 9' in t:
        return [((9,), True), ((10,), False), ((0,), True), ((-18,), True), ((27,), True)], 'specific'
    if 'convert celsius to fahrenheit' in t:
        return [((0,), 32.0), ((100,), 212.0), ((-40,), -40.0), ((37,), 98.6), ((10,), 50.0)], 'specific'
    if 'convert fahrenheit to celsius' in t:
        return [((32,), 0.0), ((212,), 100.0), ((-40,), -40.0), ((98.6,), 37.0), ((50,), 10.0)], 'specific'
    if 'convert kilometers to miles' in t:
        return [((1,), 0.621371), ((0,), 0.0), ((5,), 3.106855), ((10,), 6.21371), ((2.5,), 1.5534275)], 'specific'
    if 'convert miles to kilometers' in t:
        return [((1,), 1.60934), ((0,), 0.0), ((5,), 8.0467), ((10,), 16.0934), ((2.5,), 4.02335)], 'specific'
    if 'calculate simple interest' in t:
        return [((1000,5,2), 100.0), ((500,10,1), 50.0), ((100,0,5), 0.0), ((2000,3,3), 180.0), ((100,5,0), 0.0)], 'specific'
    if 'calculate total marks from 5 subjects' in t:
        return [(([10,20,30,40,50],), 150), (([0,0,0,0,0],), 0), (([100,100,100,100,100],), 500), (([50,50,50,50,50],), 250), (([1,2,3,4,5],), 15)], 'specific'
    if 'calculate percentage from marks' in t:
        return [((450,500), 90.0), ((0,500), 0.0), ((250,500), 50.0), ((500,500), 100.0), ((125,250), 50.0)], 'specific'
    if 'calculate average of n numbers' in t:
        return [(([1,2,3],), 2.0), (([5],), 5.0), (([0,0],), 0.0), (([-1,1],), 0.0), (([2,4],), 3.0)], 'specific'
    if 'round number down to nearest integer' in t:
        return [((2.9,), 2), ((2.0,), 2), ((-2.1,), -3), ((0.0,), 0), ((-0.1,), -1)], 'specific'
    if 'round number up to nearest integer' in t:
        return [((2.1,), 3), ((2.0,), 2), ((-2.9,), -2), ((0.0,), 0), ((-0.1,), 0)], 'specific'
    if 'find floor and ceil of a decimal number' in t:
        return [((2.3,), (2,3)), ((2.0,), (2,2)), ((-2.3,), (-3,-2)), ((0.0,), (0,0)), ((-0.1,), (-1,0))], 'specific'
    if 'generate multiplication table of n (1 to 10)' in t:
        return [((2,), [2,4,6,8,10,12,14,16,18,20]), ((1,), [1,2,3,4,5,6,7,8,9,10]), ((0,), [0,0,0,0,0,0,0,0,0,0]), ((3,), [3,6,9,12,15,18,21,24,27,30]), ((5,), [5,10,15,20,25,30,35,40,45,50])], 'specific'
    if 'print numbers from 1 to n' in t:
        return [((1,), [1]), ((3,), [1,2,3]), ((0,), []), ((5,), [1,2,3,4,5]), ((2,), [1,2])], 'specific'
    if 'print numbers from n to 1' in t:
        return [((1,), [1]), ((3,), [3,2,1]), ((0,), []), ((5,), [5,4,3,2,1]), ((2,), [2,1])], 'specific'
    if 'print all even numbers from 1 to n' in t:
        return [((1,), []), ((2,), [2]), ((5,), [2,4]), ((10,), [2,4,6,8,10]), ((0,), [])], 'specific'
    if 'print all odd numbers from 1 to n' in t:
        return [((1,), [1]), ((2,), [1]), ((5,), [1,3,5]), ((10,), [1,3,5,7,9]), ((0,), [])], 'specific'
    if 'count multiples of k from 1 to n' in t:
        return [((10,2), 5), ((10,3), 3), ((5,7), 0), ((0,2), 0), ((12,4), 3)], 'specific'
    if 'sum multiples of k from 1 to n' in t:
        return [((10,2), 30), ((10,3), 18), ((5,7), 0), ((0,2), 0), ((12,4), 24)], 'specific'
    if 'find gcd of two numbers (basic loop)' in t:
        return [((54,24), 6), ((10,5), 5), ((7,3), 1), ((0,5), 5), ((18,27), 9)], 'specific'
    if 'find lcm of two numbers (using gcd)' in t:
        return [((4,6), 12), ((10,5), 10), ((7,3), 21), ((0,5), 0), ((18,27), 54)], 'specific'
    if 'check if number is prime (simple trial division)' in t:
        return [((2,), True), ((3,), True), ((4,), False), ((1,), False), ((17,), True)], 'specific'
    if 'list all factors of a number' in t:
        return [((1,), [1]), ((6,), [1,2,3,6]), ((10,), [1,2,5,10]), ((13,), [1,13]), ((12,), [1,2,3,4,6,12])], 'specific'
    if 'count factors of a number' in t:
        return [((1,), 1), ((6,), 4), ((10,), 4), ((13,), 2), ((12,), 6)], 'specific'
    if 'check if number is perfect square' in t:
        return [((1,), True), ((4,), True), ((5,), False), ((0,), True), ((49,), True)], 'specific'
    if 'check if number is power of 2' in t:
        return [((1,), True), ((2,), True), ((3,), False), ((16,), True), ((0,), False)], 'specific'

    # Matrix basics
    if 'sum all elements in matrix' in t:
        return [(([[1,2],[3,4]],), 10), (([[]],), 0), (([[0]],), 0), (([[1,-1],[2,-2]],), 0), (([[5]],), 5)], 'specific'
    if 'transpose a matrix' in t:
        return [(([[1,2,3],[4,5,6]],), [[1,4],[2,5],[3,6]]), (([[1]],), [[1]]), (([[1,2]],), [[1],[2]]), (([[1],[2]],), [[1,2]]), (([[1,2],[3,4]],), [[1,3],[2,4]])], 'specific'
    if 'add two matrices' in t:
        return [(([[1,2],[3,4]], [[5,6],[7,8]]), [[6,8],[10,12]]), (([[0]], [[0]]), [[0]]), (([[1]], [[2]]), [[3]]), (([[1,1]], [[2,2]]), [[3,3]]), (([[1],[2]], [[3],[4]]), [[4],[6]])], 'specific'
    if 'sum main diagonal elements' in t:
        return [(([[1,2],[3,4]],), 5), (([[5]],), 5), (([[1,0,0],[0,2,0],[0,0,3]],), 6), (([[0,1],[2,0]],), 0), (([[2,2],[2,2]],), 4)], 'specific'
    if 'sum secondary diagonal elements' in t:
        return [(([[1,2],[3,4]],), 5), (([[5]],), 5), (([[1,0,3],[0,2,0],[7,0,9]],), 12), (([[0,1],[2,0]],), 3), (([[2,2],[2,2]],), 4)], 'specific'
    if 'subtract two matrices' in t:
        return [(([[5,6],[7,8]], [[1,2],[3,4]]), [[4,4],[4,4]]), (([[0]], [[0]]), [[0]]), (([[1]], [[2]]), [[-1]]), (([[2,2]], [[1,1]]), [[1,1]]), (([[3],[4]], [[1],[2]]), [[2],[2]])], 'specific'
    if 'print all elements of a 2d matrix' in t:
        return [(([[1,2],[3,4]],), [1,2,3,4]), (([[1]],), [1]), (([[]],), []), (([[1,2,3]],), [1,2,3]), (([[1],[2]],), [1,2])], 'specific'
    if 'find number of rows in a matrix' in t:
        return [(([[1,2],[3,4]],), 2), (([[1]],), 1), (([[]],), 1), (([],), 0), (([[1],[2],[3]],), 3)], 'specific'
    if 'find number of columns in a matrix' in t:
        return [(([[1,2],[3,4]],), 2), (([[1]],), 1), (([[]],), 0), (([],), 0), (([[1,2,3]],), 3)], 'specific'
    if 'find max element in matrix' in t:
        return [(([[1,2],[3,4]],), 4), (([[1]],), 1), (([[0,-1]],), 0), (([[5,5],[5,5]],), 5), (([[-3,-2],[-1,-4]],), -1)], 'specific'
    if 'find min element in matrix' in t:
        return [(([[1,2],[3,4]],), 1), (([[1]],), 1), (([[0,-1]],), -1), (([[5,5],[5,5]],), 5), (([[-3,-2],[-1,-4]],), -4)], 'specific'
    if 'print main diagonal of square matrix' in t:
        return [(([[1,2],[3,4]],), [1,4]), (([[5]],), [5]), (([[1,0,0],[0,2,0],[0,0,3]],), [1,2,3]), (([[0,1],[2,0]],), [0,0]), (([[2,2],[2,2]],), [2,2])], 'specific'
    if 'print secondary diagonal of square matrix' in t:
        return [(([[1,2],[3,4]],), [2,3]), (([[5]],), [5]), (([[1,0,3],[0,2,0],[7,0,9]],), [3,2,7]), (([[0,1],[2,0]],), [1,2]), (([[2,2],[2,2]],), [2,2])], 'specific'
    if 'multiply matrix by scalar value' in t:
        return [(([[1,2],[3,4]],2), [[2,4],[6,8]]), (([[1]],0), [[0]]), (([[1,-1]],3), [[3,-3]]), (([[]],5), [[]]), (([[2],[3]],2), [[4],[6]])], 'specific'
    if 'check if matrix is symmetric' in t:
        return [(([[1,2],[2,1]],), True), (([[1,0],[2,1]],), False), (([[1]],), True), (([[1,2,3],[2,4,5],[3,5,6]],), True), (([[1,2],[2,3]],), False)], 'specific'
    if 'flatten matrix into a list' in t:
        return [(([[1,2],[3,4]],), [1,2,3,4]), (([[1]],), [1]), (([[]],), []), (([[1,2,3]],), [1,2,3]), (([[1],[2]],), [1,2])], 'specific'
    if 'replace all negative matrix values with 0' in t:
        return [(([[1,-2],[-3,4]],), [[1,0],[0,4]]), (([[1]],), [[1]]), (([[-1]],), [[0]]), (([[]],), [[]]), (([[0,-1]],), [[0,0]])], 'specific'

    # Remaining list/string utility titles
    if 'create list of first n natural numbers' in t:
        return [((5,), [1,2,3,4,5]), ((1,), [1]), ((0,), []), ((3,), [1,2,3]), ((2,), [1,2])], 'specific'
    if 'create list of first n odd numbers' in t:
        return [((5,), [1,3,5,7,9]), ((1,), [1]), ((0,), []), ((3,), [1,3,5]), ((2,), [1,3])], 'specific'
    if 'create list of first n even numbers' in t:
        return [((5,), [2,4,6,8,10]), ((1,), [2]), ((0,), []), ((3,), [2,4,6]), ((2,), [2,4])], 'specific'
    if 'create a list of n zeros' in t:
        return [((5,), [0,0,0,0,0]), ((1,), [0]), ((0,), []), ((3,), [0,0,0]), ((2,), [0,0])], 'specific'
    if 'create a list of n ones' in t:
        return [((5,), [1,1,1,1,1]), ((1,), [1]), ((0,), []), ((3,), [1,1,1]), ((2,), [1,1])], 'specific'
    if 'split list into positives and negatives' in t:
        return [(([-1,2,-3,4],), ([2,4],[-1,-3])), (([],), ([],[])), (([1,2],), ([1,2],[])), (([-1,-2],), ([],[-1,-2])), (([0,1,-1],), ([1],[-1]))], 'specific'
    if 'split list into evens and odds' in t:
        return [(([1,2,3,4],), ([2,4],[1,3])), (([],), ([],[])), (([2,4],), ([2,4],[])), (([1,3],), ([],[1,3])), (([0,1],), ([0],[1]))], 'specific'
    if 'interleave two equal-length lists' in t:
        return [(([1,2],[3,4]), [1,3,2,4]), (([],[]), []), (([1],[2]), [1,2]), ((['a','b'],['x','y']), ['a','x','b','y']), (([1,1],[2,2]), [1,2,1,2])], 'specific'
    if 'take first half of a list' in t:
        return [(([1,2,3,4],), [1,2]), (([1,2,3],), [1]), (([],), []), (([1],), []), (([1,2],), [1])], 'specific'
    if 'take second half of a list' in t:
        return [(([1,2,3,4],), [3,4]), (([1,2,3],), [2,3]), (([],), []), (([1],), [1]), (([1,2],), [2])], 'specific'
    if 'add two same-length lists element-wise' in t:
        return [(([1,2],[3,4]), [4,6]), (([],[]), []), (([1],[2]), [3]), (([0,0],[0,0]), [0,0]), (([-1,1],[1,-1]), [0,0])], 'specific'
    if 'subtract two same-length lists element-wise' in t:
        return [(([1,2],[3,4]), [-2,-2]), (([],[]), []), (([1],[2]), [-1]), (([0,0],[0,0]), [0,0]), (([-1,1],[1,-1]), [-2,2])], 'specific'
    if 'multiply two same-length lists element-wise' in t:
        return [(([1,2],[3,4]), [3,8]), (([],[]), []), (([1],[2]), [2]), (([0,0],[0,0]), [0,0]), (([-1,1],[1,-1]), [-1,-1])], 'specific'
    if 'build frequency map of list values' in t:
        return [(([1,2,2,3],), {1:1,2:2,3:1}), (([],), {}), (([1,1,1],), {1:3}), ((['a','b','a'],), {'a':2,'b':1}), (([0],), {0:1})], 'specific'
    if 'print list without duplicates' in t:
        return [(([1,2,2,3,1],), [1,2,3]), (([],), []), (([1,1,1],), [1]), ((['a','b','a'],), ['a','b']), (([0],), [0])], 'specific'
    if 'get common elements of two lists' in t:
        return [(([1,2,3],[2,3,4]), [2,3]), (([],[1]), []), (([1],[]), []), (([1,1],[1,2]), [1]), ((['a','b'],['b','c']), ['b'])], 'specific'
    if 'get elements in list a not in list b' in t:
        return [(([1,2,3],[2,4]), [1,3]), (([],[1]), []), (([1],[]), [1]), (([1,1,2],[1]), [2]), ((['a','b'],['b']), ['a'])], 'specific'
    if 'get elements in list b not in list a' in t:
        return [(([1,2,3],[2,4]), [4]), (([],[1]), [1]), (([1],[]), []), (([1],[1,2]), [2]), ((['a','b'],['b','c']), ['c'])], 'specific'
    if 'convert a tuple to a list' in t:
        return [(((1,2,3),), [1,2,3]), (((),), []), (((5,),), [5]), ((('a','b'),), ['a','b']), (((0,0),), [0,0])], 'specific'
    if 'print each character of a string' in t:
        return [(("abc",), ['a','b','c']), (("",), []), (("a",), ['a']), (("Hi",), ['H','i']), (("12",), ['1','2'])], 'specific'
    if 'find string length' in t:
        return [(("abc",), 3), (("",), 0), (("a",), 1), (("hello world",), 11), (("12",), 2)], 'specific'
    if 'get first character of a string' in t:
        return [(("abc",), 'a'), (("a",), 'a'), (("Hi",), 'H'), (("12",), '1'), ((" z",), ' ')], 'specific'
    if 'get last character of a string' in t:
        return [(("abc",), 'c'), (("a",), 'a'), (("Hi",), 'i'), (("12",), '2'), (("z ",), ' ')], 'specific'
    if 'toggle case of each character' in t:
        return [(("AbC",), "aBc"), (("hello",), "HELLO"), (("HELLO",), "hello"), (("",), ""), (("a1B",), "A1b")], 'specific'
    if 'find first occurrence of a character' in t:
        return [(("banana",'a'), 1), (("abc",'d'), -1), (("",'a'), -1), (("aaa",'a'), 0), (("test",'t'), 0)], 'specific'
    if 'find last occurrence of a character' in t:
        return [(("banana",'a'), 5), (("abc",'d'), -1), (("",'a'), -1), (("aaa",'a'), 2), (("test",'t'), 3)], 'specific'
    if 'find substring index' in t:
        return [(("hello world","world"), 6), (("abc","d"), -1), (("aaaa","aa"), 0), (("","a"), -1), (("abc",""), 0)], 'specific'
    if 'split sentence into words' in t:
        return [(("a b c",), ["a","b","c"]), (("",), []), (("one",), ["one"]), (("  hi there ",), ["hi","there"]), (("x  y",), ["x","y"])], 'specific'
    if 'join words with spaces' in t:
        return [((["a","b","c"],), "a b c"), (([],), ""), ((["one"],), "one"), ((["hi","there"],), "hi there"), ((["x","y"],), "x y")], 'specific'
    if 'join words with commas' in t:
        return [((["a","b","c"],), "a,b,c"), (([],), ""), ((["one"],), "one"), ((["hi","there"],), "hi,there"), ((["x","y"],), "x,y")], 'specific'
    if 'find longest word in sentence' in t:
        return [(("a bb ccc",), "ccc"), (("",), ""), (("one",), "one"), (("hi there friend",), "friend"), (("to be or not",), "not")], 'specific'
    if 'find shortest word in sentence' in t:
        return [(("a bb ccc",), "a"), (("",), ""), (("one",), "one"), (("hi there friend",), "hi"), (("to be or not",), "to")], 'specific'
    if 'capitalize first letter of a string' in t:
        return [(("hello",), "Hello"), (("",), ""), (("h",), "H"), (("Hello",), "Hello"), (("123abc",), "123abc")], 'specific'
    if 'capitalize first letter of each word' in t:
        return [(("hello world",), "Hello World"), (("",), ""), (("a b c",), "A B C"), (("hi there",), "Hi There"), (("123 abc",), "123 Abc")], 'specific'
    if 'lowercase first letter of each word' in t:
        return [(("Hello World",), "hello world"), (("",), ""), (("A B C",), "a b c"), (("hi there",), "hi there"), (("123 Abc",), "123 abc")], 'specific'
    if 'compare two strings lexicographically' in t:
        return [(("abc","abd"), -1), (("abd","abc"), 1), (("abc","abc"), 0), (("","a"), -1), (("a",""), 1)], 'specific'
    if 'sort characters of a string' in t:
        return [(("cba",), "abc"), (("",), ""), (("a",), "a"), (("bca",), "abc"), (("321",), "123")], 'specific'
    if 'keep only first occurrence of each character' in t:
        return [(("banana",), "ban"), (("",), ""), (("aaaa",), "a"), (("abc",), "abc"), (("aabbcc",), "abc")], 'specific'
    if 'keep only last occurrence of each character' in t:
        return [(("banana",), "bna"), (("",), ""), (("aaaa",), "a"), (("abc",), "abc"), (("aabbcc",), "abc")], 'specific'
    if 'find first non-repeating character' in t:
        return [(("swiss",), "w"), (("aabb",), None), (("",), None), (("abc",), "a"), (("aabc",), "b")], 'specific'
    if 'find first repeating character' in t:
        return [(("swiss",), "s"), (("abc",), None), (("",), None), (("aabc",), "a"), (("abca",), "a")], 'specific'
    if 'print all indices of a character in string' in t:
        return [(("banana",'a'), [1,3,5]), (("abc",'d'), []), (("",'a'), []), (("aaa",'a'), [0,1,2]), (("test",'t'), [0,3])], 'specific'
    if 'keep only alphabetic characters' in t:
        return [(("a1b2!",), "ab"), (("",), ""), (("ABC",), "ABC"), (("123",), ""), (("a b",), "ab")], 'specific'
    if 'keep only numeric characters' in t:
        return [(("a1b2!",), "12"), (("",), ""), (("ABC",), ""), (("123",), "123"), (("a b",), "")], 'specific'
    if 'keep only alphanumeric characters' in t:
        return [(("a1b2!",), "a1b2"), (("",), ""), (("ABC",), "ABC"), (("123",), "123"), (("a b",), "ab")], 'specific'
    if 'pad string on left with zeros to length n' in t:
        return [(("42",5), "00042"), (("123",3), "123"), (("",2), "00"), (("a",1), "a"), (("7",4), "0007")], 'specific'
    if 'pad string on right with dots to length n' in t:
        return [(("42",5), "42..."), (("123",3), "123"), (("",2), ".."), (("a",1), "a"), (("7",4), "7...")], 'specific'
    if 'repeat a string n times' in t:
        return [(("ab",3), "ababab"), (("x",1), "x"), (("",5), ""), (("a",0), ""), (("hi",2), "hihi")], 'specific'
    if 'duplicate every character in string' in t:
        return [(("ab",), "aabb"), (("",), ""), (("a",), "aa"), (("Hi",), "HHii"), (("12",), "1122")], 'specific'
    if 'keep every second character' in t:
        return [(("abcdef",), "ace"), (("",), ""), (("a",), "a"), (("ab",), "a"), (("12345",), "135")], 'specific'
    if 'rotate string left by 1' in t:
        return [(("abc",), "bca"), (("a",), "a"), (("",), ""), (("ab",), "ba"), (("hello",), "elloh")], 'specific'
    if 'rotate string right by 1' in t:
        return [(("abc",), "cab"), (("a",), "a"), (("",), ""), (("ab",), "ba"), (("hello",), "ohell")], 'specific'
    if 'rotate string left by k' in t:
        return [(("abc",1), "bca"), (("abc",2), "cab"), (("a",5), "a"), (("",3), ""), (("hello",2), "llohe")], 'specific'
    if 'rotate string right by k' in t:
        return [(("abc",1), "cab"), (("abc",2), "bca"), (("a",5), "a"), (("",3), ""), (("hello",2), "lohel")], 'specific'
    if 'find smallest character in string' in t:
        return [(("bca",), "a"), (("a",), "a"), (("zyx",), "x"), (("112",), "1"), (("Ba",), "B")], 'specific'
    if 'find largest character in string' in t:
        return [(("bca",), "c"), (("a",), "a"), (("zyx",), "z"), (("112",), "2"), (("Ba",), "a")], 'specific'
    if 'mask all but last 4 characters of a string' in t:
        return [(("12345678",), "****5678"), (("1234",), "1234"), (("12",), "12"), (("",), ""), (("abcdef",), "**cdef")], 'specific'
    if 'keep only vowels from a string' in t:
        return [(("alphabet",), "aae"), (("xyz",), ""), (("",), ""), (("AEIOU",), "AEIOU"), (("hello",), "eo")], 'specific'
    if 'alternate uppercase/lowercase characters' in t:
        return [(("abcdef",), "AbCdEf"), (("a",), "A"), (("",), ""), (("AB",), "Ab"), (("hello",), "HeLlO")], 'specific'
    if 'find longest run of same character' in t:
        return [(("aaabbc",), 3), (("",), 0), (("a",), 1), (("abbbcccc",), 4), (("abc",), 1)], 'specific'
    if 'find common characters between two strings' in t:
        return [(("abc","bcd"), "bc"), (("abc","xyz"), ""), (("","abc"), ""), (("aabb","ab"), "ab"), (("hello","yellow"), "ello")], 'specific'

    # Generic heuristic rules (still title-aware)
    if any(k in t for k in ['string','sentence','word','character']):
        if t.startswith('count '):
            return [(("abc",), 3), (("",), 0), (("a a",), 3), (("123",), 3), (("Hello",), 5)], 'string_heuristic'
        if t.startswith('check ') or 'is ' in t:
            return [(("abba",), True), (("abc",), False), (("",), True), (("a",), True), (("ab",), False)], 'string_heuristic'
        if 'reverse' in t:
            return [(("hello",), "olleh"), (("",), ""), (("a",), "a"), (("ab",), "ba"), (("racecar",), "racecar")], 'string_heuristic'
        if 'remove' in t:
            return [(("a b c",), "abc"), (("",), ""), (("hello",), "hello"), (("a a",), "aa"), (("  x",), "x")], 'string_heuristic'
        if 'replace' in t:
            return [(("a b",), "a_b"), (("",), ""), (("abc",), "abc"), (("a  b",), "a__b"), ((" x ",), "_x_")], 'string_heuristic'
        if 'convert' in t:
            return [(("AbC",), "abc"), (("HELLO",), "hello"), (("",), ""), (("123",), "123"), (("Hi",), "hi")], 'string_heuristic'
        return [(("hello",), "hello"), (("",), ""), (("a",), "a"), (("abc123",), "abc123"), (("Hi There",), "Hi There")], 'string_fallback'

    if any(k in t for k in ['list','array']):
        if t.startswith('count '):
            return [(([1,2,2,3],), 4), (([],), 0), (([1],), 1), (([0,0],), 2), (([-1,1],), 2)], 'list_heuristic'
        if t.startswith('check '):
            return [(([1,2,3],), True), (([],), True), (([1],), True), (([1,1],), True), (([2,1],), False)], 'list_heuristic'
        if 'reverse' in t:
            return [(([1,2,3],), [3,2,1]), (([],), []), (([1],), [1]), ((['a','b'],), ['b','a']), (([0,0],), [0,0])], 'list_heuristic'
        if 'sort' in t:
            return [(([3,1,2],), [1,2,3]), (([],), []), (([1],), [1]), (([2,2,1],), [1,2,2]), (([-1,3,0],), [-1,0,3])], 'list_heuristic'
        if 'rotate' in t:
            return [(([1,2,3],1), [2,3,1]), (([],1), []), (([1],1), [1]), (([1,2],2), [1,2]), (([1,2,3],2), [3,1,2])], 'list_heuristic'
        if 'move' in t:
            return [(([0,1,0,2],), [1,2,0,0]), (([],), []), (([0,0],), [0,0]), (([1,2],), [1,2]), (([0,1],), [1,0])], 'list_heuristic'
        if 'sum' in t:
            return [(([1,2,3],), 6), (([],), 0), (([1],), 1), (([0,0],), 0), (([-1,1],), 0)], 'list_heuristic'
        return [(([1,2,3],), [1,2,3]), (([],), []), (([0],), [0]), (([-1,1],), [-1,1]), (([2,2],), [2,2])], 'list_fallback'

    if 'matrix' in t:
        if t.startswith('count '):
            return [(([[0,1],[0,0]],), 3), (([[1]],), 0), (([[]],), 0), (([[0]],), 1), (([[1,1],[1,1]],), 0)], 'matrix_heuristic'
        if 'sum' in t:
            return [(([[1,2],[3,4]],), 10), (([[0]],), 0), (([[]],), 0), (([[5]],), 5), (([[1,-1]],), 0)], 'matrix_heuristic'
        if 'transpose' in t:
            return [(([[1,2],[3,4]],), [[1,3],[2,4]]), (([[1]],), [[1]]), (([[1,2]],), [[1],[2]]), (([[1],[2]],), [[1,2]]), (([[]],), [[]])], 'matrix_heuristic'
        return [(([[1,2],[3,4]],), [[1,2],[3,4]]), (([[0]],), [[0]]), (([[]],), [[]]), (([[1]],), [[1]]), (([[1,-1]],), [[1,-1]])], 'matrix_fallback'

    # Pattern fallbacks by domain
    return [((5,), 5), ((0,), 0), ((-1,), -1), ((10,), 10), ((1,), 1)], 'numeric_fallback'


def write_file(path: Path, title: str, difficulty: str, tests):
    lines = [
        f'# Title: {title}',
        f'# Difficulty: {difficulty}',
        '#',
        '# Description:',
    ]
    for d in description(title):
        lines.append(f'# {d}')
    lines += [
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
        lines.append(f'        ({repr(args)}, {repr(expected)}),')

    lines += [
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

    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    files = sorted(DIR.glob('[0-9][0-9][0-9]_*.py'))
    buckets = {}
    for f in files:
        txt = f.read_text(encoding='utf-8')
        title = txt.splitlines()[0].replace('# Title: ','').strip()
        difficulty = txt.splitlines()[1].replace('# Difficulty: ','').strip()
        tests, bucket = tests_for(title)
        buckets[bucket] = buckets.get(bucket, 0) + 1
        write_file(f, title, difficulty, tests)

    print('updated', len(files))
    for k in sorted(buckets):
        print(k, buckets[k])


if __name__ == '__main__':
    main()
