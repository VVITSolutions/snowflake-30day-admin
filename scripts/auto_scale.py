# Auto-scale Snowflake Warehouse based on load
# Usage: python auto_scale.py --warehouse DEV_WH --size MEDIUM

import argparse
from snowflake.connector import connect

parser = argparse.ArgumentParser()
parser.add_argument('--warehouse', required=True)
parser.add_argument('--size', default='MEDIUM')
args = parser.parse_args()

# Update with your creds
conn = connect(
    user='KUMAR',
    password='your_password_here',
    account='your_account.uk-east-1',
    warehouse=args.warehouse
)
cur = conn.cursor()
cur.execute(f"ALTER WAREHOUSE {args.warehouse} SET WAREHOUSE_SIZE = '{args.size}';")
print(f"Scaled {args.warehouse} to {args.size}")
cur.close()
conn.close()
