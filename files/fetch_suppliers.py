import requests

def fetch_suppliers():
    # OData Service URL
    url = "https://services.odata.org/northwind/northwind.svc/Suppliers?$format=json"

    try:
        # Send GET request to fetch supplier data
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Parse JSON response
        data = response.json()
        suppliers = response.get("value", [])

        # Display supplier data
        print("Supplier Data:")
        for supplier in suppliers:
            print("ID: {supplier['SupplierID']}, Name: {supplier['CompanyName']}, Country: {supplier['Country']}")
            # print("ID: {supplier[1]}")

    except Exception as e:
        print(f"Error fetching supplier data: {e}")

if __name__ == "__main__":
    fetch_suppliers()
