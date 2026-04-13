from __future__ import annotations

import argparse
from typing import Sequence


def create_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""

    parser = argparse.ArgumentParser(description="A small CLI calculator.")

    subcommands = parser.add_subparsers(dest="command", required=True)

    add_parser = subcommands.add_parser("add", help="Add two numbers.")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    sub_parser = subcommands.add_parser("sub", help="Subtract two numbers.")
    sub_parser.add_argument("a", type=float)
    sub_parser.add_argument("b", type=float)

    mul_parser = subcommands.add_parser("mul", help="Multiply two numbers.")
    mul_parser.add_argument("a", type=float)
    mul_parser.add_argument("b", type=float)

    div_parser = subcommands.add_parser(
        "div", help="Divide two numbers (b must be non-zero)."
    )
    div_parser.add_argument("a", type=float)
    div_parser.add_argument("b", type=float)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the calculator and print the result."""

    parser = create_parser()
    args = parser.parse_args(argv)

    a: float = args.a
    b: float = args.b

    if args.command == "add":
        result = a + b
    elif args.command == "sub":
        result = a - b
    elif args.command == "mul":
        result = a * b
    else:
        if b == 0:
            parser.error("division by zero")
        result = a / b

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
