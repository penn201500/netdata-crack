# -*- coding: utf-8 -*-
import psutil

def get_cpu_total_percent():
    cpu_total_percent = psutil.cpu_percent (interval=1.0)
    return cpu_total_percent

def get_logical_cpu_number():
    logical_cpu_count = psutil.cpu_count()
    return logical_cpu_count

def get_physical_cpu_number():
    #hype thread CPUs are excluded
    physical_cpu_count = psutil.cpu_count(logical=False)
    return physical_cpu_count

def get_user_cpu_percent():
    pass

def get_system_cpu_percent():
    pass

def get_idle_cpu_percent():
    pass

def get_steal_cpu_percent():
    pass

cpu_times_percent = psutil.cpu_times_percent(interval=1.0)

print cpu_times_percent
print get_cpu_total_percent()
