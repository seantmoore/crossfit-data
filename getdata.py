#! /usr/bin/python3
import requests

BASE_URL = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2017/leaderboards?division=%d&region=%d&scaled=%d&sort=0&occupation=0&page=%d'

BASE_FILENAME = 'division_%d_region_%d_rx_%d_page_%d.json'

divisions = [d for d in range(1,20)] #[1,2] # 1 = male, 2 = female
scaled = [0,1]
regions = [r for r in range(1,18)] # region 0 is worldwide

for d in divisions:
    for s in scaled:
        for r in regions:
            # get first page
            first_page_data = requests.get(BASE_URL % (d, r, s, 1)).json()
            total_pages = first_page_data['totalpages']
            for p in range(1,total_pages+1):
                url = BASE_URL % (d, r, s, p)
                filename = BASE_FILENAME % (d, r, s, p)
                print('division: %d, region: %d, scaled?: %d, page: %d / %d' % (d, r, s, p, total_pages))
                data = requests.get(url)
                _ = data.json() # throws error if HTML
                with open(filename, 'w') as f:
                    f.write(data.text)
                # end with
            # end for f
        # end for r
    # end for s
# end for d

print("done")





'''



TO-DO: region 0





'''