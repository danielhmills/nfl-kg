import os
import pandas as pd

p = 'data'
def download():
    url =['http://nflsavant.com/pbp_data.php?year=2020', 'http://nflsavant.com/pbp_data.php?year=2019', 'http://nflsavant.com/pbp_data.php?year=2018', 'http://nflsavant.com/pbp_data.php?year=2017', 'http://nflsavant.com/pbp_data.php?year=2016', 'http://nflsavant.com/pbp_data.php?year=2015', 'http://nflsavant.com/pbp_data.php?year=2014']
    for u in url:
        df = pd.read_csv(u)
        n = 'pbp-' + u[-4:] + '.csv'
        df.to_csv(p + '/' + n,index=False)

if os.path.isdir(p) is False:
    os.mkdir(p)
    download()
else:
    download()

print(p)