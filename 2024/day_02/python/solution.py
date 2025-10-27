#!/usr/bin/env python3

import argparse
import sys


class Solution:
  @property
  def reports(self) -> list[tuple[int]]:
    if getattr(self, '_reports', None) is None:
      self._reports: list[tuple[int]] = self.get_reports()
    return self._reports

  def __init__(self, input_file: str) -> None:
    self.input_file: str = input_file

    self._reports = None

  def solve(self) -> None:
    print(self.part_one())
    print(self.part_two())

  def get_reports(self) -> list[tuple[int]]:
    results: list[tuple[int]] = []

    with open(file=self.input_file, mode='r', encoding='utf-8') as file:
      for line in file:
        results.append(self._to_report(entry=line))

    return results

  def _to_report(self, entry: str) -> tuple[int]:
    str_levels: list[str] = entry.split()
    levels: list[int] = []

    for str_level in str_levels:
      levels.append(int(str_level))

    return tuple(levels)

  def is_report_safe(self, report: tuple[int, ...]) -> bool:
    initial_difference: int = abs(report[0] - report[1])
    if initial_difference == 0 or initial_difference > 3:
      return False
    is_increasing: bool = report[0] < report[1]

    for i in range(len(report) - 2 + 1):
      window: tuple[int, ...] = report[i:i+2]

      if is_increasing and not window[0] < window[1]:
        return False
      if not is_increasing and window[0] < window[1]:
        return False

      difference: int = abs(window[0] - window[1])
      if difference == 0 or difference > 3:
        return False

    return True

  def is_report_safe_dampener(self, report: tuple[int, ...]) -> bool:
    if self.is_report_safe(report=report):
      return True

    for i in range(len(report)):
      if self.is_report_safe(report=tuple(report[:i] + report[i + 1:])):
        return True

    return False

  def part_one(self) -> int:
    results: int = 0

    for report in self.reports:
      if not self.is_report_safe(report=report):
        continue
      results += 1

    return results

  def part_two(self) -> int:
    results: int = 0

    for report in self.reports:
      if self.is_report_safe_dampener(report=report):
        results += 1
        continue

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
