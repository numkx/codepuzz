#!/usr/bin/env python3
"""Regenerate concise, concrete descriptions for easy/medium/hard challenges."""

from pathlib import Path
import argparse
import re

BASE = Path("/Users/numky/Code/codepuzz")
DEFAULT_TARGET_DIRS = ["02_easy", "03_medium", "04_hard"]


def normalize(title: str) -> str:
    t = title.lower()
    t = re.sub(r"\s*\([^)]*\)\s*", " ", t)
    t = t.replace("variant", " ")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def input_clause(t: str) -> str:
    if any(k in t for k in ["matrix", "grid", "board", "sudoku", "spiral"]):
        return "Given a 2D grid/matrix and any required parameters,"
    if any(k in t for k in ["tree", "bst", "binary tree"]):
        return "Given a binary tree and any required parameters,"
    if any(k in t for k in ["linked list", "node", "nodes"]):
        return "Given a linked list and any required parameters,"
    if any(k in t for k in ["interval", "meeting"]):
        return "Given a list of intervals and any required parameters,"
    if any(k in t for k in ["string", "substring", "anagram", "palindrome", "word", "roman", "parentheses"]):
        return "Given a string (or strings) and any required parameters,"
    if any(k in t for k in ["graph", "course", "islands", "paths", "components"]):
        return "Given graph-style input and any required parameters,"
    if any(k in t for k in ["array", "subarray", "sum", "permutation", "combination"]):
        return "Given an array/list and any required parameters,"
    return "Given the provided input,"


def goal_clause(t: str) -> str:
    special = {
        "add two numbers": "add the represented numbers and build the resulting number format",
        "longest substring without repeating characters": "find the length of the longest substring without repeated characters",
        "container with most water": "find the maximum area that can be formed by two boundaries",
        "integer to roman": "convert the integer to its Roman numeral representation",
        "roman to integer": "convert the Roman numeral to its integer value",
        "3sum": "find all unique triplets that sum to zero",
        "3sum closest": "find the triplet sum closest to the target value",
        "4sum": "find all unique quadruplets that sum to the target value",
        "remove nth node from end of list": "remove the nth node from the end of the list",
        "generate parentheses": "generate all valid combinations of parentheses",
        "merge k sorted lists": "merge all sorted lists into one sorted list",
        "reverse nodes in k group": "reverse list nodes in groups of size k",
        "divide two integers": "compute integer division without using built-in division operators",
        "next permutation": "transform the sequence into the next lexicographically greater permutation",
        "longest valid parentheses": "find the length of the longest valid parentheses substring",
        "search in rotated sorted array": "find the target index in the rotated sorted array",
        "valid sudoku": "verify whether the Sudoku board configuration is valid",
        "combination sum": "find all combinations that reach the target sum",
        "first missing positive": "find the smallest missing positive integer",
        "trapping rain water": "compute the total amount of trapped rain water",
        "multiply strings": "multiply the numeric strings and return the product as a string",
        "task scheduler": "find the minimum intervals needed to finish all tasks with cooldown",
        "jump game ii": "find the minimum number of jumps to reach the last index",
        "rotate image": "rotate the square matrix by 90 degrees",
        "group anagrams": "group strings that are anagrams of each other",
        "pow x n": "compute x raised to the power n",
        "maximum subarray": "find the maximum possible subarray sum",
        "merge intervals": "merge all overlapping intervals",
        "insert interval": "insert the new interval and merge overlaps",
        "minimum window substring": "find the shortest substring that contains all required characters",
        "word search": "determine whether the target word exists in the board",
        "largest rectangle in histogram": "find the largest rectangle area in the histogram",
        "maximal rectangle": "find the largest rectangle containing only 1s in the matrix",
        "scramble string": "check whether one string is a scramble of the other",
        "decode ways": "count how many valid decodings are possible",
        "best time to buy and sell stock iii": "find the maximum profit with at most two transactions",
        "binary tree maximum path sum": "find the maximum path sum in the binary tree",
        "word ladder": "find the shortest transformation sequence length",
        "word ladder ii": "find all shortest transformation sequences",
        "lru cache": "support cache operations with least-recently-used eviction",
        "pascal triangle": "generate Pascal's Triangle for the requested number of rows",
        "pascal triangle ii": "return the requested row from Pascal's Triangle",
        "lemonade change": "determine whether you can provide correct change to each customer in order",
        "fraction to recurring decimal": "convert the fraction to a decimal string, wrapping repeating digits in parentheses",
        "surrounded regions": "capture all regions fully surrounded by X in the board",
        "evaluate division": "evaluate query ratios using the given equation relationships",
        "sort colors": "sort the array containing 0, 1, and 2 in-place",
        "gray code": "generate a valid gray code sequence of length 2^n",
        "majority element ii": "find all values that appear more than n/3 times",
        "integer replacement": "find the minimum number of replacements needed to reduce n to 1",
        "subsets ii": "return all unique subsets when the input may contain duplicates",
        "asteroid collision": "simulate collisions and return the final state of asteroids",
        "triangle": "find the minimum path sum from top to bottom in the triangle",
        "number of recent calls": "return the number of recent requests in the last 3000 milliseconds",
        "basic calculator ii": "evaluate the expression containing +, -, *, and / with integer truncation",
        "nth digit": "find the nth digit in the infinite integer sequence",
        "missing number": "find the single missing value from the expected range",
        "counting bits": "return bit counts for every number from 0 to n",
        "valid number": "determine whether the string represents a valid numeric value",
        "gas station": "find the starting station index that allows completing the circuit",
        "candy": "find the minimum candies needed to satisfy rating rules",
        "edit distance": "compute the minimum operations to convert one string into the other",
        "range bitwise and": "compute the bitwise AND for all numbers in the inclusive range",
        "simplify path": "simplify the absolute Unix path to its canonical form",
        "largest number": "arrange numbers to form the largest possible concatenated value",
        "repeated dna sequences": "find all 10-letter-long DNA sequences that occur more than once",
        "house robber iii": "find the maximum amount that can be robbed without robbing directly-linked houses",
        "minimum genetic mutation": "find the minimum mutations needed to reach the target gene",
        "maximum population year": "find the earliest year with the highest population",
        "verify an alien dictionary": "check whether words are sorted using the custom alien alphabet",
        "implement stack using queues": "implement stack behavior using queue operations",
        "insert delete getrandom o1": "support insert, delete, and random retrieval in average O(1) time",
        "insert delete getrandom o1 duplicates allowed": "support insert, delete, and random retrieval in average O(1) time with duplicates",
        "random pick index": "return a random index for the target value with equal probability",
        "fizz buzz": "generate the fizz-buzz sequence for numbers from 1 to n",
        "arithmetic slices": "count contiguous subarrays that form arithmetic sequences",
        "longest palindromic subsequence": "find the length of the longest palindromic subsequence",
    }
    for key, sentence in special.items():
        if key in t:
            return sentence

    for prefix in [
        "find ",
        "count ",
        "return ",
        "check ",
        "determine ",
        "evaluate ",
        "implement ",
        "design ",
        "generate ",
        "partition ",
        "search ",
        "decode ",
        "encode ",
        "build ",
        "compute ",
        "calculate ",
        "add ",
        "reverse ",
        "rotate ",
        "sort ",
        "remove ",
        "insert ",
        "merge ",
        "convert ",
    ]:
        if t.startswith(prefix):
            return t

    if t.startswith("number of "):
        return f"find the {t}"
    if t.startswith("minimum "):
        return f"find the {t}"
    if t.startswith("maximum "):
        return f"find the {t}"
    if t.startswith("longest "):
        return f"find the {t}"
    if t.startswith("shortest "):
        return f"find the {t}"
    if t.startswith("largest "):
        return f"find the {t}"
    if t.startswith("smallest "):
        return f"find the {t}"

    if any(k in t for k in ["valid", "is ", "can ", "contains", "equal", "palindrome", "anagram"]):
        return "check whether the condition is satisfied"

    if any(k in t for k in ["path", "paths"]):
        return "compute the required path-based result"
    if any(k in t for k in ["tree", "bst"]):
        return "perform the required tree operation"
    if any(k in t for k in ["linked list", "list node", "cycle"]):
        return "perform the required linked-list operation"
    if any(k in t for k in ["stack", "queue", "cache", "design"]):
        return "implement the required data-structure behavior"
    if any(k in t for k in ["array", "subarray", "subset", "permutation", "combination"]):
        return "perform the required array/list operation"
    if any(k in t for k in ["string", "substring", "word", "roman"]):
        return "perform the required string operation"
    if any(k in t for k in ["matrix", "grid", "board"]):
        return "perform the required matrix/grid operation"
    if any(k in t for k in ["graph", "course", "island"]):
        return "perform the required graph traversal or connectivity operation"

    return "apply the required algorithm for this problem"


def output_clause(t: str) -> str:
    if any(k in t for k in ["valid", "is ", "can ", "contains", "equal", "palindrome", "anagram", "possible"]):
        return "Return True when the condition holds; otherwise return False."
    if any(k in t for k in ["list", "lists", "array", "arrays", "group", "groups", "permutation", "combination", "interval"]):
        return "Return the resulting list/collection."
    if any(k in t for k in ["string", "roman", "word", "substring", "decode", "encode"]):
        return "Return the resulting string."
    return "Return the computed result."


def description_lines(title: str) -> list[str]:
    t = normalize(title)
    return [f"{input_clause(t)} {goal_clause(t)}.", output_clause(t)]


def rewrite_description(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^# Title:\s*(.+)$", text, flags=re.M)
    if not m:
        return False
    title = m.group(1).strip()

    block = "# Description:\n" + "\n".join(f"# {line}" for line in description_lines(title)) + "\n#\n"

    pattern = re.compile(r"# Description:\n(?:#.*\n)*?#\n(?=\ndef solve\()", flags=re.M)
    if not pattern.search(text):
        return False

    updated = pattern.sub(block, text, count=1)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dirs",
        nargs="+",
        default=DEFAULT_TARGET_DIRS,
        help="difficulty folders to update (e.g. 04_hard)",
    )
    args = parser.parse_args()

    total = 0
    for d in args.dirs:
        changed = 0
        for f in sorted((BASE / d).glob("[0-9][0-9][0-9]_*.py")):
            if rewrite_description(f):
                changed += 1
        total += changed
        print(f"{d}: updated {changed} files")
    print(f"Total updated: {total}")


if __name__ == "__main__":
    main()
