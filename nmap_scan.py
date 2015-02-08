import subprocess

def nmapScan(subnet, output_type, output_file):
  stylesheet = "/home/<user>/netscan/nmap.xsl"
  if output_type == "xml":
    out_switch = "-oX"
  else:
    out_switch = "-oN"
  ExitCode = subprocess.call("nmap -O %s %s --stylesheet %s %s" % (out_switch, output_file, stylesheet, subnet), shell=True)
  return ExitCode

def generateReport(xml_file, html_file):
  ExitCode = subprocess.call("xsltproc %s -o %s" % (xml_file, html_file), shell=True)
  return ExitCode
