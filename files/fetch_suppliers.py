
import requests

# Define the Northwind OData service endpoint
NORTHWIND_ENDPOINT = "https://services.odata.org/V3/Northwind/Northwind.svc/Products"

def fetch_data():
    """Fetch data from the Northwind service."""
    response = requests.get(NORTHWIND_ENDPOINT, headers={"Accept": "application/json"})
    if response.status_code == 200:
        print("Successfully fetched data.")
        return response.json().get("value", [])
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        response.raise_for_status()

def main():
    """Main execution."""
    print("Fetching Northwind data...")
    products = fetch_data()
    for product in products[:10]:  # Display the first 10 products
        print(f"- {product['ProductName']} (${product['UnitPrice']})")

if __name__ == "__main__":
    main()
