#!/usr/bin/env python
import unittest
from selenium import webdriver
from lib.Logger import Logger
import logging
import time


class CreateCase(unittest.TestCase):
    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.59.6.207/crp-legal-app-dev/"
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_create_case(self):
        """新增案件"""
        logging.info("test_create_case start....")
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/button').click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()