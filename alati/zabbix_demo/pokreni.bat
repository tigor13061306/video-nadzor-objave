@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Pokrecem demo Zabbix (prvi put skida slike, moze trajati nekoliko minuta)...
docker compose up -d
echo.
echo Rezija radi, snimci idu u folder snimci. Ovaj prozor mozete zatvoriti.
docker compose logs -f rezija
