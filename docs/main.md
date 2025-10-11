# Main module (`main.py`)

Core application: CSV storage, querying, plotting, and CLI workflow.

## Class: `CSV`
A helper class that manages the `pressure_data.csv` file.

### Constants
- `CSV_FILE`: `"pressure_data.csv"`
- `COLUMNS`: `["date", "systolic", "diastolic", "heart_rate", "description"]`
- `FORMAT`: `"%d-%m-%Y"`

### `CSV.initialize_csv() -> None`
- **Description**: Ensures the CSV file exists with the correct columns.
- **Side effects**: Creates the file if missing.
- **Example**:
```python
from main import CSV
CSV.initialize_csv()
```

### `CSV.add_entry(date: str, systolic: int, diastolic: int, heart_rate: int, description: str) -> None`
- **Description**: Appends a new row to `pressure_data.csv`.
- **Parameters**: `date`, `systolic`, `diastolic`, `heart_rate`, `description`.
- **Example**:
```python
from main import CSV
CSV.add_entry("01-01-2025", 120, 80, 70, "Morning reading")
```

### `CSV.get_transactions(start_date: str, end_date: str) -> pandas.DataFrame`
- **Description**: Reads CSV and filters rows where `date` is within `[start_date, end_date]` inclusive.
- **Parameters**: `start_date`, `end_date` in `dd-mm-yyyy`.
- **Returns**: Filtered DataFrame with `date` converted to datetime.
- **Example**:
```python
from main import CSV
filtered = CSV.get_transactions("01-01-2025", "07-01-2025")
```

## Functions

### `get_pressure_data_alternative() -> str | None`
- **Description**: Prompts for a single slash-separated string `date/systolic/diastolic/heart_rate/description`.
- **Returns**: The string entered, or `None` if empty.
- **Example**:
```python
from main import get_pressure_data_alternative
raw = get_pressure_data_alternative()
```

### `add() -> None`
- **Description**: Interactive flow to add a new entry using either multiple prompts or the alternative slash-separated input.
- **Uses**: `CSV.initialize_csv`, `data_entry.get_date`, `data_entry.get_pressure_reading`, `data_entry.get_description`, `data_entry.process_data`, `CSV.add_entry`.
- **Example**:
```python
from main import add
add()  # runs the interactive prompts
```

### `plot_pressure(df: pandas.DataFrame) -> None`
- **Description**: Plots `systolic`, `diastolic`, and `heart_rate` over time using Matplotlib.
- **Parameters**: `df` with columns `date`, `systolic`, `diastolic`, `heart_rate`.
- **Example**:
```python
import pandas as pd
from main import plot_pressure

df = pd.read_csv("pressure_data.csv")
plot_pressure(df)
```

### `main() -> None`
- **Description**: CLI menu loop. Options: add entry, view filtered transactions, plot data, exit.
- **Entrypoint**: Executed when running `python main.py`.
- **Example**:
```bash
python main.py
```

## CLI Usage

- **Add a new transaction**: choose option `1` and follow prompts, or choose `2` in the sub-prompt to paste a slash-separated entry.
- **View transactions within a date range**: choose option `2` and input start/end dates; optionally plot the result.
- **Plot pressure data**: choose option `3` to plot all data in `pressure_data.csv`.
