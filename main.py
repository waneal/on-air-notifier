import os, subprocess

from PyP100 import PyP100

DEVICE_IP = os.environ["TP_LINK_DEVICE_IP"]
EMAIL = os.environ["TP_LINK_EMAIL"]
PASSWORD = os.environ["TP_LINK_PASSWORD"]

p100 = PyP100.P100(DEVICE_IP, EMAIL, PASSWORD)
p100.handshake()
p100.login()

# get cpu usage(%) of krisp
cpu_usage = float(subprocess.getoutput(["ps -o %cpu -o comm -ax | grep krisp | awk '{print $1}'"]))

# when krisp is used as cpu usage is more than 10 % on my macbook
if cpu_usage > 5:
    p100.turnOn()
else:
    p100.turnOff()
