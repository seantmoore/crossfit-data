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

## Division IDs:
1 - Male
2 - Female
3 - Men (45-49)
4 - Women (45-49)
5 - Men (50-54)
6 - Women (50-54)
7 - Men (55-59)
8 - Women (55-59)
9 - Men (60+)
10 - Women (60+)
11 - Team
12 - Men (40-44)
13 - Women (40-44)
14 - Boys (14-15)
15 - Girls (14-15)
16 - Boys (16-17)
17 - Girls (16-17)
18 - Men (35-39)
19 - Women (35-39)

## File name examples:

The file `division_1_region_11_rx_0_page_21.json` would be data for males, region 11 (North East), RX athletes, page 21.

The file `division_2_region_11_rx_0.csv` would be aggregated data for females, region 11 (North East), for RX athletes.

# TO-DO

- Update the scripts to take in parameter names which control region, scaled, etc.
- Figure out the rate limit. Rough estimate is ~10k requests per hour.
- Add support for detecting 403 errors (forbidden, which is apparently their code for rate limited).