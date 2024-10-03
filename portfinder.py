import psutil
from rich.table import Table
from rich.console import Console
from datetime import datetime
from typing import List


def list_bound_ports() -> List[dict]:
    bound_ports = []

    for conn in psutil.net_connections(kind='inet'):
        if conn.status == psutil.CONN_LISTEN:
            try:
                process = psutil.Process(conn.pid)
                cmdline = ' '.join(process.cmdline()) if process.cmdline() else process.exe()
                bound_ports.append({
                    'interface': conn.laddr[0],
                    'port': conn.laddr[1],
                    'pid': str(process.pid),
                    'cmdline': cmdline,
                    'creation_date': datetime.fromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    return bound_ports


def display_ports(ports: List[dict]) -> None:
    console = Console()

    if not ports:
        console.print("[bold red]No processes are currently binding on any address or port.[/bold red]")
        return

    table = Table(title="Processes Binding on Address + Port")

    table.add_column("Interface", style="cyan", no_wrap=True)
    table.add_column("Port", style="magenta")
    table.add_column("PID", style="red")
    table.add_column("Cmdline", style="yellow", overflow="fold")
    table.add_column("Creation Date", style="blue")

    for port in ports:
        table.add_row(
            port['interface'],
            str(port['port']),
            port['pid'],
            port['cmdline'],
            port['creation_date']
        )

    console.print(table)


if __name__ == "__main__":
    bound_ports = list_bound_ports()
    display_ports(bound_ports)
