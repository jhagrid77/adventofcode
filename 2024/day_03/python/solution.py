#!/usr/bin/env python3

import argparse
import re
import sys


class Solution:
  @property
  def corrupted_memory(self) -> str:
    if getattr(self, '_corrupted_memory', None) is None:
      with open(file=self.input_file, mode='r', encoding='utf-8') as file:
        self._corrupted_memory = file.read()
    return self._corrupted_memory

  def __init__(self, input_file: str) -> None:
    self.input_file: str = input_file

    self._corrupted_memory = None

  def solve(self) -> None:
    print(self.part_one())
    print(self.part_two())

  def part_one(self) -> int:
    results: int = 0

    matches = re.findall(r'mul\((\d+,\d+)\)', self.corrupted_memory)
    for match in matches:
      numbers = match.split(',')
      results += int(numbers[0]) * int(numbers[1])

    return results

  def part_two(self) -> int:
    results: int = 0
    multiplication_enabled: bool = True

    matches = re.finditer(r'mul\((\d+,\d+)\)|do\(\)|don\'t\(\)', self.corrupted_memory)

    for match in matches:
      if match.group(0) == 'do()':
        multiplication_enabled = True
      elif match.group(0) == 'don\'t()':
        multiplication_enabled = False
      else:
        if not multiplication_enabled:
          continue
        numbers = match.group(1).split(',')
        results += int(numbers[0]) * int(numbers[1])

    return results

class MyArgNamespace(argparse.Namespace):
  input_file: str


def create_arg_parser() -> argparse.ArgumentParser:
  parser: argparse.ArgumentParser = argparse.ArgumentParser()

  parser.add_argument(
    '-f',
    '--file',
    action='store',
    default=None,
    dest='input_file',
    help='The filepath to the input',
    required=True,
  )

  return parser


## Main
def main() -> None:
  try:
    arg_parser: argparse.ArgumentParser = create_arg_parser()
    args: argparse.Namespace = arg_parser.parse_args(namespace=MyArgNamespace())

    Solution(input_file=args.input_file).solve()

  except KeyboardInterrupt:
    sys.exit(130)


if __name__ == '__main__':
  main()
