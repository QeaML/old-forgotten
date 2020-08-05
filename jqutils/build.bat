@echo off

:: Compiling
echo ----- Compiling -----
for /r src %%i in (*.java) do (
	echo Compiling %%i...
	javac -cp src "%%i"
)

:: Packaging
echo ----- Packaging -----
echo Creating temporary folder...
if exist pkg rmdir pkg /s /q
mkdir pkg
echo Copying compiled files...
xcopy src\*.class .\pkg /E
echo Creating JAR...
if exist jqutils.jar del jqutils.jar
jar cvf jqutils.jar -C pkg .

:: Cleaning
echo ----- Cleaning up -----
echo Deleting temporary folder...
rmdir pkg /s /q
echo Deleting class files...
for /r src %%i in (*.class) do (
	del "%%i"
)
echo Done!