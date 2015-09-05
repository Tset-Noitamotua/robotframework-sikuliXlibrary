# -*- coding: utf-8 -*-

import common
from sikuli import *
from logger import *
from sikuli.Sikuli import Region as SikuliRegion

# enable slow motion if debug log level enabled
if common.cfgLoggingLevel.lower() == 'debug':
	setShowActions(False)

# =============================================== #
#         Overwritten SikuliX methods             #
# =============================================== #
# NOTE @ WLAD:	Dieser Abschnitt kann evtl. weg
# 			 	Er wird nur benoetigt, wenn SikuliX Methoden OHNE Region aufrufbar sein sollen.
# 				TODO: Pruefen und ggf. Abschnitt loeschen!!!

def sikuli_method(name, *args, **kwargs):
	return sys.modules['sikuli.Sikuli'].__dict__[name](*args, **kwargs)

def exists(target, timeout=0):
	addFoundImage(getFilename(target))
	return sikuli_method('exists', target, float(timeout))



# =============================================== #
#          Overwritten SikuliX classes            #
# =============================================== #

# overwritten SikuliX Region class
class Region(SikuliRegion, BaseLogger):

	def click(self, target, modifiers=0):
		try:
			return SikuliRegion.click(self, target, modifiers)
		except FindFailed, e:
			self.log.html_img("Find Failed", common.cfgImageLibrary + '/' + getFilename(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e

	def rightClick(self,target, modifiers=0):
		# addFoundImage(getFilename(target))
		try:
			return SikuliRegion.rightClick(self, target, modifiers)
		except FindFailed, e:
			self.log.html_img("Find Filed", common.cfgImageLibrary + '/' + getFilename(target))
			self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
			raise e

	def exists(self, target, timeout=None):
		img = getFilename(target)
		reg = (self.getX(), self.getY(), self.getW(), self.getH())
		addFoundImage(img, reg)
		return SikuliRegion.exists(self, target, timeout)

	def waitVanish(self, target, timeout=0.0):
		img = getFilename(target)
		reg = (self.getX(), self.getY(), self.getW(), self.getH())
		addFoundImage(img, reg)
		return SikuliRegion.waitVanish(self, target, timeout)