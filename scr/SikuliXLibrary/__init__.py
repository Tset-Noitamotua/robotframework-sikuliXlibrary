import os
from sikuli import *
from keywords import *
from keywords import common

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))

__version__ = VERSION


class SikuliXLibrary(_SikuliX_Keywords):
	"""SikuliXLibrary is a generic GUI testing library for Robot Framework.

	It uses SikuliX ... .
	See http://sikulix.org for more information about SikuliX.

	It should work on most modern platforms and can be used with (both Python and?TODO) Jython interpreters.

	= Before running tests =
	TODO

	= Locating elements =
    TODO

	= Timeouts =
	TODO

	All timeouts can be given as numbers considered seconds (e.g. 0.5 or 42)
	"""

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	ROBOT_LIBRARY_VERSION = VERSION

	def __init__(self, image_path='images', timeout=5.0, similarity=0.7, greeting='World', single_key=Key.F1):
		"""SikuliXLibrary can be imported with optional arguments.

        `timeout` is the default timeout used to wait for all TODO.
        It can be later set with `TODO`.

        'implicit_wait' is the implicit timeout that Selenium waits when
        looking for elements. TODO: Do we need this in SikuliXLibrary, too?
        It can be later set with TODO `Set SikuliX Implicit Wait`.

        TODO: Library import examples:
        | Library `|` SikuliXLibrary `|` 15         | # Sets default timeout to 15 seconds
        | Library `|` SikuliXLibrary `|` timeout=10 | # Sets default timeout to 10 seconds
        """
		self.greeting = greeting
		self.timeout = timeout
		self.similarity = similarity
		self.single_key = single_key

		self.appCoordinates = (0, 0, 1024, 768)
		# self.action = 'click'
		self.click_target = None
		self.post_condition = None
		self.location = None
		self.press_key = None
		# self.reg = Region(s)
		self.region = Region.create(Screen(0).x, Screen(0).y, Screen(0).w, Screen(0).h)
		self.region = Region(self.region)

		self.image_path = image_path
		common.cfgImageLibrary = self.image_path
		addImagePath(common.cfgImageLibrary)

		for base in SikuliXLibrary.__bases__:
			base.__init__(self)

		##########addImagePath(common.cfgImageLibrary)
		# self.set_selenium_timeout(timeout)
		# self.set_selenium_implicit_wait(implicit_wait)
		# self.register_keyword_to_run_on_failure(run_on_failure)

	def log_library_arguments(self):
		if self.greeting == 'World' and self.timeout == 5.0 and self.similarity == 0.7 \
				and self.image_path == 'images':
			print 'NO library args passed! SikuliXLibrary imported with defaults:\n'
			print 'greeting:\t\t', self.greeting
			print 'timeout:\t\t', self.timeout
			print 'similarity:\t\t', self.similarity
			print 'image_path:\t\t', self.image_path
			print '- self.single_key:\t\t', self.single_key
		else:
			print 'SikuliXLibrary imported with this FUCKING arguments:\n'
			print 'greeting:\t\t', self.greeting
			print 'timeout:\t\t', self.timeout
			print 'similarity:\t\t', self.similarity
			print 'image_path:\t\t', self.image_path
			print 'cfgImageLibrary:\t', common.cfgImageLibrary
			print '- self.single_key:\t\t', self.single_key
