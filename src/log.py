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


class Logger:
    def __init__(self, logger_name: str, console_level: int = logging.INFO,
                 file_level: int = logging.DEBUG, create_file: bool = False) -> None:
        """
        A new simple wrapper class around python logging.

        The logger have a console handler that have a default log level of INFO.
        The logger have a file handler that have a default log level of DEBUG.

        Note that this wrapper is made for small to medium project. For bigger
        project, we advise you to take the time to make your logger fit your project.
        """
        self.name = logger_name

        # We check if a logger with logger_name does not already exist
        logger_list = [name for name in logging.root.manager.loggerDict]
        if self.name in logger_list:
            self.logger = logging.getLogger(logger_name)  # XXX
            return

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

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

        # create formatter
        formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to console_handler
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # add console_handler to logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def debug(self, msg: str = "", *args, **kwargs) -> None:
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg: str = "", *args, **kwargs) -> None:
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: str = "", *args, **kwargs) -> None:
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: str = "", *args, **kwargs) -> None:
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: str = "", *args, **kwargs) -> None:
        self.logger.critical(msg, *args, **kwargs)

    def exception(self, msg: str = "", *args, **kwargs) -> None:
        self.logger.exception(msg, *args, **kwargs)

    def close_all(self) -> None:
        """Be aware that this will close all of the logger. Not juste this one."""
        logging.shutdown()
