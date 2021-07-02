#!/usr/bin/env python3
# coding: utf-8

"""log.py: A simple wrapper around python logging."""

import logging
import os
from datetime import datetime


def create_directory(directory_name: str) -> None:
    """Create a log directory if it does not exist."""
    if not (os.path.isdir(directory_name)):
        os.mkdir(directory_name)


def create_log_file(path: str) -> None:
    """Create a file with the current time as name at path."""
    file_name = datetime.now().strftime("%Y_%m_%d-%H_%M_%S.log")
    file = open(path + file_name, 'w')
    file.close()


class ConsoleFormatter(logging.Formatter):
    """Logging Formatter with colors."""

    grey = "\x1b[38;21m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    my_format = ("[%(asctime)s.%(msecs)03d] %(name)s - %(levelname)s"
                 + "- %(message)s (%(filename)s:%(lineno)d)")

    FORMATS = {logging.DEBUG: grey + my_format + reset,
               logging.INFO: green + my_format + reset,
               logging.WARNING: yellow + my_format + reset,
               logging.ERROR: red + my_format + reset,
               logging.CRITICAL: bold_red + my_format + reset}

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(fmt=log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)


def logger(logger_name: str, console_level: int = logging.INFO,
           file_level: int = logging.DEBUG, create_file: bool = False) -> logging.Logger:
    """
    A new simple logger config for python logging.

    The logger have a console handler that have a default log level of INFO.
    The logger have a file handler that have a default log level of DEBUG.

    Note that this config is made for small to medium project. For bigger
    project, we advise you to take the time to make your logger fit your project.
    """
    # Check if a logger with logger_name does not already exist
    logger_list = [name for name in logging.root.manager.loggerDict]
    if logger_name in logger_list:
        return logging.getLogger(logger_name)  # XXX

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    log_dir_name = "log/"

    # create log directory
    create_directory(log_dir_name)

    if create_file or len(os.listdir(log_dir_name)) == 0:
        create_log_file(log_dir_name)

    # create console handler and set level to INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)

    # create file handler and set level to debug
    file_list = os.listdir(log_dir_name)
    file_list.sort()
    file_path = log_dir_name + file_list[-1]
    file_handler = logging.FileHandler(filename=file_path, mode='a', encoding='utf-8')
    file_handler.setLevel(file_level)

    # create file formatter
    file_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    file_formatter = logging.Formatter(fmt=file_format, datefmt='%m/%d/%Y %I:%M:%S %p')

    # add formatter to console_handler
    console_handler.setFormatter(ConsoleFormatter())
    file_handler.setFormatter(file_formatter)

    # add console_handler to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def close_logger() -> None:
    """Be aware that this will close all of the logger. Not juste this one."""
    logging.shutdown()
