@echo off
title Iniciador de Systemic Play
color 0a

echo ====================================================
echo   CERRANDO PROCESOS TRABADOS DE PYTHON EN TU PC...
echo ====================================================
:: Cierra cualquier servidor fantasma que este ocupando el puerto 8080
taskkill /f /im python.exe 2>nul
taskkill /f /im pythonw.exe 2>nul

echo.
echo ====================================================
echo   INICIANDO SERVIDOR FLASK (PORT 8080)...
echo ====================================================
:: Ejecuta tu aplicacion directamente
"%USERPROFILE%\AppData\Local\Programs\Python\Python314\python.exe" app.py

echo.
echo El servidor se ha detenido.
pause