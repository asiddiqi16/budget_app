"""
This is a module that describes the Budget app class used for creating a custom bduget
Author: Ariba
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Union, ClassVar

# TODO: Check if there is any point in using the dataclass decorate


class Frequency(Enum):
    """
    A class used to represent the list of support budget frequencies

    Example Usage:
    >>> "Daily" in Frequency
    True
    """

    DAILY = "Daily"
    WEEKLY = "Weekly"
    FORTNIGHTLY = "Fortnightly"
    MONTHLY = "Monthly"
    BIMONTHLY = "Bi-monthly"
    QUARTERLY = "Quarterly"
    ANNUALLY = "Annually"


@dataclass
class BudgetLineItem:
    """
    A class used to represent a budget line item

    Class Attributes
    ----------------
    _main_category: set
        A set of main categories created for the class when instances are created.
        Example: Income, Home, Utilities etc.

    Attributes
    ----------
    category: str | None
        A budget line item categories such as Income, Home, Utilities etc.

    frequency: Frequency
        A frequency of a budget line item. Inherits from the Frequency Enum class.

    description: str
        A brief description for the budget line item, such as Rent, Electricity etc.

    value: **
        Currency value for the budget line item. Incomes are positive values, Expenses are negative.

    Raises
    -------
    AttributeError:
        If an invalid frequency value not supported by Frequency Enum is assigned.

    Example Usage:
    >>> budgetlineitem1 = BudgetLineItem(category = "Home",
    description ="Rent",
    value = 2651.0,
    frequency = Frequency.MONTHLY)



    """

    frequency: Frequency = field(init=False)
    _category: Union[str, None] = field(init=False, repr=False)
    _frequency: Frequency = field(init=False, repr=False)
    _main_category: ClassVar[set] = set()
    category: Union[str, None] = field(init=False, default=None)
    description: str = ""
    value: float = 0.0

    @property
    def category(self):
        """
        Returns the private variable category
        """

        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the captilised category value and updates the _main_category class attribute
        """

        if category:
            self._category = category.title()
            BudgetLineItem._main_category.add(self._category)
        else:
            self._category = category

    @property
    def frequency(self):
        """
        Returns the private frequency enum
        """

        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency value and raises an exception if its not a valid Frequency enum
        """

        try:
            self._frequency = frequency
        except AttributeError as error:
            raise AttributeError(f"Invalid frequency selection - {error}\n") from None


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
