from fastapi import FastAPI

from app.tools.linux import (
    get_system_info,
    get_disk_usage,
    get_memory_usage,
    get_cpu_usage,
    get_uptime,
)

app = FastAPI(
    title="AI Linux Operations Engineer",
    description="Linux monitoring and AI-assisted operations API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "application": "AI Linux Operations Engineer",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/system")
def system():
    return get_system_info()


@app.get("/disk")
def disk():
    return get_disk_usage("/")


@app.get("/memory")
def memory():
    return get_memory_usage()


@app.get("/cpu")
def cpu():
    return get_cpu_usage()


@app.get("/uptime")
def uptime():
    return get_uptime()


@app.get("/diagnostics")
def diagnostics():
    return {
        "system": get_system_info(),
        "disk": get_disk_usage("/"),
        "memory": get_memory_usage(),
        "cpu": get_cpu_usage(),
        "uptime": get_uptime(),
    }
