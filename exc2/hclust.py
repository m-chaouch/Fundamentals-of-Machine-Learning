import pandas as pd
import seaborn as sb # for visualisation of data
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

blogdata = pd.read_json("exc2/blogdata.json")
# print(blogdata)

# words = blogdata.iloc[:, 0]
# print(words)

# visited = list() # a list of sets. Only one combination of a set of two elements exists, so we can compare and see if we already visited such a combination.
# i = 0
# for blog1 in blogdata:
#     # print(blogdata[f"{blog}"]) #prints out every row of every blog
#     for blog2 in blogdata:
#         if({blog1, blog2} not in visited):
#             visited.append({blog1,blog2})
#             i += 1

# print(visited)
# print(len(visited))
# print(i)


pearsoncorr = blogdata.corr(method='pearson', numeric_only=True)
# print(type(pearsoncorr))
pc_arr = pearsoncorr.to_numpy()
print(pc_arr)
Z = hierarchy.linkage(pc_arr, 'single') # linkage describes when two points(point-cluster/cluster-cluster) are similar

# print(type(cluster_history))
# print(Z)
dn = hierarchy.dendrogram(Z)
# plt.figure()
plt.show()


# for blog1 in pearsoncorr:
#     for blog2 in pearsoncorr:

