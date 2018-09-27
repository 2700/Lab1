import pandas as pd

df1 = pd.DataFrame([[113,'a'],
         [122,'b'],
         [123,'b'],
         [301,'c']],
	columns=['ID','Letter'])

df2 = pd.DataFrame([['1', 113],
	['2', 113],
	['3', 301],
	['4', 122],
	['5', 113]], 
	columns=['num', 'num_letter'])

df2['letter'] = df2['num_letter'].apply(lambda x: df1.letter[x])

print df1