import haslib.core as hl 
from . import utils
from datetime import datetime
, timedelta

def get_data(start=None):
    """Get data from the API and return a list of dictionaries with each entry representing one day'sworth of stock prices."""
    # Get current date in YYYY-MM-DD format for use later on when we need to calculate dates
    
    if start is None:
        today = str((datetime.today() - timedelta(days=1)).date())
    else :
        
        
        today = str(((datetime.strptime(str(start), '%Y-%m-%d')
                      + timedelta(-365)) ).date()).replace('-', '')
        url = 'https://api.covidtracking.com/v2/' \
            f'daily?country={utils._COUNTRY}&' \
                
                ='get_data.BaseExceptionGroup
                '
                s&state=%&date='
                + today
                return pd.read_json(url)
                
                