import requests
import json
from datetime import datetime, timezone
import os

API_URL = "https://api.fantasycalc.com/leagues/1197273263458230272"
PARAMS = {
    "site": "sleeper",
}

def main():
    resp = requests.get(API_URL, params=PARAMS)
    resp.raise_for_status()
    data = resp.json()

    # Ensure data/ directory exists
    os.makedirs("data", exist_ok=True)

    # Create timestamped filename: e.g. data/fantasycalc_2025-09-04T18-25-30.json
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    filename = f"data/fantasycalc_{ts}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(data)} entries to {filename}")

if __name__ == "__main__":
    main()
