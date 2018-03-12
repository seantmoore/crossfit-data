#! /usr/bin/python3
import json
import os

BASE_FILENAME = 'division_%d_region_%d_rx_%d.csv'

divisions = [d for d in range(1,20)] # 1 = male, 2 = female
scaled = [0,1]
regions = [r for r in range(18)] # 0 for worldwide

for d in divisions:
    for s in scaled:
        for r in regions:
            with open('results/csv/'+BASE_FILENAME % (d, r, s), 'w') as out_csv:
                print('Rank,Name,Points,17.1 rank,17.1 score,17.2 rank,17.2 score,17.3 rank,17.3 score,17.4 rank,17.4 score,17.5 rank,17.5 score,', file=out_csv)
                lines = []
                for root, dir, files in os.walk('results/json'):
                    for file in files:
                        if file.startswith('division_%d_region_%d_rx_%d' % (d, r, s)):
                            with open('results/json/'+str(file)) as curr_json:
                                data = json.load(curr_json)
                                for athlete in data['athletes']:
                                    line = [
                                        athlete['overallrank'],
                                        athlete['name'],
                                        athlete['overallscore'],
                                        athlete['scores'][0]['workoutrank'],
                                        athlete['scores'][0]['scoredisplay'],
                                        athlete['scores'][1]['workoutrank'],
                                        athlete['scores'][1]['scoredisplay'],
                                        athlete['scores'][2]['workoutrank'],
                                        athlete['scores'][2]['scoredisplay'],
                                        athlete['scores'][3]['workoutrank'],
                                        athlete['scores'][3]['scoredisplay'],
                                        athlete['scores'][4]['workoutrank'],
                                        athlete['scores'][4]['scoredisplay']
                                    ] # rank, name, points, place1, place2, ... place 5
                                    #print(",".join(line), file=out_csv)
                                    lines.append(line)
                                # end for athlete
                            # end open curr_json
                    # end for file
                # end for root, dir, files
                lines.sort(key=lambda x: int(x[0]))
                for line in lines:
                    print(",".join(line).encode('ascii', errors="ignore").decode(), file=out_csv)
            # end out_csv
        # end r
    # end s
# end d

print('done')