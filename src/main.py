#!/usr/bin/env python3
# coding: utf-8

"""main.py: Main program for the project."""

from log import close_logger, logger


def main():
    """Main function of the project."""
    log = logger("Main", create_file=True)
    log.info("Program starting...")

    # TODO

    log.info("Program ending...")
    close_logger()


if __name__ == "__main__":
    main()
