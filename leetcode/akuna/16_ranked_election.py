ballots = [[1,4,3,-1,-1],[2,1,-1,-1,-1],[1,3,2,0,-1],[3,2,4,0,1],[2,3,4,0,-1]]
import pandas as pd

print(pd.DataFrame(ballots).value_counts())