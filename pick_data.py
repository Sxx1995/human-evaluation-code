import json
import random
s = json.load(open('merged_results.json','r'))

Len = []

for i in s['LBD_result'].keys():
    if len(s['LBD_result'][i].split(' ')) >= 9:
    	Len += [i]

pick1 = random.sample(Len, 20)

pick2 = random.sample(list(s['LBD_result'].keys()), 10)

gt_select = []
for i in range(30):
    gt_select.append(random.randint(0,4))


json.dump( list(zip(pick1 + pick2, gt_select)), open('new_im_q.json','w'))

