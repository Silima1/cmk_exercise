#!/usr/bin/python3


import subprocess

def get_uptime():
    uptime_output = subprocess.check_output("uptime", shell=True).decode()
    return uptime_output.strip()

def get_cpu_load():
    load_output = subprocess.check_output("cat /proc/loadavg", shell=True).decode()
    load_values = load_output.split()[:3]
    return " ".join(load_values)

def get_memory_usage():
    mem_output = subprocess.check_output("free -m | grep Mem", shell=True).decode()
    mem_values = mem_output.split()[1:4]
    return " ".join(mem_values)

if __name__ == "__main__":
    output = []

    output.append("<<<os_performance>>>")
    output.append(f"uptime: {get_uptime()}")
    output.append(f"cpu_load: {get_cpu_load()}")
    output.append(f"memory_usage: {get_memory_usage()}")

    print("\n".join(output))
