import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==================
# TOTAL COUNT
# ==================
def calc_total(df, case_name):
    return np.sum(df[case_name].to_numpy())

# ============================
# SORT DATAFRAME BY VALUES
# ============================
def sort_df(df, case_name):
    return df.sort_values(case_name, ascending=False)

# ========================
# TOTAL CASES DATAFRAME
# ========================
def total_cases(df):
    total_confirmed = calc_total(df, "Confirmed")
    total_deaths = calc_total(df, "Deaths")
    total_recovered = calc_total(df, "Recovered")
    total_active = calc_total(df, "Active")
    
    cases_df = pd.DataFrame({
        "Category": ["Total Confirmed", "Total Deaths", "Total Recovered", "Total Active"],
        "Values": [total_confirmed, total_deaths, total_recovered, total_active]
    })
    return cases_df

# =================
# BAR CHART
# =================
def bar_chart_total_cases(df):
    cases_df = total_cases(df)

    # Define different colors for each category
    colors = np.array(["#3498db", "#0963ff", "#006aff", "#0011ff"])

    # Create bar chart
    plt.barh(cases_df["Category"], cases_df["Values"], color=colors)
    plt.title("Global COVID-19 Total Cases Overview")
    plt.xlabel("Number of Cases")
    plt.ylabel("Category")

    # Add value labels beside each bar (with commas for readability)
    for index, value in enumerate(cases_df["Values"]):
        plt.text(value, index, f"{int(value):,}", va='center')

    plt.tight_layout()
    plt.show()
    
def bar_chart_with_sorted(df, case_name):
    sorted_df = sort_df(df, case_name).head(10)
    
    colours = np.array(["#f73e3e", "#f7633e", "#faa72a", "#facc00", "#53fa00",
                        "#0bea77", "#00fae1", "#00affa", "#002afa", "#5700fa"])

    plt.barh(sort_df["Country/Region"], sort_df[case_name], color=colours)
    plt.show()
    
def main():
    file_path = "data_set/Country_wise_latest.csv"
    df = pd.read_csv(file_path)
    # bar_chart_total_cases(df)
    
    bar_chart_with_sorted(df, "Confirmed")
    
if __name__ == "__main__":
    main()