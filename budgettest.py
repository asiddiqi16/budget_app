"""test_data= [{"category": string (optional),
        "description":string,
        "value": float,
        "frequency": string (matching class attribute frequency values),
        "billing_start_date": isoformat date (optional),
        "billing_period": int days (optional)}]
"""

test_data = [
    {
        "category": "Home",
        "description": "Rent",
        "value": 2651.00,
        "frequency": "Monthly",
        "billing_start_date": "2024-06-24",
        "billing_period": None,
    },
    {
        "category": "Home",
        "description": "Groceries",
        "value": 500,
        "frequency": "Monthly",
        "billing_start_date": None,
        "billing_period": None,
    },
    {
        "category": "Utilities",
        "description": "Phone",
        "value": 30,
        "frequency": "Monthly",
        "billing_start_date": "2024-06-01",
        "billing_period": 28,
    },
]
