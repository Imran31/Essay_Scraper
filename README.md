# Essay_Scraper

Python script that will extract all Paul Graham Essays.
Paul has amazing essays but his website is a nightmare when it comes to extracting data. His essays are enclosed in table row. The end result is a pdf for each essay, but the line breaks and formatting is nothing to be proud about. Any improvements are welcome!

## Instructions

### virtualenv

```
  pip install virtualenv
  virtualenv essay_scraper
  cd essay_scrapper
  source bin/activate
```

### pyfpdf: FPDF for Python
[Instructions from https://github.com/reingart/pyfpdf]

You can also install PyFPDF from PyPI, with easyinstall or from Windows 
installers. For example, using pip:
```
   pip install fpdf
```
## Run

Copy crawley.py into essay_scraper directory and run the script. The script will take some time to finish execution, the directoty will be populated with a new pdf file for each essay.

## Contribute

The essays don't look so great but it is readable and I welcome everyone to contribute!
