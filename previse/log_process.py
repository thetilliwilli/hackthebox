import pandas as pd
from sys import argv

if argv[1] == 'space':
    delims = ' '
elif argv[1] == 'tab':
    delims = '\t'
else:
    delims = ','

df = pd.read_csv('/var/www/file_access.log', 
                index_col='time', 
                names=['time', 'user', 'fileID'])
df.to_csv('/var/www/out.log', sep=delims)
