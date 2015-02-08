import os
import signal
import stat
import time

def file_age_in_seconds(pathname):
  return time.time() - os.stat(pathname)[stat.ST_MTIME]

def killProcess(name):
  for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
    fields = line.split()
    pid = fields[0]
    os.kill(int(pid), signal.SIGKILL)