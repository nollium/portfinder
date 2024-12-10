import psutil
from rich.table import Table
from rich.console import Console
from rich.text import Text
from datetime import datetime
from typing import List
import sys


def list_bound_ports(filter_ports: List[int] = None) -> List[dict]:
    bound_ports = []

    for conn in psutil.net_connections(kind='inet'):
        if conn.status == psutil.CONN_LISTEN:
            if filter_ports and conn.laddr[1] not in filter_ports:
                continue
            try:
                process = psutil.Process(conn.pid)
                cmdline = process.cmdline() if process.cmdline() else [process.exe()]
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


def format_cmdline(cmdline: List[str]) -> Text:
    text = Text()
    colors = ["yellow", "green", "cyan", "magenta", "red", "blue"]

    for i, arg in enumerate(cmdline):
        color = colors[i % len(colors)]
        text.append(arg, style=color)
        if i < len(cmdline) - 1:
            text.append(" ")

    return text


def display_ports(ports: List[dict]) -> None:
    console = Console()

    if not ports:
        console.print("[bold red]No processes are currently binding on any address or port.[/bold red]")
        return

    table = Table(title="Processes Binding on Address + Port", show_lines=True)

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
            format_cmdline(port['cmdline']),
            port['creation_date']
        )

    console.print(table)


if __name__ == "__main__":
    # Parse command-line arguments for ports
    if len(sys.argv) > 1:
        try:
            filter_ports = [int(port) for port in sys.argv[1:]]
        except ValueError:
            print("Please provide valid port numbers.")
            sys.exit(1)
    else:
        filter_ports = None

    bound_ports = list_bound_ports(filter_ports)
    display_ports(bound_ports)
