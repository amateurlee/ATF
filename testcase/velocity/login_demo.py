# -*- coding=utf-8 -*-

"""
About this module
    A demo of test case.

Description of classes
    LoginDemo:
        Demo test case class for login.

Description of methods

"""

__authors__ = [
    '"Hugo Ding" <huicong.ding@spirent.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-12   First version                                 Hugo
# ------------------------------------------------------------------------------

from testcase.base import SeleniumBaseTestCase


class LoginDemo(SeleniumBaseTestCase):
    def setUp(self):
        super(LoginDemo, self).setUp()

    def test_login(self):
        pass

    def tearDown(self):
        super(LoginDemo, self).tearDown()
