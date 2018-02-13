#!/usr/bin/env python
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import os
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
        time.sleep(5)
        # 点击登陆按钮
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/button').click()
        time.sleep(5)
        # 点击右上角功能键
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/header/div[2]/span/button').click()
        # 点击案件列表
        driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/div/a[1]/div[2]/div[1]/span').click()
        time.sleep(3)
        # # 点击右下角新增按钮
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/a').click()
        # # 选择涉案组织
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[3]/div[2]/div[2]/input').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[3]/div[2]/ul/li[12]').click()
        # time.sleep(3)
        # # 选择业态
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[4]/div[2]/div[2]/input').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[4]/div[2]/ul/li[4]').click()
        # # 选择涉案主体
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[5]/div/div[2]/div[2]/input').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[5]/div/div[2]/ul/li[1]').click()
        # # 选择我方其他涉案主体
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[6]/div[2]/div[2]/input').click()
        # time.sleep(3)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[6]/div[2]/ul/li[5]').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[6]/div[2]/div[2]/input').click()
        # time.sleep(3)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[6]/div[2]/ul/li[6]').click()
        # time.sleep(3)
        # # 选择案件类型
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[7]/div[2]/div[2]/span').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[7]/div[2]/ul/li[1]').click()
        # time.sleep(3)
        # # # 选择起诉日期/法律文书送达日期
        # # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[8]/input').click()
        # # time.sleep(2)
        # # data = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div/div[2]/div[1]/div/div[9]')
        # # time.sleep(2)
        # # target = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div/div[2]/div[1]/div/div[11]')
        # # time.sleep(2)
        # # ActionChains(driver).drag_and_drop(data, target).perform()
        # # time.sleep(4)
        # # ActionChains.click_and_hold(data).move_by_offset(0, 36).release().perform()
        # # 选择民事
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[9]/div[2]/div[2]/span').click()
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[9]/div[2]/ul/li[1]').click()
        # time.sleep(3)
        # # 选择案件分类编码
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[10]/div[2]/div[2]/input').click()
        # time.sleep(3)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[10]/div[2]/ul/li[1]').click()
        # time.sleep(5)
        # # 选择二级案件分类
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[10]/div[3]/div[2]/input').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[10]/div[3]/ul/li[1]').click()
        # time.sleep(3)
        # # 选择我方角色
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[11]/div[2]/div[2]/span').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[11]/div[2]/ul/li[2]').click()
        # time.sleep(3)
        # # 选择重大/非重大案件
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[12]/div[2]/div[2]/span').click()
        # time.sleep(3)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[12]/div[2]/ul/li[2]').click()
        # time.sleep(3)
        # # 新增对方当事人
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[13]/div/div[2]/span/i').click()
        # time.sleep(5)
        # # 输入案件名称
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div/div[1]/input').send_keys('xxx某案件')
        # time.sleep(3)
        # # 选择对方性质
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div/div[2]/div[2]/div[2]/span').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div/div[2]/div[2]/ul/li[1]').click()
        # time.sleep(3)
        # # 选择对方角色
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div/div[3]/div[2]/div[2]/span').click()
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div/div[3]/div[2]/ul/li[1]').click()
        # time.sleep(3)
        # # 点击添加
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div/div[4]/div[2]/button').click()
        # time.sleep(5)
        # # 点击下一步按钮
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[14]/div[2]/button').click()
        # time.sleep(5)
        # # 输入案件名称
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/input').send_keys('申请人诉被申请人案')
        # # 输入关联案件案号
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[3]/input').send_keys('CRPH500--2017--Z000000--00001')
        # # 输入案号
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[4]/input').send_keys('23552')
        # # 输入标的额
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[5]/input').send_keys('234')
        # # 选择主办法律顾问
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[6]/div[2]/div[2]/input').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[6]/div[2]/ul/li[87]').click()
        # # 选择辅助人员
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[7]/div[2]/div[2]/input').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[7]/div[2]/ul/li[86]').click()
        # # 输入诉讼请求
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[8]/textarea').send_keys('诉讼请求')
        # # 输入备注
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[9]/textarea').send_keys('哈哈哈哈哈')
        # # 点击保存
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[10]/div[2]/button').click()
        # time.sleep(3)
        # # 选择是否要加外聘律师（不需要）
        # driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div[5]/div[4]/div/div[1]/button').click()
        # time.sleep(5)




if __name__ == '__main__':
    unittest.main()