@echo off

IF NOT EXIST ".\PythonEnv" (
  py -m venv ".\PythonEnv"
)


IF EXIST "PythonEnv" (
  call ".\PythonEnv\Scripts\activate.bat"
  python --version
)
