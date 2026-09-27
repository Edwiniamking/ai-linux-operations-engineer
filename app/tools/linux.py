import platform
import shutil
import socket
import time
import psutil


def get_system_info():
    """Collect basic information about the Linux system."""
    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.platform(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
    }


def get_disk_usage(path="/"):
    """Collect disk utilization information."""
    total, used, free = shutil.disk_usage(path)
    gb = 1024 ** 3

    return {
        "filesystem": path,
        "total_gb": round(total / gb, 2),
        "used_gb": round(used / gb, 2),
        "free_gb": round(free / gb, 2),
        "percent_used": round((used / total) * 100, 2),
    }


def get_memory_usage():
    """Collect system memory utilization."""
    memory = psutil.virtual_memory()
    gb = 1024 ** 3

    return {
        "total_gb": round(memory.total / gb, 2),
        "available_gb": round(memory.available / gb, 2),
        "used_gb": round(memory.used / gb, 2),
        "percent_used": memory.percent,
    }


def get_cpu_usage():
    """Collect CPU utilization."""
    return {
        "cpu_count": psutil.cpu_count(),
        "cpu_percent": psutil.cpu_percent(interval=1),
    }


def get_uptime():
    """Return system uptime in hours."""
    uptime_seconds = time.time() - psutil.boot_time()

    return {
        "uptime_hours": round(uptime_seconds / 3600, 2)
    }
