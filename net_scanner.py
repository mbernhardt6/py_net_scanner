#!/usr/local/bin/python2.7

#Modules
import logger
import marklib
import nettools
import nmap_scan
import os

#Variables
output = "xml"
folder = "/home/<user>/netscan/"
newscan = folder + "newscan.xml"
htmlreport = "/var/www/html/nmapscan.html"
log = "/var/log/net_scanner.log"
lock = folder + "lock"

def runScan():
  logger.logMessage(log, "Setting lock file before starting.")
  open(lock, 'a').close()
  logger.logMessage(log, "Starting nmap scan of local network.")
  subnet = nettools.findSubnet()
  logger.logMessage(log, "Using %s as local subnet." % subnet)
  nmapExitCode = nmap_scan.nmapScan(subnet, output, newscan)
  logger.logMessage(log, "nmap scan completed with exit code %s" % nmapExitCode)
  reportExitCode = nmap_scan.generateReport(newscan, htmlreport)
  logger.logMessage(log, "Report generated with exit code %s" % reportExitCode)
  os.remove(lock)
  logger.logMessage(log, "Lock file removed.")

if __name__ == "__main__":
  if (os.path.isfile(lock)):
    lockage = marklib.file_age_in_seconds(lock)
    if (lockage > 10800):
      logger.logMessage(log, "Removing stale lock file.")
      os.remove(lock)
      logger.logMessage(log, "Killing stale processes.")
      marklib.killProcess("nmap")
      runScan()
    else:
      logger.logMessage(log, "Lock file detected. Aborting. Age:%s seconds" % lockage)
  else:
    runScan()