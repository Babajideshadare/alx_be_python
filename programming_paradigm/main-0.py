# main-0.py

import argparse
import sys
from bank_account import BankAccount

def parse_args():
    parser = argparse.ArgumentParser(
        description="Bank account CLI using the BankAccount class."
    )
    parser.add_argument(
        "-i", "--initial-balance",
        type=float,
        default=0.0,
        help="Initial account balance (default: 0.0)"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    deposit_parser = subparsers.add_parser("deposit", help="Deposit an amount")
    deposit_parser.add_argument("amount", type=float, help="Amount to deposit")

    withdraw_parser = subparsers.add_parser("withdraw", help="Withdraw an amount")
    withdraw_parser.add_argument("amount", type=float, help="Amount to withdraw")

    subparsers.add_parser("balance", help="Show current balance")

    return parser.parse_args()

def main() -> int:
    args = parse_args()
    account = BankAccount(initial_balance=args.initial_balance)

    try:
        if args.command == "deposit":
            account.deposit(args.amount)
            print(f"Deposited ${args.amount:.2f}")
            account.display_balance()

        elif args.command == "withdraw":
            success = account.withdraw(args.amount)
            if success:
                print(f"Withdrew ${args.amount:.2f}")
            else:
                print("Insufficient funds: withdrawal denied.")
            account.display_balance()

        elif args.command == "balance":
            account.display_balance()

    except ValueError as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())