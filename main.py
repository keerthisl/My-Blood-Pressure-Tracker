import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from data_entry import get_date, get_pressure_reading, process_data, get_description

class CSV:
    CSV_FILE = "pressure_data.csv"
    COLUMNS = ["date", "systolic", "diastolic", "heart_rate", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, systolic, diastolic, heart_rate, description):
        new_entry = {
            "date": date,
            "systolic": systolic,
            "diastolic": diastolic,
            "heart_rate": heart_rate,
            "description": description,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

        return filtered_df

def get_pressure_data_alternative():
    """
    Gets pressure data and description in a single slash-separated string.

    Returns:
        str: The input data string or None if user doesn't enter data.
    """
    data_str = input("Enter pressure readings and description (date/systolic/diastolic/heart_rate/description) or press Enter to continue: ")
    return data_str

def add():
    CSV.initialize_csv()

    choice = input("Enter data using (1) individual prompts or (2) slash-separated format (1/2): ")

    if choice == "1":
        date = get_date(
            "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
            allow_default=True,
        )
        systolic = get_pressure_reading("Enter systolic pressure:")
        diastolic = get_pressure_reading("Enter diastolic pressure:")
        heart_rate = get_pressure_reading("Enter heart rate:")
        description = get_description()
        CSV.add_entry(date, systolic, diastolic, heart_rate, description)
    elif choice == "2":
        data_str = get_pressure_data_alternative()
        if data_str:  # Check if user entered data
            try:
                data = process_data(data_str)
                CSV.add_entry(data["date"][0], data["systolic"][0], data["diastolic"][0], data["heart_rate"][0], data["description"][0])
            except ValueError as e:
                print(f"Invalid data format: {e}")
            except Exception as e:  # Catch other potential errors
                print(f"An error occurred: {e}")
    else:
        print("Invalid choice. Enter 1 or 2.")


# def plot_pressure(df):
## This will show by each date
    if 'heart_rate' in df.columns:
        plt.figure(figsize=(12, 6))
        plt.plot(df['date'], df['systolic'], label='Systolic')
        plt.plot(df['date'], df['diastolic'], label='Diastolic')
        plt.plot(df['date'], df['heart_rate'], label='Heart Rate')
        plt.xlabel('Date')
        plt.ylabel('Pressure (mmHg) / Heart Rate (bpm)')
        plt.title('Systolic, Diastolic Pressure and Heart Rate Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Heart rate data not available in the provided DataFrame.")


# def plot_pressure(df):
## This will show by month1 
    if 'heart_rate' in df.columns:
        plt.figure(figsize=(12, 6))

        # Convert 'date' to datetime if it's not already
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)

        # Plot the data
        plt.plot(df['date'], df['systolic'], label='Systolic')
        plt.plot(df['date'], df['diastolic'], label='Diastolic')
        plt.plot(df['date'], df['heart_rate'], label='Heart Rate')

        # Format the x-axis to show months
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # e.g., "Jan 2024"
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Major ticks on the first of each month

        # Rotate the labels for better readability
        plt.gcf().autofmt_xdate()

        # Add labels, title, legend, and grid
        plt.xlabel('Date')
        plt.ylabel('Pressure (mmHg) / Heart Rate (bpm)')
        plt.title('Systolic, Diastolic Pressure and Heart Rate Over Time')
        plt.legend()
        plt.grid(True)

        # Display the plot
        plt.show()
    else:
        print("Heart rate data not available in the provided DataFrame.")


# def plot_pressure(df):
## This will show by month2
    if 'heart_rate' in df.columns:
        plt.figure(figsize=(12, 6))

        # Convert 'date' to datetime if it's not already
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)

        # Plot the data
        plt.plot(df['date'], df['systolic'], label='Systolic')
        plt.plot(df['date'], df['diastolic'], label='Diastolic')
        plt.plot(df['date'], df['heart_rate'], label='Heart Rate')

        # Set x-axis ticks dynamically based on the data
        unique_months = df['date'].dt.to_period('M').drop_duplicates().to_timestamp()
        plt.gca().set_xticks(unique_months)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # e.g., "Jan 2024"

        # Rotate the labels for better readability
        plt.gcf().autofmt_xdate()

        # Add labels, title, legend, and grid
        plt.xlabel('Date')
        plt.ylabel('Pressure (mmHg) / Heart Rate (bpm)')
        plt.title('Systolic, Diastolic Pressure and Heart Rate Over Time')
        plt.legend()
        plt.grid(True)

        # Display the plot
        plt.show()
    else:
        print("Heart rate data not available in the provided DataFrame.")

# def plot_pressure(df):
## This will show by month3
    if 'heart_rate' in df.columns:
        plt.figure(figsize=(12, 6))

        # Convert 'date' to datetime if it's not already
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)

        # Plot the data
        plt.plot(df['date'], df['systolic'], label='Systolic')
        plt.plot(df['date'], df['diastolic'], label='Diastolic')
        plt.plot(df['date'], df['heart_rate'], label='Heart Rate')

        # Find unique months with data
        unique_months = df['date'].dt.to_period('M').unique()
        unique_months = pd.Series(unique_months).dt.start_time

        # Set x-axis ticks dynamically based on the unique months
        plt.gca().set_xticks(unique_months)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # e.g., "Jan 2024"

        # Rotate the labels for better readability
        plt.gcf().autofmt_xdate()

        # Add labels, title, legend, and grid
        plt.xlabel('Date')
        plt.ylabel('Pressure (mmHg) / Heart Rate (bpm)')
        plt.title('Systolic, Diastolic Pressure and Heart Rate Over Time')
        plt.legend()
        plt.grid(True)

        # Display the plot
        plt.show()
    else:
        print("Heart rate data not available in the provided DataFrame.")

# def plot_pressure(df):
## This will show by month4
    if 'heart_rate' in df.columns:
        plt.figure(figsize=(12, 6))

        # Convert 'date' to datetime if it's not already
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)

        # Extract month-year as a string for categorical plotting
        df['month_year'] = df['date'].dt.strftime('%b %Y')  # e.g., "Jan 2024"

        # Plot the data using the categorical x-axis
        plt.plot(df['month_year'], df['systolic'], label='Systolic')
        plt.plot(df['month_year'], df['diastolic'], label='Diastolic')
        plt.plot(df['month_year'], df['heart_rate'], label='Heart Rate')

        # Configure the plot
        plt.xlabel('Month')
        plt.ylabel('Pressure (mmHg) / Heart Rate (bpm)')
        plt.title('Systolic, Diastolic Pressure and Heart Rate Over Time')
        plt.legend()
        plt.grid(True)

        # Rotate the x-axis labels for readability
        plt.xticks(rotation=45, ha='right')

        # Display the plot
        plt.tight_layout()  # Adjust layout to prevent overlap
        plt.show()
    else:
        print("Heart rate data not available in the provided DataFrame.")


def plot_pressure(df):
    if 'heart_rate' in df.columns:
        plt.figure(figsize=(12, 6))

        # Convert 'date' to datetime if it's not already
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)

        # Sort the data by date to ensure it goes from old to new
        df = df.sort_values(by='date')

        # Extract month-year as a string for categorical plotting
        df['month_year'] = df['date'].dt.strftime('%b %Y')  # e.g., "Jan 2024"

        # Plot the data using the categorical x-axis
        plt.plot(df['month_year'], df['systolic'], label='Systolic')
        plt.plot(df['month_year'], df['diastolic'], label='Diastolic')
        plt.plot(df['month_year'], df['heart_rate'], label='Heart Rate')

        # Configure the plot
        plt.xlabel('Month')
        plt.ylabel('Pressure (mmHg) / Heart Rate (bpm)')
        plt.title('Systolic, Diastolic Pressure and Heart Rate Over Time')
        plt.legend()
        plt.grid(True)

        # Rotate the x-axis labels for readability
        plt.xticks(rotation=45, ha='right')

        # Adjust layout to prevent overlap
        plt.tight_layout()

        # Display the plot
        plt.show()
    else:
        print("Heart rate data not available in the provided DataFrame.")



def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions within a date range")
        print("3. Plot pressure data")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add()
        elif choice == "2":
            today = datetime.today().strftime("%d-%m-%Y")
            start_date = get_date("Enter the start date (dd-mm-yyyy), or press Enter for today: ", today)
            end_date = get_date("Enter the end date (dd-mm-yyyy), or press Enter for today: ", today)
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_pressure(df.copy())
        elif choice == "3":
            df = pd.read_csv("pressure_data.csv")
            plot_pressure(df)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
