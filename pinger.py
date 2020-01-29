#!/usr/bin/env python3

import subprocess

# Ping command
def ping(host,count):
    try:
        cmd_ping = subprocess.check_output(["ping",host,"-c",str(count)])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    ping("10.0.2.1",2)

if __name__ == "__main__":
    main()