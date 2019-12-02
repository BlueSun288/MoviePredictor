import pandas as pd

def getPredictions(ratings): # Takes in dataframe of [movieID, rating]s & returns dataframe of top 5 [movieID, certainty] where certainty is the highest.

	#Initializes
	ld = pd.DataFrame(pd.read_csv("learned.csv")) # Learned values
	vals = [["a",-1],["a",-1],["a",-1],["a",-1],["a",-1]]
	out = pd.DataFrame(vals, columns=["movieID", "Certainty"])

	for i in range(1,3952):
		val = 1
		for j in ratings.index:

			# Gets certainty for each Movie given the user's ratings
			a = ld.iloc[i][ratings.iloc[j][0]]

			d = float(ratings.iloc[j][1]) / 10.0

			b = (1 - (d % 5))
			c = a * b

			val *= c
		#print(i,": ", val)
		vals.append([i, val]) # Array of certainty for each movie in list

	# Sorts vals by Certainty, descending
	vals.sort(key=sortCertainty, reverse=True)

	# Puts the top 5 [movieId, Certainty]s into out
	for i in range(0,5):
		out.iloc[i] = vals[i]
	#print(out)
	return out

def sortCertainty(val):
	return val[1]