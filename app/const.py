path = r'/app/downloads/victims.zip'
name = 'Victims_Age_by_Offense_Category_2022.xlsx'  
header=[3,4]
skipfooter=1
skiprows=lambda x:x in [5,5]

session_command_tuple= ("POST", '/session/$sessionId/chromium/send_command')
prefs={
            "download.default_directory": "/app/mydownloads",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
command_executor='http://selenium-chrome:4444/wd/hub'
downloads_dir='/app/mydownloads'
url = 'https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home'
doc_down='#hr-docs-action-lbl'
tables_list='#dwnnibrs-download-select > button'
table="Victims"
years_list='#dwnnibrscol-year-select > button'
year="2022"
locations_list='#dwnnibrsloc-select > button'
location="Florida"
download='#nibrs-download-button'