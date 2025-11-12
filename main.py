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

<<<<<<< HEAD
# ============================
# BAR CHART DRAWING
# ============================
=======

>>>>>>> 9ea63f46a36a3e62d226c2d3e01b88a5d9e89989
def draw_bar_chart(x_axis, y_axis, colours, title, x_label, y_label):
    plt.barh(x_axis, y_axis, color=colours)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Add value labels beside each bar (with commas for readability)
    for index, value in enumerate(y_axis):
<<<<<<< HEAD
        plt.text(value, index, f"{float(value):,.2f}", va='center')

    plt.tight_layout()
    plt.show()


# ==================================================================================
# SUBPLOT DRAWING FOR COUNTRY VS CASES
# ==================================================================================
def subplt_country_vs_cases(df):
    confirmed_sorted_df = sort_df(df, "Confirmed").head(10)
    deaths_sorted_df = sort_df(df, "Deaths").head(10)
    recovered_sorted_df = sort_df(df, "Recovered").head(10)
    active_sorted_df = sort_df(df, "Active").head(10)
    
    cases = np.array([["Confirmed", "Deaths"],
                      ["Recovered", "Active"]])
    sorted_df = [[confirmed_sorted_df, deaths_sorted_df],
                          [recovered_sorted_df, active_sorted_df]]
    
    colours = plt.cm.viridis(np.linspace(0, 1, len(confirmed_sorted_df)))
    
    figure, axis = plt.subplots(2,2)
    
    figure.set_size_inches(10,8)
    
    for i in range(0,2):
        for j in range(0,2):
            axis[i,j].barh((sorted_df[i][j])["Country/Region"], (sorted_df[i][j])[cases[i][j]], color=colours)
            axis[i,j].set_title(f"Top 10 Countries/Region – {cases[i][j]}")
            axis[i,j].set_xlabel(cases[i][j])
            axis[i,j].set_ylabel("Country/Region")
            
            for index, value in enumerate((sorted_df[i][j])[cases[i][j]]):
                axis[i,j].text(value, index, f"{float(value):,.2f}", va='center')
         
    figure.suptitle("“Global COVID-19 Overview – Top 5 Countries Comparison", size=20, color="red")
    plt.tight_layout()
    plt.show()
    
=======
        plt.text(value, index, f"{int(value):,}", va='center')

    plt.tight_layout()
    plt.show()
>>>>>>> 9ea63f46a36a3e62d226c2d3e01b88a5d9e89989
    
    
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

# ==============================
# BAR CHART WITH TOTAL CASES
# ==============================
def bar_chart_total_cases(df):
    cases_df = total_cases(df)

    # Define different colors for each category
    colours = np.array(["#3498db", "#0963ff", "#006aff", "#0011ff"])

    # Create bar chart
<<<<<<< HEAD
    draw_bar_chart(x_axis=cases_df["Category"], y_axis=cases_df["Values"],
                   colours=colours, title="Global COVID-19 Total Cases Overview",
                   x_label="Number of Cases", y_label="Category")
=======
    draw_bar_chart(x_axis=cases_df["Category"], y_axis=cases_df["Values"], colours=colours, title="Global COVID-19 Total Cases Overview", x_label="Number of Cases", y_label="Category")
>>>>>>> 9ea63f46a36a3e62d226c2d3e01b88a5d9e89989
    
# =================================
# BAR CHART WITH COUNTRY AND CASE
# ==================================
def bar_chart_with_sorted(df, case_name):
    sorted_df = sort_df(df, case_name).head(10)
    
    colours = np.array(["#f73e3e", "#f7633e", "#faa72a", "#facc00", "#53fa00",
                        "#0bea77", "#00fae1", "#00affa", "#002afa", "#5700fa"])

<<<<<<< HEAD
    draw_bar_chart(x_axis=sorted_df["Country/Region"], y_axis=sorted_df[case_name],
                   colours=colours, title=f"Global COVID-19 Country/Region and {case_name} Overview",
                   x_label=f"Values of {case_name}", y_label=f"Country/Region")
=======
    draw_bar_chart(x_axis=sorted_df["Country/Region"], y_axis=sorted_df[case_name], colours=colours, title=f"Global COVID-19 Country/Region and {case_name} Overview", x_label=f"Values of {case_name}", y_label=f"Country/Region")
>>>>>>> 9ea63f46a36a3e62d226c2d3e01b88a5d9e89989
    
    
def main():
    file_path = "data_set/Country_wise_latest.csv"
    df = pd.read_csv(file_path)
<<<<<<< HEAD
    
    # bar_chart_total_cases(df)
    # bar_chart_with_sorted(df, "Confirmed")
    # bar_chart_with_sorted(df, "Deaths / 100 Cases")
    # bar_chart_with_sorted(df, "Recovered / 100 Cases")
    # bar_chart_with_sorted(df, "Deaths / 100 Recovered")
    
    subplt_country_vs_cases(df)
    

    
if __name__ == "__main__":
    main()
=======
    bar_chart_total_cases(df)
    
    bar_chart_with_sorted(df, "Confirmed")
    
if __name__ == "__main__":
    main()
>>>>>>> 9ea63f46a36a3e62d226c2d3e01b88a5d9e89989
