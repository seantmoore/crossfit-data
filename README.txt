# Summary

The `results/json/` folder contains all the raw data for each region. They're split into pages because the API only returns 50 results per page.
The `results/csv/` folder contains simplified files for each region. Open them in excel and they should look similar to the scoreboard on the website. These are aggregated result for each region which is why there are no pages.

## Region IDs:
0 - worldwide
1 - Africa
2 - Asia
3 - Australia
4 - Canada East
5 - Canada West
6 - Central East
7 - Euroupe
8 - Latin America
9 - Mid Atlantic
10 - North Central
11 - North East
12 - Northern California
13 - North West
14 - South Central
15 - South East
16 - Southern California
17 - South West


## RX IDs:
0 - RX
1 - Scaled

## File name examples:

The file `region_11_rx_0_page_21.json` would be data for region 11 (North East), RX athletes, page 21.

The file `region_11_rx_0.csv` would be aggregated data for region 11 (North East), for RX athletes.

# TO-DO

- I got rate limited when I tried collecting the worldwide data. I need to get that and generate the CSV files for that "region" once I am no longer rate limited.
- Update the scripts to take in parameter names which control region, scaled, etc.