#!/usr/bin/env python3

import argparse
import re
import sys
from typing import Any


class Solution:
  @property
  def input_lines(self) -> list[str]:
    if getattr(self, '_input_lines', None) is None:
      with open(file=self.input_file, mode='r', encoding='utf-8') as file:
        self._input_lines = file.readlines()
    return self._input_lines

  def __init__(self, input_file: str) -> None:
    self.input_file: str = input_file

    self._input_lines = None

    self.lines_length = len(self.input_lines)
    self.max_lines_index = self.lines_length - 1

    self.line_length = len(self.input_lines[0])
    self.max_line_index = self.line_length - 1

  def solve(self) -> None:
    print(self.part_one())
    print(self.part_two())

  def _check_up(self, line_num: int, x_pos: int) -> bool:
    if line_num - 3 < 0:
      return False

    word_to_check: str = (
      self.input_lines[line_num][x_pos]
      + self.input_lines[line_num - 1][x_pos]
      + self.input_lines[line_num - 2][x_pos]
      + self.input_lines[line_num - 3][x_pos]
    )

    return word_to_check == 'XMAS'

  def _check_up_right(self, line_num: int, x_pos: int) -> bool:
    if line_num - 3 < 0:
      return False

    if x_pos + 3 > self.max_line_index:
      return False

    word_to_check: str = (
      self.input_lines[line_num][x_pos]
      + self.input_lines[line_num - 1][x_pos + 1]
      + self.input_lines[line_num - 2][x_pos + 2]
      + self.input_lines[line_num - 3][x_pos + 3]
    )

    return word_to_check == 'XMAS'

  def _check_right(self, line_num: int, x_pos: int) -> bool:
    if x_pos + 3 > self.max_line_index:
      return False

    word_to_check: str = self.input_lines[line_num][x_pos : x_pos + 4]

    return word_to_check == 'XMAS'

  def _check_down_right(self, line_num: int, x_pos: int) -> bool:
    if line_num + 3 > self.max_lines_index:
      return False

    if x_pos + 3 > self.max_line_index:
      return False

    word_to_check: str = (
      self.input_lines[line_num][x_pos]
      + self.input_lines[line_num + 1][x_pos + 1]
      + self.input_lines[line_num + 2][x_pos + 2]
      + self.input_lines[line_num + 3][x_pos + 3]
    )

    return word_to_check == 'XMAS'

  def _check_down(self, line_num: int, x_pos: int) -> bool:
    if line_num + 3 > self.max_lines_index:
      return False

    word_to_check: str = (
      self.input_lines[line_num][x_pos]
      + self.input_lines[line_num + 1][x_pos]
      + self.input_lines[line_num + 2][x_pos]
      + self.input_lines[line_num + 3][x_pos]
    )

    return word_to_check == 'XMAS'

  def _check_down_left(self, line_num: int, x_pos: int) -> bool:
    if line_num + 3 > self.max_lines_index:
      return False

    if x_pos - 3 < 0:
      return False

    word_to_check: str = (
      self.input_lines[line_num][x_pos]
      + self.input_lines[line_num + 1][x_pos - 1]
      + self.input_lines[line_num + 2][x_pos - 2]
      + self.input_lines[line_num + 3][x_pos - 3]
    )

    return word_to_check == 'XMAS'

  def _check_left(self, line_num: int, x_pos: int) -> bool:
    if x_pos - 3 < 0:
      return False

    word_to_check: str = (self.input_lines[line_num][x_pos - 3 : x_pos + 1])[::-1]
    return word_to_check == 'XMAS'

  def _check_up_left(self, line_num: int, x_pos: int) -> bool:
    if line_num - 3 < 0:
      return False

    if x_pos - 3 < 0:
      return False

    word_to_check: str = (
      self.input_lines[line_num][x_pos]
      + self.input_lines[line_num - 1][x_pos - 1]
      + self.input_lines[line_num - 2][x_pos - 2]
      + self.input_lines[line_num - 3][x_pos - 3]
    )

    return word_to_check == 'XMAS'

  def _is_x_mas(self, line_num: int, x_pos: int) -> bool:
    if line_num - 1 < 0 or line_num + 1 > self.max_lines_index:
      return False

    if x_pos - 1 < 0 or x_pos + 1 > self.max_line_index:
      return False

    cross_one: str = (
      self.input_lines[line_num - 1][x_pos - 1]
      + self.input_lines[line_num][x_pos]
      + self.input_lines[line_num + 1][x_pos + 1]
    )

    cross_two: str = (
      self.input_lines[line_num - 1][x_pos + 1]
      + self.input_lines[line_num][x_pos]
      + self.input_lines[line_num + 1][x_pos - 1]
    )

    return (cross_one == 'MAS' or cross_one == 'SAM') and (cross_two == 'MAS' or cross_two == 'SAM')

  def part_one(self) -> int:
    results: int = 0

    for line_number in range(0, self.lines_length):
      matches = re.finditer(pattern='X', string=self.input_lines[line_number])

      for match in matches:
        for function in (
          self._check_up,
          self._check_up_right,
          self._check_right,
          self._check_down_right,
          self._check_down,
          self._check_down_left,
          self._check_left,
          self._check_up_left,
        ):
          if function(line_num=line_number, x_pos=match.start()):
            results += 1

    return results

  def part_two(self) -> int:
    results: int = 0

    for line_number in range(0, self.lines_length):
      matches = re.finditer(pattern='A', string=self.input_lines[line_number])

      for match in matches:
        if self._is_x_mas(line_num=line_number, x_pos=match.start()):
          results += 1

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
