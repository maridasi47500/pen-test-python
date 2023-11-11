import re
import subprocess
device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb")
devices = []
for i in df.split(b'\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
            devices.append(dinfo)
            
for i in devices:
  if b"Apple" in i["tag"]:
    #print(i)
    #print(i["device"].split("/")[4])
    print(i["tag"]+b"\n")
    if i["device"].split("/")[4] == "b'001'":
      print("le telephone est branché en tethering au bon port usb")
    else:
      print("le telephone est branché en tethering au mauvais port usb. ne branchez pas le telephone sur le port bleu")
