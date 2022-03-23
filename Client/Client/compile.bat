@echo off
CALL "C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools\VsDevCmd.bat"
cd %~dp0
msbuild LorderonBin.sln /property:Configuration=Release /maxcpucount -target:Clean
msbuild LorderonBin.sln /property:Configuration=Release /maxcpucount
pause