#Sysinfo function credits https://stackoverflow.com/a/1996085
import os,re

def get_fingerprint():
    values = {};

    def SysInfo():
        cache = os.popen2("SYSTEMINFO")
        source = cache[1].read()
        sysOpts = ["Host Name", "OS Name", "OS Version", "Product ID", "System Manufacturer", "System Model", "BIOS Version"]
        for opt in sysOpts:
            values[opt] = [item.strip() for item in re.findall("%s:\w*(.*?)\n" % (opt), source, re.IGNORECASE)][0]

    def get_uuid():
        values['UUID'] = os.popen2("wmic csproduct get UUID")[1].read().split("\n")[1].strip();

    def get_sys_env():
        values['username'] = os.getenv('username');
        values['computername'] = os.getenv('COMPUTERNAME');

    def get_hdd_id():
        source  = os.popen2("wmic diskdrive get SerialNumber")[1].read().split("\n")
        values['hdd_id'] = "_".join(x.strip() for x in source[:-2])

    def get_cpu_id():
        source =os.popen2("wmic cpu get ProcessorID")[1].read().split("\n")
        values['cpu_id']= "_".join(x.strip() for x in source[:-2]);

#intialise whatever parameters u need
    SysInfo();
    get_uuid();
    get_sys_env();
    get_hdd_id();
    get_cpu_id();
    return values





