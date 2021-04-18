# Creating Project Automated
## Co to je?
Script na vytvoření nového projektu. Vytvoří novou složku, repozitář a propojí je. Ve složce dále vytvoří soubor `README.md` a otevře VSCode.

## Co je třeba?
- Nainstalovaný python
- Nainstalovaný modul Selenium (pip install selenium)

## Jak nastavit?
- Uvnitř __create-project.bat__ změnit `cesta ke složce s projekty` na cestu ke složce s projekty např. E:\MojeProjekty (pokud se složka nachází na jiném disku, je nejdříve nutné před příkazem cd změnit disk např. e:) a `username` na Vaše `jméno` na Githubu.
- Uvnitř __create.py__ nastavit `USERNAME` a `PASSWORD` = Přihlášení do Githubu a `path` = cesta ke složce s projekty
- Přidat tuto složku do `PATH`
- Pokud nemáte VS Code, smažte poslední řádek v `create-project.bat`
- Pro vytvoření nového projektu stačí napsat `create-projekt název_projektu`