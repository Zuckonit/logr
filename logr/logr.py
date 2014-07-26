# encoding: utf-8
#!/usr/bin/env python

"""
    Desc:
        simple logging wrapper
    
    Example:
        >>> from logr.logr import Logr
        >>> class TestLogr(Logr):
        >>>     def __init__(self):
        >>>         super(TestLogr, self).__init__('~/test')

        >>>     def test(self):
        >>>         try:
        >>>             1/0
        >>>         except Exception as e:
        >>>             self.error('function test error: %s' % e)

    ~~~~~~~
    logr.py
"""

import os.path as osp
import logging
from logging.handlers import RotatingFileHandler


__all__ = [
    'Logr',
]

class Logr(object):
    def __init__(self, log_path, log_level=logging.DEBUG, log_size=10<<10<<10, backup_count=5):
        super(Logr, self).__init__()
        
        log_path = self.__get_safe_path(log_path)
        if osp.splitext(log_path)[-1] != '.log':
            log_path += '.log'
        
        formatter = logging.Formatter("%(asctime)s -- [%(levelname)s] [%(name)s] [%(lineno)s]: %(message)s")
        self.logger = logging.getLogger(__name__)
        if log_level > logging.ERROR:
            log_error_path = log_path
            self.logger.setLevel(logging.ERROR)
        else:
            log_debug_path = log_path
            log_error_path = osp.splitext(log_path)[0] + '_error.log'
            self.logger.setLevel(logging.DEBUG)

            self.file_hd_debug= RotatingFileHandler(log_debug_path, maxBytes=log_size,
                    backupCount=backup_count, encoding="utf-8")
            self.file_hd_debug.setLevel(logging.DEBUG)
            self.file_hd_debug.setFormatter(formatter)
            self.logger.addHandler(self.file_hd_debug)
        
        self.file_hd_error = RotatingFileHandler(log_error_path, maxBytes=log_size,
                backupCount=backup_count, encoding="utf-8")
        self.file_hd_error.setLevel(logging.ERROR)
        self.file_hd_error.setFormatter(formatter)
        self.logger.addHandler(self.file_hd_error)
    
    def __get_safe_path(self, path):
        path = osp.expanduser(path)
        path = osp.abspath(path)
        path = path.replace('\\', '/')
        return path

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self.logger.critical(*args, **kwargs)

    def exception(self, *args, **kwargs):
        '''by this, we can quickly find the problem line'''
        self.logger.exception(*args, **kwargs)
