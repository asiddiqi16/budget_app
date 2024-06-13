"""
This is a module that describes the Budget app class used for creating a custom bduget
Author: Ariba
"""

from datetime import datetime
from dataclasses import dataclass, field


class BudgetLineItem:
    """
    A class used to represent a budget line item
    ...
    Attributes
    ----------


    Methods
    -------

    """

    category = set()
    frequency = {
        "Daily",
        "Weekly",
        "Fortnightly",
        "Monthly",
        "Bi-Monthly",
        "Quarterly",
        "Annually",
    }

    def __init__(self, budget_line_item: dict = None):
        """A constructor for the Budget Line Item"""
        self.line_item = budget_line_item

    @property
    def line_item(self):
        """Returns the budget line item contents"""
        return self._line_item

    @line_item.setter
    def line_item(self, budget_line_item):
        """Sets the budget line item from the input value"""
        line_item = {}

        if budget_line_item["category"]:
            BudgetLineItem.category.add(budget_line_item["category"].title())
            line_item["category"] = budget_line_item["category"].title()
        else:
            line_item["category"] = None

        line_item["description"] = budget_line_item["description"].title()

        line_item["value"] = budget_line_item["value"]

        if budget_line_item["frequency"].title() not in BudgetLineItem.frequency:
            raise ValueError(
                f'{budget_line_item["frequency"].title()} is not supported'
            )
        line_item["frequency"] = budget_line_item["frequency"].title()

        if budget_line_item["billing_start_date"]:
            line_item["billing_start_date"] = datetime.fromisoformat(
                budget_line_item["billing_start_date"]
            )
        if budget_line_item["billing_period"]:
            line_item["billing_period"] = int(budget_line_item["billing_period"])
        self._line_item = line_item
        return self._line_item

    def update_line_item(self, budget_line_item, attribute):
        pass


class Budget:
    """
    A class used to represent a financial budget
    ...
    Attributes
    ----------


    Methods
    -------

    """

    def __init__(self, name: str = "My_Budget"):
        """Constructs a Budget object

        Parameters
        ----------

        line_items: list
        A list value with dictionaries representing each line item with the following format:
        [{category: string (optional),
        description:string,
        value: float,
        frequency: string (matching class attribute frequency values),
        billing_start_date: isoformat date (optional),
        billing_period: int days (optional)}]
        name : str
        A string value that is assigned to the self.name attribute
        """
        self.name = name
        self._line_items = []

    def add_line_items(self, line_items):
        pass
