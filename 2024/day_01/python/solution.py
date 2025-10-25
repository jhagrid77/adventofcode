#!/usr/bin/env python3

import argparse
import sys


class Solution:
  @property
  def first_column_numbers(self) -> list[int]:
    if getattr(self, '_first_column_numbers', None) is None:
      self._first_column_lines: list[int] = self.get_column_entries(column=0)
      self._first_column_lines.sort()
    return self._first_column_lines

  @property
  def second_column_numbers(self) -> list[int]:
    if getattr(self, '_second_column_numbers', None) is None:
      self._second_column_numbers: list[int] = self.get_column_entries(column=1)
      self._second_column_numbers.sort()
    return self._second_column_numbers

  def __init__(self, input_file: str) -> None:
    self.input_file: str = input_file

    self._first_column_lines = None
    self._second_column_numbers = None

  def solve(self) -> None:
    print(self.part_one())
    print(self.part_two())

  def get_column_entries(self, column: int) -> list[int]:
    with open(file=self.input_file, mode='r', encoding='utf-8') as file:
      lines: list[str] = file.readlines()

    column_entries: list[int] = []

    for line in lines:
      column_entries.append(int(line.split()[column].strip()))

    return column_entries

  def part_one(self) -> int:
    total_distance: int = 0

    for pair in zip(self.first_column_numbers, self.second_column_numbers):
      distance: int = abs(pair[0] - pair[1])
      total_distance += distance

    return total_distance

  def part_two(self) -> int:
    similarity_score: int = 0

    for number in self.first_column_numbers:
      similarity_score += number * self.second_column_numbers.count(number)

    return similarity_score

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
