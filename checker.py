import requests
import time
import logging
import json
import smtplib
from email.mime.text import MIMEText

# Load config
with open('config.json', 'r') as f:
    config = json.load(f)

servers = config['servers']
alert_email = config['alert_email']
smtp_server = config['smtp']['server']
smtp_port = config['smtp']['port']
smtp_user = config['smtp']['user']
smtp_pass = config['smtp']['password']

# Set up logging
logging.basicConfig(filename='health.log', level=logging.INFO,
                    format='[%(asctime)s] %(message)s')

def send_alert(server):
    msg = MIMEText(f'Server {server} is DOWN!')
    msg['Subject'] = f'[ALERT] {server} is DOWN'
    msg['From'] = smtp_user
    msg['To'] = alert_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, alert_email, msg.as_string())
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")

def check_server(server):
    try:
        start = time.time()
        response = requests.get(server, timeout=5)
        latency = int((time.time() - start) * 1000)
        if response.status_code == 200:
            logging.info(f"✅ {server} is UP ({response.status_code}, {latency}ms)")
        else:
            logging.warning(f"❌ {server} is DOWN ({response.status_code})")
            send_alert(server)
    except requests.RequestException:
        logging.error(f"❌ {server} is DOWN (no response)")
        send_alert(server)

if __name__ == '__main__':
    for server in servers:
        check_server(server)
