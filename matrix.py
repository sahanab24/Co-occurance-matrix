corpus=["abc def ijk pqr", "pqr klm opq", "lmn pqr xyz abc def pqr abc"]
features=["abc", "pqr","def"]
window_size= 2
#Co_occurace matrix

      #abc pqr	def
#abc: 3 2	3
#pqr: 2	3	2
#def: 3	2	2
import numpy as np
window=2
C = np.zeros([len(features), len(features)])
for feature in features:
      for review in corpus:
            if feature in review:
                  words = review.split()
                  indices = [i for i, x in enumerate(words) if x == feature]
                  for index in indices:
                        for j, word in enumerate(words):
                              if j>i and word in features and abs(j-index) <= window :
                                    #print(review)
                                    #print(abs(j-index))
                                    i = features.index(feature)
                                    j = features.index(word)
                                    #print(i,feature,j,word)
                                    #print("________________")
                                    C[i][j] += 1                           
print(C)
