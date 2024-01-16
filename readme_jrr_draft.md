## World Inflation Analysis
### Data:
#### "Latitude and Longitude for Every Country and State"
* Publisher: [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/latitude-and-longitude-for-every-country-and-state)
* Author: Paul Mooney
* Format: CSV file
* Copyright Information: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0 DEED)
* Use: This data was used to create a map, plotted with points, based on longitude and latitude

#### "ISO-3166-Countries-with-Regional-Codes"
* Publisher: [Github](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv)
* Author: Luke Duncalfe
* Format: CSV file
* Copyright Information: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0 DEED)
* Use: This data was used to merge two dataframes, using ISO-2 and ISO-3 codes.

 #### "Inflation, consumer prices (annual %)"
* Publisher: [The World Bank](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG)
* Source: International Monetary Fund, International Financial Statistics and data files
* Format: CSV file
* Copyright Information: Creative Commons License (CC BY 4.0)
* Use: This data was used to create two data visualizations: one heatmap bar chart and one plotted point map.

### Imports:
* from pathlib import Path
* import datetime as dt
* import hvplot.pandas
* import pandas as pd
* import geopandas as gpd
* import matplotlib.pyplot as plt
* import numpy as np
* import geoviews as gv
* import geoviews.feature as gf
* from geoviews import dim, opts
* import altair as alt
* from vega_datasets import data
* import scipy
* from scipy import stats

### Other attributed technical resources:
* Scipy z-scores: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html
* Pandas dataframe mask: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html
* Altair heatmap example: https://altair-viz.github.io/gallery/annual_weather_heatmap.html

### Results:
1. The data demonstrates how inflation increased worldwide in 2022. This calculation was based on data that was cleaned to remove outliers outside of three standard deviations, relative to the year.
2. The data showed which countries were impacted the most and least by inflation, relative to the ten-year mean. This calculation was based on data that was cleaned to remove outliers outside of three standard deviations, relative to the country in all years of available data.
#### Altair Heatmap Bar Chart
![high world inflation map](world_inflation_geo_data\agg_world_inflation.png)
#### Geoviews Plotted Map
![high world inflation map](world_inflation_geo_data\high_world_inflation.png)











## US Inflation Analysis
### Data:
#### "Consumer Price Index for All Urban Consumers (CPI-U): All items in U.S. city average, all urban consumers, seasonally adjusted"
* Source: [Bureau of Labor Statistics Beta Labs](https://beta.bls.gov/dataViewer/view/timeseries/CUSR0000SA0)
* Copyright Information: "The Bureau of Labor Statistics (BLS) is a Federal government agency and everything that we publish, both in hard copy and electronically, is in the public domain, except for previously copyrighted photographs and illustrations. You are free to use our public domain material without specific permission, although we do ask that you cite the Bureau of Labor Statistics as the source."
* Format: CSV file
* Use: This dataset describes the seasonally-adjusted consumer price index (CPI-U) - a common metric used to measure inflation in the United States.

### Imports:
* from pathlib import Path
* import datetime as dt
* import pandas as pd
* import numpy as np
* import hvplot.pandas

### Results:
This data was used to create a line graph that demonstrates how inflation rose sharply in 2022, based on the seasonally adjusted consumer price index for all urban consumers (CPI-U).
#### hvPlot line graph
![inflation line graph](cpi_data\inflation_cpiu.png)







## I bonds Analysis
### Data:

#### "Series I Bond Rates"
* Publisher: [Your Treasury Direct](https://www.yourtreasurydirect.com/rates/ibonds)
* Source: Department of the Treasury, Treasury Direct website
* Copyright Information:

    Your Treasury Direct - a for-profit company - states that "You may not access or use the Services for any purpose other than that for which we make the Services available. The Services may not be used in connection with any commercial endeavors except those that are specifically endorsed or approved by us. As a user of the Services, you agree not to: Systematically retrieve data or other content from the Services to create or compile, directly or indirectly, a collection, compilation, database, or directory without written permission from us."

    *Essentially, this for-profit website is using public domain information from the federal government and can, therefore, make no specific claims to the data itself. Ideally, the Treasury's website would have made a CSV file, but we were not able to locate one for I bonds, specifically.*
* Format: CSV file
* Use: This dataset describes six-month I bond return rates, including the fixed interest rate and the variable interest rate. 


#### "SERIES I SAVINGS BOND EARNINGS RATES EFFECTIVE NOVEMBER 1, 2023"
* Publisher: [Treasury Direct](https://treasurydirect.gov/files/savings-bonds/i-bond-rate-chart.pdf)
* Source: Department of the Treasury, Treasury Direct website
* Copyright Information: public domain
* Format: table in PDF file
* Use: This data was used to fill in missing data from the oiriginal CSV


### Imports:
* from pathlib import Path
* import datetime as dt
* import pandas as pd
* import matplotlib.pyplot as plt
* import numpy as np
* import hvplot.pandas

### Results:
This data was used to create a stacked bar chart, showing how I bond interest rates were significantly higher in 2022 than previous years.
####  hvPlot stacked bar chart
![ibonds stacked bar chart](ibonds_data\ibonds_bar_chart.png)