@echo off
cd /d "%~dp0"
echo Pravim grafove iz postojecih podataka...
docker compose run --rm rezija bash -c "pip install -q playwright==1.49.0 requests && python /app/grafovi.py"
echo Gotovo. Ovaj prozor mozete zatvoriti.
