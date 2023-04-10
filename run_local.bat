@REM before using this script, activate venv by running activate/activate.bat in venv/Script folder

@@echo off

set API_KEY=my-key
uvicorn web_service:app --reload