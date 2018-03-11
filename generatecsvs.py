#! /usr/bin/python3
import json
import os

BASE_FILENAME = 'region_%d_rx_%d.csv'

scaled = [0,1]
regions = [0] # [r for r in range(1,17)]

for s in scaled:
    for r in regions:
        with open('results/csv/'+BASE_FILENAME % (r, s), 'w') as out_csv:
            print('Rank,Name,Points,17.1 rank,17.1 score,17.2 rank,17.2 score,17.3 rank,17.3 score,17.4 rank,17.4 score,17.5 rank,17.5 score,', file=out_csv)
            lines = []
            for root, dir, files in os.walk('results/json'):
                for file in files:
                    if file.startswith('region_%d_rx_%d' % (r, s)):
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
            for l in lines:
                print(",".join(l).encode('ascii', errors="ignore").decode(), file=out_csv)
        # end out_csv
    # end r
# end s

print('done')