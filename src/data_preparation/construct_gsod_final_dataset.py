"""
Constructs the final GSOD from its parts.

==== How it works ====
The objective is to create a dataset where each entry is a year-state pair
that describes average meteorological stats for that state in that year.

We download the GSOD dataset using download_gsod.sh. It creates a bunch
of folders. There is a folder for each year. Each folder contains a csv
file for a weather station in some state. The csv file contains the
station's daily meteorological info for that station in that year.

For every year, we:
    - iterate over every weather-station-csv file in the year's folder,
    figure out the state of that weather station, and add its entries
    to a dictionary storing the entries for each state of that year.
    - then we take the averages of the values for each state of that year
    and save them as a single year-state dataset entry

After iterating over every year, we save the year-state dataset entries
into a csv file.
"""

from os import listdir
import csv
import numpy as np

# We only consider these states (all the official US states). The GSOD dataset
# also contains data for US terriotries that we ignore.
states_to_consider = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL",
                      "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA",
                      "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE",
                      "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR",
                      "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VI", "VT", "WA",
                      "WI", "WV", "WY"]

# The function that constructs our dataset
def construct():
    # Store the final dataset entries here
    year_state_averages = []

    # For years in [1980, 2022)
    for year in range(1980, 2022):
        print(f"Working on {year}:")
        path = "gsod_raw/" + str(year)
        files = [f for f in listdir(path)]

        # For the year, store data about each state
        print("    reading data...")
        state_data = {}

        # Go over every file in the year's folder...
        for file in files:
            # print(f"    Reading {file}...")

            with open(path + "/" + file, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                is_header = True

                # The state that this weather station file belongs to:
                current_state = None

                # Read every row in the weather station file
                for row in reader:
                    # Skip the header
                    if is_header:
                        is_header = False
                        continue

                    # We haven't figured out the state that this file belongs to.
                    # Let's do that.
                    if current_state is None:
                        # Extract the state from the weather station name, which typically
                        # looks like "Denver Airport, OH" or "Denver Airport, OH US"
                        location = row[5]

                        if location == "":
                            continue

                        current_state_split = location.split(",")

                        if len(current_state_split) < 2:
                            continue

                        current_state_split_2 = current_state_split[1][1:].strip()
                        current_state = current_state_split_2.split(" ")[0].strip()

                        if current_state not in states_to_consider:
                            # This "state" is actually some random US territory
                            break

                    # Clean up the row we are looking at for this weather station
                    row_2 = [x.split(" ")[-1] for x in row]
                    row_3 = [("0" if x == "" else x) for x in row_2]

                    # Add the row to its corresponding state
                    if current_state not in state_data:
                        state_data[current_state] = [row_3]
                    else:
                        state_data[current_state].append(row_3)


        # Now state_data has all the rows for each state for this year... we must now
        # average the values for each state.
        print("    averaging data...")

        # Which columns/features we want to have in our dataset:
        # values_to_average = [4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 26]
        values_to_average = [4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 26]
        # values_to_average = [4, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 26]

        # Average the values for each state
        for state in state_data:
            arr = np.array(state_data[state])
            arr_2 = arr[:, values_to_average]
            # arr_3 = np.char.replace(arr_2, "", "0")
            # try:
            arr_4 = arr_2.astype(float)
            # except:
            #     continue
            means = np.mean(arr_4, axis=0)
            year_state_averages.append([year, state] + means.tolist())

    # Write final dataset
    print("Writing final file!")

    with open('gsod_final.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["YEAR", "STATE", "ELEVATION", "TEMP", "TEMP_ATTRIBUTES", "DEWP", "DEWP_ATTRIBUTES", "SLP", "SLP_ATTRIBUTES",
                         "STP", "STP_ATTRIBUTES", "VISIB", "VISIB_ATTRIBUTES", "WDSP", "WDSP_ATTRIBUTES", "MXSPD",
                         "GUST", "MAX", "SNDP"])

        for row in year_state_averages:
            writer.writerow(row)




if __name__ == "__main__":
    construct()
