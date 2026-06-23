import psutil
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

LOG_FILE = "system_health.log"


def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    print(log_message)

    with open(LOG_FILE, "a") as file:
        file.write(log_message + "\n")


def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: CPU usage is {cpu_usage}%")

    return cpu_usage


def check_memory():
    memory = psutil.virtual_memory()

    if memory.percent > MEMORY_THRESHOLD:
        log_alert(f"ALERT: Memory usage is {memory.percent}%")

    return memory.percent


def check_disk():
    disk = psutil.disk_usage('/')

    if disk.percent > DISK_THRESHOLD:
        log_alert(f"ALERT: Disk usage is {disk.percent}%")

    return disk.percent


def check_processes():
    process_count = len(psutil.pids())
    return process_count


def main():
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    processes = check_processes()

    print("\n===== SYSTEM HEALTH REPORT =====")
    print(f"CPU Usage       : {cpu}%")
    print(f"Memory Usage    : {memory}%")
    print(f"Disk Usage      : {disk}%")
    print(f"Running Process : {processes}")
    print("================================")


if __name__ == "__main__":
    main()