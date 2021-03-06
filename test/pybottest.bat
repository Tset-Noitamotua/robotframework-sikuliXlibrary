@echo off

set sikulix_jar=C:\SikuliX_110\sikulixapi.jar
set robot_framework_jar=C:\robotframework\robotframework-2.8.7.jar

java -cp "%robot_framework_jar%;%sikulix_jar%" ^
     -Dpython.path="%sikulix_jar%/Lib" ^
     org.robotframework.RobotFramework ^
	 --pythonpath=..\scr ^
     --outputdir=results ^
     --loglevel=TRACE ^
     %*