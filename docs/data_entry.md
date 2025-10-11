# Data Entry module (`data_entry.py`)

Utility functions for collecting and parsing blood pressure and heart rate readings.

## Functions

### `get_date(prompt: str, allow_default: bool = False) -> str`
- **Description**: Prompt for a date in `dd-mm-yyyy` format. If `allow_default` is `True` and input is empty, returns today's date.
- **Parameters**:
  - `prompt`: Message displayed to the user.
  - `allow_default`: Whether to allow today's date when input is empty.
- **Returns**: Date string in `dd-mm-yyyy`.
- **Raises/Errors**: Re-prompts on invalid format.
- **Example**:
```python
from data_entry import get_date
start = get_date("Enter start date (dd-mm-yyyy): ")
```

### `get_pressure_reading(prompt: str) -> int`
- **Description**: Prompt for a positive integer (pressure or heart rate).
- **Parameters**:
  - `prompt`: Message displayed to the user.
- **Returns**: Positive integer.
- **Raises/Errors**: Re-prompts until a valid positive integer is entered.
- **Example**:
```python
from data_entry import get_pressure_reading
systolic = get_pressure_reading("Enter systolic pressure: ")
```

### `get_description() -> str`
- **Description**: Prompt for a free-form description of the reading.
- **Returns**: Description string.
- **Example**:
```python
from data_entry import get_description
description = get_description()
```

### `process_data(data_str: str) -> dict`
- **Description**: Parse a slash-separated input string: `date/systolic/diastolic/heart_rate/description`.
- **Parameters**:
  - `data_str`: Input string with five fields separated by `/`.
- **Returns**: Dict with keys `date`, `systolic`, `diastolic`, `heart_rate`, `description`, each mapped to a single-element list.
- **Raises**: `ValueError` if the format is incorrect.
- **Example**:
```python
from data_entry import process_data
payload = process_data("01-01-2025/120/80/70/Morning reading")
# payload => {"date": ["01-01-2025"], "systolic": [120], ...}
```
