#!/usr/bin/env python3
"""
ServerGuard CLI - Professional Server Management Tool
A robust command-line interface for server administration, auditing, and monitoring.

INSTALACIÓN Y USO:
1. Guarda este archivo como: serverguard.py
2. Dale permisos de ejecución: chmod +x serverguard.py (Linux/Mac)
3. Ejecuta: python serverguard.py --help
4. Prueba comandos: python serverguard.py system status
"""

import sys
import argparse
from datetime import datetime
from typing import List, Dict, Any


# Color codes compatible with Windows and Linux
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'

    @staticmethod
    def disable():
        Colors.RESET = ''
        Colors.RED = ''
        Colors.GREEN = ''
        Colors.YELLOW = ''
        Colors.BLUE = ''
        Colors.CYAN = ''
        Colors.GRAY = ''
        Colors.BOLD = ''


# Símbolos de estado
SYMBOL_OK = '✔'
SYMBOL_ERROR = '✖'
SYMBOL_WARNING = '⚠'
SYMBOL_INFO = 'ℹ'


def print_header(text: str):
    """Imprime un encabezado de sección"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{text}{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * len(text)}{Colors.RESET}")


def print_success(text: str):
    """Mensaje de éxito"""
    print(f"{Colors.GREEN}{SYMBOL_OK}{Colors.RESET} {text}")


def print_error(text: str):
    """Mensaje de error"""
    print(f"{Colors.RED}{SYMBOL_ERROR}{Colors.RESET} {text}")


def print_warning(text: str):
    """Mensaje de advertencia"""
    print(f"{Colors.YELLOW}{SYMBOL_WARNING}{Colors.RESET} {text}")


def print_info(text: str):
    """Mensaje informativo"""
    print(f"{Colors.BLUE}{SYMBOL_INFO}{Colors.RESET} {text}")


def print_table(headers: List[str], rows: List[List[str]], col_widths: List[int] = None):
    """Imprime una tabla formateada"""
    if not col_widths:
        col_widths = [max(len(str(row[i])) for row in [headers] + rows) + 2 for i in range(len(headers))]

    # Encabezados
    header_line = "  ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    print(f"\n{Colors.BOLD}{header_line}{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * (sum(col_widths) + 2 * (len(headers) - 1))}{Colors.RESET}")

    # Filas
    for row in rows:
        row_line = "  ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row)))
        print(row_line)


# ============================================================================
# COMANDO: system
# ============================================================================
def cmd_system_status(args):
    """Muestra el estado del sistema"""
    print_header("SYSTEM STATUS")

    # Datos simulados
    metrics = [
        ("CPU Usage", "45%", "OK"),
        ("Memory", "8.2/16 GB", "OK"),
        ("Disk /", "124/500 GB", "OK"),
        ("Disk /data", "890/1000 GB", "WARNING"),
        ("Network eth0", "UP", "OK"),
        ("Load Average", "2.15, 1.98, 1.85", "OK"),
        ("Uptime", "15 days, 7 hours", "OK"),
    ]

    for name, value, status in metrics:
        if status == "OK":
            symbol = f"{Colors.GREEN}{SYMBOL_OK}{Colors.RESET}"
        elif status == "WARNING":
            symbol = f"{Colors.YELLOW}{SYMBOL_WARNING}{Colors.RESET}"
        else:
            symbol = f"{Colors.RED}{SYMBOL_ERROR}{Colors.RESET}"

        print(f"{symbol} {Colors.BOLD}{name:<20}{Colors.RESET} {value}")

    print()


def cmd_system_services(args):
    """Lista servicios del sistema"""
    print_header("SYSTEM SERVICES")

    services = [
        ["nginx", "active", "running", "16d 7h"],
        ["postgresql", "active", "running", "16d 7h"],
        ["redis", "active", "running", "16d 7h"],
        ["docker", "active", "running", "16d 7h"],
        ["ufw", "inactive", "stopped", "-"],
    ]

    headers = ["SERVICE", "STATE", "STATUS", "UPTIME"]

    colored_services = []
    for svc in services:
        name = svc[0]
        state = svc[1]

        if state == "active":
            state_str = f"{Colors.GREEN}{state}{Colors.RESET}"
        else:
            state_str = f"{Colors.GRAY}{state}{Colors.RESET}"

        colored_services.append([name, state_str, svc[2], svc[3]])

    print_table(headers, colored_services, [20, 12, 12, 15])
    print()


def cmd_system_resources(args):
    """Muestra uso de recursos"""
    print_header("RESOURCE USAGE")

    print(f"\n{Colors.BOLD}CPU:{Colors.RESET}")
    print(f"  Core 1: {'█' * 15}{'░' * 35} 30%")
    print(f"  Core 2: {'█' * 22}{'░' * 28} 45%")
    print(f"  Core 3: {'█' * 18}{'░' * 32} 35%")
    print(f"  Core 4: {'█' * 25}{'░' * 25} 50%")

    print(f"\n{Colors.BOLD}Memory:{Colors.RESET}")
    print(f"  Used:  {'█' * 25}{'░' * 25} 51% (8.2 GB / 16 GB)")

    print(f"\n{Colors.BOLD}Disk:{Colors.RESET}")
    print(f"  /      {'█' * 12}{'░' * 38} 24% (124 GB / 500 GB)")
    print(f"  /data  {'█' * 44}{'░' * 6} {Colors.YELLOW}89%{Colors.RESET} (890 GB / 1000 GB)")
    print()


# ============================================================================
# COMANDO: logs
# ============================================================================
def cmd_logs_tail(args):
    """Muestra logs recientes"""
    print_header(f"LOGS: {args.service or 'system'}")

    log_entries = [
        ("2024-12-14 14:32:15", "INFO", "nginx", "Request processed successfully"),
        ("2024-12-14 14:32:18", "INFO", "app", "User login: admin"),
        ("2024-12-14 14:32:22", "WARNING", "postgresql", "Slow query detected (2.3s)"),
        ("2024-12-14 14:32:25", "ERROR", "app", "Failed to connect to API endpoint"),
        ("2024-12-14 14:32:28", "INFO", "nginx", "SSL certificate renewed"),
    ]

    print()
    for timestamp, level, service, message in log_entries[-int(args.lines):]:
        if level == "INFO":
            level_str = f"{Colors.BLUE}INFO{Colors.RESET}"
        elif level == "WARNING":
            level_str = f"{Colors.YELLOW}WARN{Colors.RESET}"
        else:
            level_str = f"{Colors.RED}ERROR{Colors.RESET}"

        print(f"{Colors.GRAY}{timestamp}{Colors.RESET} {level_str} {Colors.CYAN}[{service}]{Colors.RESET} {message}")
    print()


def cmd_logs_search(args):
    """Busca en los logs"""
    print_header(f"LOG SEARCH: '{args.query}'")
    print_info(f"Searching in: {args.service or 'all services'}")
    print_info(f"Time range: last {args.hours} hours")

    print(f"\n{Colors.GREEN}Found 3 matches:{Colors.RESET}\n")

    matches = [
        ("2024-12-14 12:15:30", "ERROR", "app", "Failed to connect to API endpoint"),
        ("2024-12-14 13:42:18", "ERROR", "app", "Connection timeout to API"),
        ("2024-12-14 14:32:25", "ERROR", "app", "Failed to connect to API endpoint"),
    ]

    for timestamp, level, service, message in matches:
        highlighted = message.replace(args.query, f"{Colors.BOLD}{Colors.YELLOW}{args.query}{Colors.RESET}")
        print(
            f"{Colors.GRAY}{timestamp}{Colors.RESET} {Colors.RED}ERROR{Colors.RESET} {Colors.CYAN}[{service}]{Colors.RESET} {highlighted}")
    print()


# ============================================================================
# COMANDO: users
# ============================================================================
def cmd_users_list(args):
    """Lista usuarios del sistema"""
    print_header("SYSTEM USERS")

    users = [
        ["admin", "1000", "sudo,docker", "2024-12-14 08:30", "active"],
        ["deploy", "1001", "docker", "2024-12-13 18:45", "active"],
        ["monitor", "1002", "monitoring", "2024-12-12 09:15", "active"],
        ["backup", "1003", "backup", "2024-11-28 14:20", "inactive"],
    ]

    headers = ["USERNAME", "UID", "GROUPS", "LAST LOGIN", "STATUS"]

    colored_users = []
    for user in users:
        status = user[4]
        if status == "active":
            status_str = f"{Colors.GREEN}{SYMBOL_OK} {status}{Colors.RESET}"
        else:
            status_str = f"{Colors.GRAY}{SYMBOL_WARNING} {status}{Colors.RESET}"

        colored_users.append([user[0], user[1], user[2], user[3], status_str])

    print_table(headers, colored_users, [15, 8, 20, 20, 15])
    print()


def cmd_users_sessions(args):
    """Muestra sesiones activas"""
    print_header("ACTIVE SESSIONS")

    sessions = [
        ["admin", "pts/0", "192.168.1.100", "08:30", "6h 2m"],
        ["deploy", "pts/1", "10.0.0.50", "13:15", "1h 17m"],
    ]

    headers = ["USER", "TTY", "FROM", "LOGIN", "IDLE"]
    print_table(headers, sessions)

    print(f"\n{Colors.BOLD}Total active sessions:{Colors.RESET} 2")
    print()


# ============================================================================
# COMANDO: audit
# ============================================================================
def cmd_audit_scan(args):
    """Ejecuta escaneo de seguridad"""
    print_header("SECURITY AUDIT")
    print_info("Scanning system configuration...")

    print("\n" + Colors.BOLD + "Security Checks:" + Colors.RESET)

    checks = [
        ("SSH root login disabled", True),
        ("Firewall enabled", False),
        ("Automatic updates configured", True),
        ("Password policy enforced", True),
        ("Unnecessary services disabled", True),
        ("SSL certificates valid", True),
        ("File permissions secure", False),
    ]

    passed = sum(1 for _, status in checks if status)
    total = len(checks)

    for check, status in checks:
        if status:
            print_success(check)
        else:
            print_error(check)

    print(f"\n{Colors.BOLD}Results:{Colors.RESET} {passed}/{total} checks passed")

    if passed == total:
        print_success("System security: EXCELLENT")
    elif passed >= total * 0.7:
        print_warning("System security: GOOD (review warnings)")
    else:
        print_error("System security: NEEDS ATTENTION")
    print()


def cmd_audit_compliance(args):
    """Verifica cumplimiento de políticas"""
    print_header("COMPLIANCE CHECK")

    policies = [
        ["Password Policy", "PASS", "All users comply"],
        ["Backup Policy", "PASS", "Last backup: 2h ago"],
        ["Update Policy", "WARN", "3 updates pending"],
        ["Access Control", "PASS", "No violations found"],
        ["Encryption", "FAIL", "/data not encrypted"],
    ]

    headers = ["POLICY", "STATUS", "DETAILS"]

    colored_policies = []
    for policy in policies:
        status = policy[1]
        if status == "PASS":
            status_str = f"{Colors.GREEN}{SYMBOL_OK} {status}{Colors.RESET}"
        elif status == "WARN":
            status_str = f"{Colors.YELLOW}{SYMBOL_WARNING} {status}{Colors.RESET}"
        else:
            status_str = f"{Colors.RED}{SYMBOL_ERROR} {status}{Colors.RESET}"

        colored_policies.append([policy[0], status_str, policy[2]])

    print_table(headers, colored_policies, [20, 15, 30])
    print()


# ============================================================================
# COMANDO: report
# ============================================================================
def cmd_report_generate(args):
    """Genera reporte del sistema"""
    print_header(f"GENERATING {args.type.upper()} REPORT")

    print_info(f"Period: {args.period}")
    print_info(f"Format: {args.format}")
    print()

    print("Processing...")
    print(f"  {Colors.GREEN}✓{Colors.RESET} Collecting system metrics")
    print(f"  {Colors.GREEN}✓{Colors.RESET} Analyzing logs")
    print(f"  {Colors.GREEN}✓{Colors.RESET} Gathering security data")
    print(f"  {Colors.GREEN}✓{Colors.RESET} Compiling statistics")

    filename = f"serverguard_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"

    print()
    print_success(f"Report generated: {filename}")
    print_info(f"Location: /var/log/serverguard/reports/{filename}")
    print()


# ============================================================================
# CLI Setup
# ============================================================================
def main():
    parser = argparse.ArgumentParser(
        prog='serverguard',
        description='Professional server management, auditing, and monitoring tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  serverguard system status              Show system status
  serverguard logs tail --lines 50       Show last 50 log entries
  serverguard audit scan                 Run security audit
  serverguard users list                 List system users
  serverguard report generate daily      Generate daily report

For more information, visit: https://serverguard.example.com
        '''
    )

    parser.add_argument('--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('--version', action='version', version='ServerGuard CLI v2.4.1')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # SYSTEM
    system_parser = subparsers.add_parser('system', help='System monitoring and status')
    system_sub = system_parser.add_subparsers(dest='subcommand')

    system_sub.add_parser('status', help='Show overall system status')
    system_sub.add_parser('services', help='List system services')
    system_sub.add_parser('resources', help='Display resource usage')

    # LOGS
    logs_parser = subparsers.add_parser('logs', help='Log management and analysis')
    logs_sub = logs_parser.add_subparsers(dest='subcommand')

    tail_parser = logs_sub.add_parser('tail', help='Show recent log entries')
    tail_parser.add_argument('--service', help='Filter by service name')
    tail_parser.add_argument('--lines', default='10', help='Number of lines (default: 10)')

    search_parser = logs_sub.add_parser('search', help='Search in logs')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--service', help='Filter by service')
    search_parser.add_argument('--hours', default='24', help='Time range in hours (default: 24)')

    # USERS
    users_parser = subparsers.add_parser('users', help='User management and sessions')
    users_sub = users_parser.add_subparsers(dest='subcommand')

    users_sub.add_parser('list', help='List system users')
    users_sub.add_parser('sessions', help='Show active sessions')

    # AUDIT
    audit_parser = subparsers.add_parser('audit', help='Security auditing and compliance')
    audit_sub = audit_parser.add_subparsers(dest='subcommand')

    audit_sub.add_parser('scan', help='Run security scan')
    audit_sub.add_parser('compliance', help='Check policy compliance')

    # REPORT
    report_parser = subparsers.add_parser('report', help='Generate system reports')
    report_sub = report_parser.add_subparsers(dest='subcommand')

    gen_parser = report_sub.add_parser('generate', help='Generate report')
    gen_parser.add_argument('type', choices=['daily', 'weekly', 'monthly'], help='Report type')
    gen_parser.add_argument('--period', default='last-24h', help='Time period (default: last-24h)')
    gen_parser.add_argument('--format', choices=['pdf', 'html', 'json'], default='pdf', help='Output format')

    args = parser.parse_args()

    if args.no_color:
        Colors.disable()

    if not args.command:
        parser.print_help()
        return

    # Routing
    try:
        if args.command == 'system':
            if args.subcommand == 'status':
                cmd_system_status(args)
            elif args.subcommand == 'services':
                cmd_system_services(args)
            elif args.subcommand == 'resources':
                cmd_system_resources(args)
            else:
                system_parser.print_help()

        elif args.command == 'logs':
            if args.subcommand == 'tail':
                cmd_logs_tail(args)
            elif args.subcommand == 'search':
                cmd_logs_search(args)
            else:
                logs_parser.print_help()

        elif args.command == 'users':
            if args.subcommand == 'list':
                cmd_users_list(args)
            elif args.subcommand == 'sessions':
                cmd_users_sessions(args)
            else:
                users_parser.print_help()

        elif args.command == 'audit':
            if args.subcommand == 'scan':
                cmd_audit_scan(args)
            elif args.subcommand == 'compliance':
                cmd_audit_compliance(args)
            else:
                audit_parser.print_help()

        elif args.command == 'report':
            if args.subcommand == 'generate':
                cmd_report_generate(args)
            else:
                report_parser.print_help()

    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Operation cancelled by user{Colors.RESET}")
        sys.exit(130)
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
