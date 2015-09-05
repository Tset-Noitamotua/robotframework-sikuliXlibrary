@echo off

set sikulix_jar=C:\SikuliX_110\sikulixapi.jar

set CLASSPATH=%sikulix_jar%
set JYTHONPATH=%sikulix_jar%/Lib

jybot --pythonpath=..\scr ^
	  --outputdir=results ^
      --loglevel=TRACE ^
	  library_self_test.robot ^
      %*