# -*- coding: utf-8 -*-
from __future__ import with_statement

from sikuliwrapper import *

s = Screen()


class _SikuliX_Keywords(BaseLogger):
	"""SikuliXLibrary for Robot Framework"""

	def __init__(self):
		self.name = 'WorldOfShit'
		self.action = 'click'
		self.reg = Region(s)
		self.region = Region.create(Screen(0).x, Screen(0).y, Screen(0).w, Screen(0).h)
		self.region = Region(self.region)
		self.appCoordinates = (0, 0, 1024, 768)

	# def log_library_arguments(self):
	# 	if self.greeting == 'World' and self.timeout == 5.0 and self.similarity == 0.7 \
	# 			and self.image_path == 'images':
	# 		print 'NO library args passed! SikuliXLibrary imported with defaults:\n'
	# 		print 'greeting:\t\t', self.greeting
	# 		print 'timeout:\t\t', self.timeout
	# 		print 'similarity:\t\t', self.similarity
	# 		print 'image_path:\t\t', self.image_path
	# 		print '- self.single_key:\t\t', self.single_key
	# 	else:
	# 		print 'SikuliXLibrary imported with this FUCKING arguments:\n'
	# 		print 'greeting:\t\t', self.greeting
	# 		print 'timeout:\t\t', self.timeout
	# 		print 'similarity:\t\t', self.similarity
	# 		print 'image_path:\t\t', self.image_path
	# 		print 'cfgImageLibrary:\t', common.cfgImageLibrary
	# 		print '- self.single_key:\t\t', self.single_key

	def click(self, *args, **kwargs):
		"""
        Clicks a click target (e.g. gui element)

        ARGS:   required        optional
                click_target    post_condition
                                timeout
                                similarity
        EXAMPLE:
        click('gui_image.png', 'condition_imgage.png', timeout=7.7)
        click('click_target.png', 'post_action_condition.png)

        ROBOT FRAMEWORK EXAMPLE:
        click   click_target.png    post_condition.png  timeout=3.0
        """

		self.action = 'click'
		# self.post_condition = kwargs.get('post_condition', None)

		# log given arguments
		# self.log_arguments('CLICK', *args, **kwargs)

		# pass given arguments to -> do() function
		self.do(*args, **kwargs)

	def wait_vanish(self, *args, **kwargs):
		"""
        Waits until something disappears. 'Something' can be a button, a window or else represented by an image.

        ARGS:   required        optional
                image           timeout
                                similarity
        EXAMPLE:
        wait_vanish('some_image.png', timeout=7.7, similarity=0.5)

        ROBOT FRAMEWORK EXAMPLE:
        wait vanish   image.png    timeout=3.0     similarity=0.5
        """
		image = args[0]
		# self.action = 'wait_vanish'
		self.timeout = kwargs.get('timeout', 5.0)
		Debug.on(3)
		if self.reg.waitVanish(image, float(self.timeout)):
			self.log.passed("%s disappeared before timeout." %image)
		else:
			self.log.failed("%s did NOT disappear before timeout!" %image)
		Debug.off()

		# log given arguments
		self.log_arguments('WAIT_VANISH', *args, **kwargs)

	# pass given arguments to -> do() function
	# self.do(*args, **kwargs)

	def type(self, *args, **kwargs):
		""" - - - - - - - - - - - - - - \
        Types text into a textfield   \
        - - - - - - - - - - - - - - - - \

        Also enables to send special keys like ENTER, DEL, END etc.
        But this will be implemented by press_key()
        ENTER   = \n
        DEL     = \007
        END     = \006
        ...

        TODO: add other special keys here!!!

        """
		self.action = 'type'

		# log given arguments
		# self.log_arguments('TYPE', *args, **kwargs)

		# pass given arguments to -> do() function
		self.do(*args, **kwargs)

	def use_keyboard_shortcut(self, *args, **kwargs):
		# self.action = 'press_key'
		# self.single_key = kwargs.get('single_key', 'shit')

		# log given arguments
		self.log_arguments('USE_KEYBOARD_SHORTCUT', *args, **kwargs)

		# perform action press KeyCombination
		self.reg.keyDown(args[0])
		self.reg.type(args[1])
		self.reg.keyUp(args[0])

	def use_seq_keyboard_shortcut(self):
		pass

	# TODO

	def context_click(self, *args, **kwargs):
		""" - - - - - - - - - - - - - - - - - - - -
        Makes a context click on a click target
        - - - - - - - - - - - - - - - - - - - - - -

        This will perform a right click whit the mouse on a given click target.
        Click target can be a gui element represented by an image path string. See
        examples below. The following args must/can be used:

        ARGS:   required        optional
                click_target    post_condition=None
                                timeout=5.0

        USAGE:
        click(click_target, post_condition=None, timeout=5.0)

        EXAMPLE:
        click('gui_image.png', 'condition_imgage.png', timeout=7.7)
        click('click_target.png', 'post_condition.png)    # will use default timeout

        ROBOT FRAMEWORK EXAMPLE:
        click   click_target.png    post_condition.png   timeout=3.0
        click   image.png           condition.png        # will use default timeout
        """
		self.action = 'context_click'

		# log given arguments
		self.log_arguments('CONTEXT_CLICK', *args, **kwargs)

		# pass given arguments to -> do() function
		self.do(*args, **kwargs)

	def check_post_condition(self, *args, **kwargs):

		self.timeout = kwargs.get('timeout', 5.0)

		# change MinSimilarity if necessary
		self.similarity = kwargs.get('similarity', 0.7)
		Settings.MinSimilarity = float(self.similarity)

		# log given arguments
		self.log_arguments('CHECK_POST_CONDITION', *args, **kwargs)

		if not self.post_condition:
			self.log.passed('Action successfully performed!')
		else:
			# change MinSimilarity if necessary
			# self.similarity = kwargs.get('similarity', 0.7)
			# Settings.MinSimilarity = float(self.similarity)

			# check post condition until timeout
			if not exists(self.post_condition, float(self.timeout)):
				self.log.failed('Post condition (%s) NOT MET!' % self.post_condition)

			# restore default post_condition
			# self.post_condition = kwargs.get('post_condition', None)
			else:
				self.log.passed('Expected post condition (%s) met.' % self.post_condition)

			# restore default post_condition
			# self.post_condition = kwargs.get('post_condition', None)

			# restore default post_condition
			self.post_condition = kwargs.get('post_condition', None)

			# restore default similarity
			Settings.MinSimilarity = 0.7
			self.similarity = Settings.MinSimilarity

	def do(self, *args, **kwargs):
		"""
        Interacts with gui elements and checks condition after action.

        action  --> can be click, doubleclick, rightclick, type, etc.
        args[0] --> image of gui element to interact with (click targe)
        args[1] --> image of the state of the app to check after action (post condition)
        kwargs['timeout'] --> timeout value for post condition check (default = 5.0)
        """
		# log arguments
		# self.log_arguments('BEGINNING OF DO', *args, **kwargs)

		# Check for valid arguments - - - - - - - - - - - - - - - - -  - - - - - - - -

		if len(args) == 0 or not args[0]:
			raise ValueError('At least one argument (click target) is required')

		# If only one argument given
		elif len(args) < 2:
			# Store it with meaningful name/key
			self.click_target = args[0]

			# Check click_target, can not be None.
			if not isinstance(self.click_target, basestring) and \
					not isinstance(self.click_target, Pattern):
				raise ValueError('First argument (click target) must be \
				String or Pattern!')

		# If more than one argument given
		else:
			# Store given arguments with meaningful names/keys
			self.click_target = args[0]
			self.post_condition = args[1]

			# Check click_target argument, can not be None.
			if not isinstance(self.click_target, basestring) and \
					not isinstance(self.click_target, Pattern):
				raise ValueError('First argument (click target) must be \
				String or Pattern!')

			# check post_condition argument, might be None
			if not isinstance(self.post_condition, basestring) and \
					not isinstance(self.post_condition, Pattern):
				raise ValueError('Second argument (post_condition) must be \
				String or Patter!')

		# Log all passed arguments - - - - - - - - - - - - - - - - - - - - - - - - - -

		# log arguments
		# self.log_arguments('MIDDLE OF DO', *args, **kwargs)

		# first eval action then perform it - - - - - - - - - - - - - - - - - - - - -

		if self.action == 'double_click':
			action = self.reg.doubleClick
			action(self.click_target)

		elif self.action == 'context_click':
			action = self.reg.rightClick

			# perform context_click action
			action(self.click_target)

			# check post_condition until timeout
			self.check_post_condition(*args, **kwargs)

			# restore default region
			self.reg = s

		elif self.action == 'click':
			action = self.reg.click

			# perform click action
			action(self.click_target)

			# check post condition until timeout
			self.check_post_condition(*args, **kwargs)

			# restore default region
			self.reg = s

		elif self.action == 'wait_vanish':
			action = self.reg.waitVanish

			# wait until whatever disappears
			action(self.click_target, **kwargs)

			# check post condition until timeout
			# self.check_post_condition(*args, **kwargs)

			# restore default region
			self.reg = s

		elif self.action == 'type':
			action = self.reg.type

			# perform action type
			action(self.click_target)

			# check post condition until timeout
			self.check_post_condition(*args, **kwargs)

			# restore default region
			self.reg = s

		elif self.action == 'press_key':
			action = self.reg.type

			# perform action press key
			action(self.single_key)

			# check post condition until timeout
			self.check_post_condition(*args, **kwargs)

		else:
			# befor this can happen RF will throw a 'unknown keyword' error
			raise ValueError('Unknown action "%s"!' % self.action)

		# log arguments
		# self.log_arguments('END OF DO', *args, **kwargs)

	def set_region(self, image, **kwargs):
		# privateLog("HELPER SET_REGION")
		self.timeout = kwargs.get('timeout', 5.0)
		# change MinSimilarity if necessary
		self.similarity = kwargs.get('similarity', 0.7)
		Settings.MinSimilarity = float(self.similarity)

		# log given arguments
		self.log_arguments('SET_REGION', **kwargs)

		if exists(image, self.timeout):
			s.find(image)
			match = s.getLastMatch()
			region_coordinates = (match.getX(), match.getY(), match.getW(), match.getH())
			self.reg = Region(*region_coordinates)
			self.log.passed("OK. Image %s found." % image)
			self.reg.highlight(1)

		# return reg
		else:
			self.log.failed("Image %s NOT found!" % image)

		# Stellt Default Einstellung wieder her
		# setAutoWaitTimeout(120)
		# print 'AutoWaitTimeout = ' + str(Settings.AutoWaitTimeout)

		# restore default similarity
		Settings.MinSimilarity = 0.7
		self.similarity = Settings.MinSimilarity

		print 'self.reg: ', str(self.reg)
		return self.reg

	def set_similarity(self, value):
		Settings.MinSimilarity = float(value)
		self.similarity = Settings.MinSimilarity
		return self.similarity

	# ------------------------- OBSERVER --------------------------------
	def event_handler(self, event):
		print 'Entered event_handler.'
		# popup('WARNING! A FUCKED UP PICTURE APPEARED!')
		self.set_region('error_QtCore4.png', timeout=1.0)
		self.click('Ecliso_Button_OK.png')
		self.region.stopObserver()
		self.e = 'Event stopped successfully!'
		print '1. e - ', self.e

	# popup('COOL!')

	def event_observer(self):
		print 'Register Event Observer.'
		self.region.onAppear('error_QtCore4.png', self.event_handler)
		print 'Registered Event Observer.'
		self.region.observe(background=True)
		print 'Started Observer.'

	# print "wait 10 s"
	# s.wait(10)
	# -------------------------------------------------------------------

	def log_arguments(self, in_func, *args, **kwargs):
		""" - - - - - - - - - - - - - - - - - - - - - -
        Logs all arguments that are passed from  RF
        - - - - - - - - - - - - - - - - - - - - - - - -
        """

		# log given *args
		print "*args in '%s()':" % in_func
		if args is not None:
			i = 0
			for arg in args:
				print "- args[%i] = %s" % (i, arg)
				i += 1
		print '\n'

		# log given **kwargs
		if kwargs is not None:
			print "**kwargs in '%s()': " % in_func
			for key, value in kwargs.iteritems():
				print "- kwargs: %s = %s" % (key, value)
		print '\n'

		# log __init__ vars
		print "__init__(vars) in '%s()':" % in_func
		print '- self.timeout:\t\t\t', self.timeout
		print '- self.action:\t\t\t', self.action
		print '- self.click_target:\t\t', self.click_target
		print '- self.post_condition:\t\t', self.post_condition
		print '- self.similarity:\t\t', self.similarity
		print '- self.single_key:\t\t', self.single_key
		print '\n'

	# ---------------------------------- LIBRARY SELF TEST -------------------------------------

	def call_keyword(self):
		"""simple keyword without args"""
		print 'You have used the simplest keyword.'

	def pass_arguments(self, first, second='second argument'):
		"""keyword with one obligatory and one optional argument"""
		print 'First argument (obligatory): ', first
		print 'Second argument (optional): ', second

	def pass_args(self, *args):
		"""keyword with variable amount of positional args"""

		# log given *args
		print 'args is = ', args
		if args != ():
			print "This keyword was called with this *args:"
			i = 0
			for arg in args:
				print "- args[%i] = %s" % (i, arg)
				i += 1
		else:
			print 'NO *args passed.'

	def pass_kwargs(self, **kwargs):
		"""keyword with variable amount of keyworded args"""

		# log given **kwargs
		print 'kwargs is = ', kwargs
		if kwargs != {}:
			print "This keyword was called with this **kwargs:"
			for key, value in kwargs.iteritems():
				print "- kwargs: %s = %s" % (key, value)
		else:
			print 'NO **kwargs passed.'

	def pass_args_kwargs(self, *args, **kwargs):
		# log given *args
		print 'args is = ', args
		if args != ():
			print "This keyword was called with this *args:"
			i = 0
			for arg in args:
				print "- args[%i] = %s" % (i, arg)
				i += 1
		else:
			print 'NO *args passed.'

		# log given **kwargs
		print 'kwargs is = ', kwargs
		if kwargs != {}:
			print "This keyword was called with this **kwargs:"
			for key, value in kwargs.iteritems():
				print "- kwargs: %s = %s" % (key, value)
		else:
			print 'NO **kwargs passed.'

	def multiply_by_two(self, number):
		"""Returns the given number multiplied by two"""

		print "*DEBUG* [SL]: The result is always a floating point number. This keyword fails if the given `number` cannot be converted to number."
		return float(number) * 2

	def numbers_should_be_equal(self, first, second):
		print '*DEBUG* [SL]: Got arguments %s and %s' % (first, second)
		print '*DEBUG* [SL]: This keyword fails if given args are not numbers or are not equal.'
		if float(first) != float(second):
			raise AssertionError('Given numbers are unequal!')

	# -------------------------- CALC TEST ---------------------------------------------------

	def start_app(self):
		calcApp = App("Rechner")
		if not calcApp.window():
			App.open("calc.exe")
			s.wait(2)
		calcApp.focus()
		s.wait(1)

	def verify_app(self):
		# check application
		if exists("CalcApp.png"):
			self.log.passed("Calculator window appeared")
		else:
			self.log.failed("No calculator window")

	def perform_action(self, *args):
		# get application region
		s.find("CalcApp.png")
		r = Region()
		r.exists("test.png")

		match = s.getLastMatch()
		self.appCoordinates = (match.getX(), match.getY(), match.getW(), match.getH())
		self.reg = Region(*self.appCoordinates)

		# rewrite action
		action = args[1]
		if args[1] == '+':
			action = 'Plus'
		elif args[1] == 'exp':
			action = 'Exp'

		self.reg.click("btnC.png")

		self.reg.click("btn%s.png" % (args[0],))
		self.reg.click("btn%s.png" % (action,))
		self.reg.click("btn%s.png" % (args[2],))

		self.reg.click("btnEqual.png")

	def verify_result(self, *args):
		expected_result = str(eval(''.join(args)))
		actual_result = self.get_result_from_clipboard()

		# verification
		if actual_result == expected_result:
			self.log.passed("Action performed correctly and result equals %s" % expected_result)
		else:
			self.log.failed(
				"Actual result '%s' is not equal to expected result '%s'" % (actual_result, expected_result))

	def get_result_from_clipboard(self):
		type('c', KEY_CTRL)
		return str(Env.getClipboard())
