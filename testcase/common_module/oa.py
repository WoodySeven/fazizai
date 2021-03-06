#!/usr/bin/env python
import os
import unittest
from selenium import webdriver
import logging
import time


class Oa(unittest.TestCase):
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

    def test_create_meeting(self):
        """新增案件"""
        logging.info("test_create_case start....")
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(5)
        # 点击登陆按钮
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/button').click()
        time.sleep(5)
        # 点击右上角功能键
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/header/div[2]/span/button').click()
        # 点击案件列表
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/div/a[1]/div[2]/div[1]/span').click()
        time.sleep(3)
        # 点击某案件
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[4]/div/div[2]/div[1]/a').click()
        # 勾选六项审查
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/a/div[2]/div[1]/label/span[1]/span').click()
        # 点击查看更多按钮
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div/div[3]/div[10]/button').click()
        # 点击新增按钮
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div/div[3]/div[4]/div/div/div[1]/div[2]/span/span').click()
        # 输入备注
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[5]/textarea').send_keys('sssss')
        # 点击上传文件
        driver.find_element_by_xpath('//*[@id="file"]').click()
        time.sleep(5)
        os.system(r'C:\Users\sanmao\Desktop\file.exe')
        time.sleep(4)
        # 点击确定按钮
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[9]/button/label').click()
        time.sleep(5)
