# Creating Project Automated
## Co to je?
Příkaz, který Vám vytvoří složku ve složce s projekty a vytvoří repozitář, kam pushne `README.md` a otevře VS Code

## Co je třeba?
- Nainstalovaný python
- Nainstalovaný modul Selenium

## Jak nastavit?
- Uvnitř __create-project.bat__ změnit `cesta ke složce s projekty` na cestu ke složce s projekty např. E:\MojeProjekty a `username` na Vaše jméno na Githubu.
- Uvnitř __create.py__ nastavit `USERNAME` a `PASSWORD` = Přihlášení do Githubu a `path` = cesta ke složce s projekty
- Přidat tuto složku do `PATH`
- Pokud nemáte VS Code, smažte poslední řádek v `create-project.bat`