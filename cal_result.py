import json
import os
address = "./users/u2/"
fre = 0
acr = 0
fre_u = 0
acr_u = 0
fre_g = 0
acr_g = 0
for root,dirs,files in os.walk(r"./users/"):
    for file in files:
        if ("result" in root) and ("u2" in root):
           print(os.path.join(root,file))
           addr = os.path.join(root,file)
           tmp = json.load(open(addr,'r'))
           fre += tmp['fluent_score']
           acr += tmp['correct_score']
           fre_u += tmp['fluent_score_u']
           acr_u += tmp['correct_score_u']
           fre_g += tmp['fluent_score_g']
           acr_g += tmp['correct_score_g']
print("Relevance_LBD:", fre/30)
print("Relevance_RFE:", fre_u/30)
print("Relevance_GRT:", fre_g/30)
print("Richness_LBD:", acr/30)
print("Richness_RFE:", acr_u/30)
print("Richness_GRT:", acr_g/30)
 
           
