import argparse


def parse_arguments():
    """
        Parses command line arguments for the Secret Santa assignment script.
        Returns:
            argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Secret Santa Assignment")
    parser.add_argument("input_file", type=str, help="Path to the input CSV file")
    parser.add_argument("previous_assignment", type=str,
            help="Path to previous year secret santa CSV file")
    return parser.parse_args()