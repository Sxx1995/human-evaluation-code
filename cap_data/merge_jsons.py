import json
output = {}
output['LBD_result'] = {}
s = open('msr-vtt_test_predictions.txt','r').readlines()
for i in range(len(s)):
    s[i] = s[i][:-1]
    s[i] = s[i].split('\t') 
    output['LBD_result'][s[i][0]] = s[i][1]

output['RFE_result'] = {}
s = open('msr-vtt_test_predictions_RFE.txt','r').readlines()
for i in range(len(s)):
    s[i] = s[i][:-1]
    s[i] = s[i].split('\t')
    output['RFE_result'][s[i][0]] = s[i][1]

output['GRT_result'] = {}
s = open('msr-vtt_test_references.txt','r').readlines()
for i in range(len(s)):
    s[i] = s[i][:-1]
    s[i] = s[i].split('\t')
    if not s[i][0] in output['GRT_result'].keys():
         output['GRT_result'][s[i][0]] = []
    output['GRT_result'][s[i][0]] += [s[i][1]]

with open('merged_results.json', 'w') as outfile:
    json.dump(output, outfile)


