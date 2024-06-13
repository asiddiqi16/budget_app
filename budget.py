"""
This is a module that describes the Budget app class used for creating a custom bduget
Author: Ariba
"""

from datetime import datetime
from dataclasses import dataclass, field
from typing import Union, ClassVar


@dataclass
class BudgetLineItem:
    """
    A class used to represent a budget line item
    ...
    Attributes
    ----------


    Methods
    -------

    """

    category: Union[str, None] = None
    description: str = ""
    value: float = 0.0
    frequency: str = ""

    _category: Union[str, None] = field(init=False, repr=False)
    _frequency: str = field(init=False, repr=False)
    _FREQUENCY: ClassVar[tuple] = ("Daily", "Weekly", "Fortnightly", "Monthly")
    _main_category: ClassVar[set] = set()

    line_item: dict = field(init=False, repr=False)

    def __post_init__(self):

        self.line_item = {
            "category": self._category,
            "description": self.description.title(),
            "value": self.value,
            "frequency": self._frequency,
        }

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category:
            self._category = category.title()
            BudgetLineItem._main_category.add(self._category)
        else:
            self._category = category

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        if frequency.title() not in BudgetLineItem._FREQUENCY:
            raise ValueError(f"{frequency.title()} is not supported")
        else:
            self._frequency = frequency.title()


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
