from rich.console import Console
from rich.table import Table
import psutil
import socket
import platform
import time

console = Console()

table = Table(title="Linux Dashboard")

table.add_column("Info", style="cyan")
table.add_column("Value", style="green")

table.add_row("Hostname", socket.gethostname())
table.add_row("System", platform.system())
table.add_row("CPU Usage", f"{psutil.cpu_percent()}%")
table.add_row("RAM Usage", f"{psutil.virtual_memory().percent}%")
table.add_row("Disk Usage", f"{psutil.disk_usage('/').percent}%")

console.print(table)