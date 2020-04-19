#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"
# FileName: *.py
# Version:1.0.0
# ====#====#====#====
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, NoSuchWindowException, NoAlertPresentException, \
	NoSuchElementException


# browser: WebDriver = webdriver.Chrome(
# 	executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')


class Page(object):
	"""
	base class for ui page
	"""

	def __init__(self, driver):
		# TODO: for temp
		self.driver = webdriver.Chrome(
			executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
		pass;

	def open(self, url):
		"""
		open current page
		:return:
		"""
		self.driver.get(url)
		pass

	def get_element(self, *loc):
		"""
		wait and find html element by locator
		:param loc:
		:return: html element
		"""
		try:
			WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
			return self.driver.find_element(*loc)
		except ValueError as e:
			print(e)
			pass

	def get_elements(self, *loc):
		"""
		wait and find html elements by locator
		:param loc:
		:return: html element
		"""
		try:
			WebDriverWait().until(EC.visibility_of_element_located(loc))
			return self.driver.find_elements(loc)
			pass
		except:
			pass

	def send_key(self, loc, val):
		"""

		:param loc:
		:param val:
		:return:
		"""
		loc = getattr(self, "_%s" % loc)
		self.get_element(*loc).send_keys(val)
