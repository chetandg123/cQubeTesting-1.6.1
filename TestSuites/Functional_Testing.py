import configparser
import sys
import os

from SR import semester_report_functional_testing
from get_dir import pwd
from CRC import crc, crc_report_functional_testing
from Login import cQube_login
from SI.MAP import SI_mapreport, School_Map_functional_testing
from SI.Report import SI_Report, School_report_functional_testing

import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_functional_testing.cQube_CRC_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_functional_testing.cQube_Semester_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_Map_functional_testing.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_report_functional_testing.cQube_SI_Report)
        ])
        p= pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Functional Test Report',
            verbosity=1,
        )

        runner1.run(functional_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()