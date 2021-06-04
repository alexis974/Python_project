#!/usr/bin/env python3
# coding: utf-8

"""main.py: Main program for the project."""

from log import Logger


def main():
    """Main function of the project."""
    log = Logger("Main", create_file=True)
    log.info("Program starting...")

    # TODO

    log.info("Program ending...")
    log.close_all()


if __name__ == "__main__":
    main()
