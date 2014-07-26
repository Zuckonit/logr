#!/usr/bin/env python
# encoding: utf-8

from logr import Logr

class TestLogr(Logr):
    def __init__(self):
        log_path = '~/test'
        super(TestLogr, self).__init__(log_path)

    def f(self):
        try: 1/0
        except Exception as e:
            self.logger.error('f error: %s' % e)


if __name__ == '__main__':
    t = TestLogr()
    t.f()
