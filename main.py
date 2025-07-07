import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

from datetime import date
import pandas as pd
from custom_auto_email import send_email

SHEET_ID = '1r2AQSH8Wr1Q77ltT__VNCi0qhJt6Z0wqTBt1cx-6qTY'
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=0'

def load_df(url):
    df = pd.read_csv(url)
    
    # Clean and parse dates manually (auto handles both yy and yyyy)
    df['due_date'] = pd.to_datetime(df['due_date'], dayfirst=True, errors='coerce')
    df['reminder_date'] = pd.to_datetime(df['reminder_date'], dayfirst=True, errors='coerce')
    
    return df

def query_data_and_send_email(df):
    present_date = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present_date >= row['reminder_date'].date()) and (row['has_paid'].strip().lower() == 'no'):
            send_email(
                subject=f'[Python Automation Expert] invoice {row["invoice_no"]}',
                reciever_email=row['email'],
                name=row['name'],
                due_date=row['due_date'].strftime('%d-%m-%Y'),
                invoice_no=row['invoice_no'],
                amount=row['amount'],
            )
            email_counter += 1
    return f'Total Email sent: {email_counter}'

result = query_data_and_send_email(load_df(URL))
print('Result:', result)


