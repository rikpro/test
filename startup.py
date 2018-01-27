"""
 Startup script for E3-cable
 - reads config file
 - configures database
 - loads user menu

To start this script automatically when starting e3.cable, the following string key must be added in the registery:
HKEY_LOCAL_MACHINE\SOFTWARE\Zuken\e3.series\<version>\ConfigureAddOnsMenu 
The key value should be the full path and name of the startup script:
<scriptpath>Startup.vbs


 Versions:
 0.01   16/01/2013  RPR     Initial Version 
 
"""
__version__ = "0.01"
__author__ = "RPR"
__date__ = "16/01/2012"
__change__ = "Initial Version"

def main():
    print "testscript"


