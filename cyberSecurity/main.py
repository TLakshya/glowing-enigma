import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

TARGET_URL = "https://www.google.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
TEST_INPUT_FIELD = "txtName"  
payloads = {
    "SQL Injection": "' OR '1'='1",
    "XSS": "<script>alert('XSS')</script>",
    "Command Injection": "; ls",
    "Directory Traversal": "../etc/passwd",
    "CSRF Simulation": "<input type='hidden' name='csrf_token' value='fake'>",
}

report = []

# Vulnerability Scanner

def scan_vulnerabilities(url):
    print("[*] Scanning Target:", url)
    for name, payload in payloads.items():
        try:
            # Send GET request 
            response = requests.get(url, params={TEST_INPUT_FIELD: payload}, headers=HEADERS, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Check for payload reflection 
            reflected = payload in response.text
            status = "Potentially Vulnerable" if reflected else "No Reflection"

            # Save to report
            report.append([name, payload, status, response.status_code])

        except Exception as e:
            report.append([name, payload, f"Error: {e}", "N/A"])

# Report Generator
def generate_report():
    print("\n\n🔍 Vulnerability Assessment Report:\n")
    headers = ["Test Name", "Payload", "Result", "HTTP Status"]
    print(tabulate(report, headers=headers, tablefmt="grid"))

# Run the Scanner
if __name__ == "__main__":
    scan_vulnerabilities(TARGET_URL)
    generate_report()
