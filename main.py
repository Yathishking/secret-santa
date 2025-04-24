import sys
from src.AppInit import AppInit
from utils.cli import parse_arguments

def main():
    args = parse_arguments()
    try:
        init = AppInit(args.input_file, previous_assignment=args.previous_assignment)
        init.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


