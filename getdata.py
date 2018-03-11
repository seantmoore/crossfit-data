#! /usr/bin/python3
import requests

BASE_URL = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2017/leaderboards?division=1&region=%d&scaled=%d&sort=0&occupation=0&page=%d'

BASE_FILENAME = 'region_%d_rx_%d_page_%d.json'

scaled = [1] # [0,1]
regions = [0] # [r for r in range(17)] # region 0 is worldwide

for s in scaled:
    for r in regions:
        # get first page
        first_page_data = requests.get(BASE_URL % (r, s, 1)).json()
        total_pages = first_page_data['totalpages']
        for p in range(1,total_pages+1):
            url = BASE_URL % (r, s, p)
            filename = BASE_FILENAME % (r, s, p)
            print('region: %d, scaled?: %d, page: %d / %d' % (r, s, p, total_pages))
            data = requests.get(url)
            with open(filename, 'w') as f:
                f.write(data.text)
            # end with
        # end for f
    # end for r
# end for s

print("done")