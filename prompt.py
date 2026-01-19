# prompt.py

def phonepe_goal(csv_path: str, target_date: str, device_pin: str) -> str:
    return f"""
You are a PhonePe transaction extraction agent.

1. Unlock device if required (PIN: {device_pin})
2. Go to home screen
3. Open PhonePe (package: com.phonepe.app)
4. Enter app PIN if asked
5. Open Transaction History
6. Extract ONLY transactions for date {target_date}

7. Write data to CSV file at:
{csv_path}

Rules:
- If file exists, APPEND rows
- If file does not exist, CREATE it
- CSV columns (exact order):
  merchant_name, datetime, amount, direction, app
- Set app column value as: phonepe
- Do NOT print JSON
- Do NOT return data
"""


def googlepay_goal(csv_path: str, target_date: str, device_pin: str) -> str:
    return f"""
You are a Google Pay transaction extraction agent.

1. Unlock device if required (PIN: {device_pin})
2. Go to home screen
3. Open Google Pay (package: com.google.android.apps.nbu.paisa.user)
4. Enter app PIN if asked
5. Navigate to Money section then click on see Transaction history.
6. Extract ONLY transactions for date {target_date}

7. Write data to CSV file at:
{csv_path}

Rules:
- If file exists, APPEND rows
- If file does not exist, CREATE it
- CSV columns (exact order):
  merchant_name, datetime, amount, direction, app
- Set app column value as: googlepay
- Do NOT print JSON
- Do NOT return data
"""


def paytm_goal(csv_path: str, target_date: str, device_pin: str) -> str:
    return f"""
You are a Paytm transaction extraction agent.

1. Unlock device if required (PIN: {device_pin})
2. Go to home screen
3. Open Paytm (package: net.one97.paytm)
4. Enter app PIN if asked
5. Open Balance & History
6. Extract ONLY transactions for date {target_date}

7. Write data to CSV file at:
{csv_path}

Rules:
- If file exists, APPEND rows
- If file does not exist, CREATE it
- CSV columns (exact order):
  merchant_name, datetime, amount, direction, app
- Set app column value as: paytm
- Do NOT print JSON
- Do NOT return data
"""