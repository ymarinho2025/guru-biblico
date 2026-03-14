@echo off
title Guru Biblico IA
cd /d "%USERPROFILE%\Downloads\Guru Biblico\Bible-API"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python nao encontrado no PATH.
    pause
    exit
)

python bible-api.py
pause
