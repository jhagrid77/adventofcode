#!/usr/bin/env python3

import argparse
import sys

class Solution:

  @property
  def input_lines(self) -> list[str]:
    if getattr(self, '_input_lines', None) is None:
      with open(file=self.input_file, mode='r', encoding='utf-8') as file:
        self._input_lines = [line.strip() for line in file.readlines()]
    return self._input_lines

  def __init__(self, input_file: str) -> None:
    self.input_file: str = input_file

    self._input_lines = None

  def solve(self) -> None:
    print(self.part_one())
    print(self.part_two())

  def _rotate_left(self, current_position: int, clicks: int) -> int:
    spins = clicks // 100
    clicks = clicks - (spins * 100)

    if current_position - clicks >= 0:
      return current_position - clicks

    return (current_position - clicks) + 100

  def _rotate_right(self, current_position: int, clicks: int) -> int:
    spins = clicks // 100
    clicks = clicks - (spins * 100)

    if current_position + clicks <= 99:
      return current_position + clicks

    return (current_position + clicks) - 100

  def part_one(self) -> int:
    results: int = 0
    position: int = 50

    for entry in self.input_lines:
      direction: str = entry[0]

      if direction == 'L':
        position = self._rotate_left(current_position=position, clicks=int(entry[1:]))
      elif direction == 'R':
        position = self._rotate_right(current_position=position, clicks=int(entry[1:]))

      if position == 0:
        results += 1

    return results

  def part_two(self) -> int:
    results: int = 0
    current_position: int = 50
    new_position = None

    for entry in self.input_lines:
      direction: str = entry[0]
      clicks: int = int(entry[1:])
      spins: int = clicks // 100
      clicks = clicks - (spins * 100)

      results += spins

      if direction == 'L':
        new_position = self._rotate_left(current_position=current_position, clicks=clicks)
        if current_position != 0 and new_position > current_position and new_position != 0:
          results += 1
      elif direction == 'R':
        new_position = self._rotate_right(current_position=current_position, clicks=clicks)
        if current_position != 0 and new_position < current_position and new_position != 0:
          results += 1

      if new_position == 0:
        results += 1

      current_position = new_position

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
