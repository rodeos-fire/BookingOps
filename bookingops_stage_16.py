# === Stage 16: Add argparse support for the most common commands ===
# Project: BookingOps
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="BookingOps CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Resources command
    res_parser = subparsers.add_parser('resources', help='List resources')
    res_parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    # Reservations command
    resv_parser = subparsers.add_parser('reservations', help='Manage reservations')
    resv_sub = resv_parser.add_subparsers(dest='action', required=True)
    list_resv = resv_sub.add_parser('list', help='List all reservations')
    add_resv = resv_sub.add_parser('add', help='Add a new reservation')
    del_resv = resv_sub.add_parser('delete', help='Delete a reservation')
    
    # Reports command
    rep_parser = subparsers.add_parser('reports', help='Generate reports')
    rep_parser.add_argument('--utilization', action='store_true', help='Show utilization stats')
    rep_parser.add_argument('--conflicts', action='store_true', help='List conflicts')
    
    args = parser.parse_args()
    return args
