@echo off
::�����ļ�����
set time_hh=%time:~0,2%
if /i %time_hh% LSS 10 (set time_hh=0%time:~1,1%)
set filename=%date:~,4%%date:~5,2%%date:~8,2%_%time_hh%%time:~3,2%%time:~6,2%

@echo on
@echo "���ڼ�¼log����ctrl + c ֹͣץȡ"
@adb logcat > log/%filename%.txt