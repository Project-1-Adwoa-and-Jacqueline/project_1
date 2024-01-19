# **Executive Summary: *Inflation Investing in 2022***

## Project Overview
The aim of this project was two-fold. First, we aimed analyze the scope and significance of inflation in 2022. Second, we aimed to analyze inflation impacted securities - specifically I bonds and S&P 500 stocks - and made investing recommendations, based on that analysis. These analyses resulted in eight data visualizations that demonstrate our results:
1. Aggregate Inflation rate Worldwide 2013-2022
2. 2022 Inflation Rate, Expressed as Percentage of 10-Year Mean
3. USA Inflation Rate: Consumer Price Index for All Urban Consumers (CPI-U)
4. I bonds Aggregate Annualized Interest Rate
5. Cumulative Returns of the Top 5 Stocks & S&P 500 Index
6. Rolling Standard Deviation of the Top 5 Stocks & S&P 500 Index
7. Comparison of Total Returns: Top 5 Stocks, S&P 500 Index, and I bonds

## Approach
We essentially divided the task into a data analysis of the inflation indicators and an analysis of stock data between the two members of our group. We created a repository on Github and communicated over Slack and SMS. During class meetings, we discussed to-do lists and progress.

# Analysis: The State of Inflation in 2022
## World Inflation
### Datasets
The following data sources were used to create a merged dataframe:
1. #### "Latitude and Longitude for Every Country and State"
    * Author: Paul Mooney ([Kaggle](https://www.kaggle.com/datasets/paultimothymooney/latitude-and-longitude-for-every-country-and-state))
    * Copyright Information: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0 DEED)
    * Use: This data was used to create a map, plotted with points, based on longitude and latitude
2. #### "Inflation, consumer prices (annual %)"
    * Source: International Monetary Fund, International Financial Statistics and data files ([The World Bank](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG))
    * Copyright Information: Creative Commons License (CC BY 4.0)
    * Use: This data was used for inflation data by country and year to create two data visualizations: one heatmap bar chart and one plotted point map.
3. #### "ISO-3166-Countries-with-Regional-Codes"
    * Author: Luke Duncalfe ([Github](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv))
    * Copyright Information: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0 DEED)
    * Use: This data was used more accurately to merge the two dataframes, using ISO-2 and ISO-3 codes.
### Imports
* Pathlib, DateTime, hvPlot, pandas, GeoPandas, Matplotlib, NumPy, Vega-Altair, SciPy
### Other attributed technical resources
* Scipy z-scores: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html
* Pandas dataframe mask: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html
* Altair heatmap example: https://altair-viz.github.io/gallery/annual_weather_heatmap.html
### Results
For both data visualizations, data was first filtered, limited to ten years, ending in 2022.
#### Altair Heatmap Bar Chart
1. **How much did inflation increase across the world in 2022?** First, the data was filtered to remove outliers outside of three standard deviations, relative to the year, using z-scores (SciPy) and the "mask" method. This means that 99.73% of the available data was used to calculate the aggregate inflation rate worldwide, eliminating the impact of failed states on the results. Then, an Altair "2D Histogram Heatmap" was created to show the worldwide inflation rate in 2022 and in relationship to the worldwide inflation rate for the past ten years. A box plot was used to inform the parameters of the heatmap.

    Although statistics showed that the mean inflation in those ten years was approximately 4.3%, the heatmap shows that the inflation rate was most typically around 3.5% before COVID-19 impacted the world economy. The heatmap also shows that inflation was significantly higher at 10.29% in 2022 after rising to 5.59% in 2021.
    ![agg world inflation](https://github.com/Project-1-Adwoa-and-Jacqueline/project_1/blob/main/agg_world_inflation.png)

2. **Where did inflation increase significantly?** First, the data was filtered to remove outliers outside of three standard deviations, relative to the country, using z-scores (SciPy) and the "mask" method. This means that 99.73% of the available data was used for calculations, eliminating very irregular data - possibly from periods of civil war, misreporting, etc. From that filtered dataframe, the ten-year mean inflation rate was calculated for each country. Finally, the 2022 inflation rate was expressed, relative to the mean to identify inflation rates that were significant in the context of each country's economy. Those values were plotted (GeoViews), using coordinates, and assigned a color that signifies the significance of each country's inflation rate in 2022. A box plot was used to inform the cmap scale.

    While we had originally intended to use polygons to create this map, we decided to use dot plots because we did not want a granular understanding of inflation or to highlight differences between specific countries. Instead, the map is used to identify regions where inflation increased significiantly: The Americas, West Africa, Europe, The Arabian/Persian Gulf, Southeast Asia, Australasia, and Oceania. In those regionals, most countries experienced an inflation rate in 2022 that was more than 200% of the mean and often much more. The data also demonstrates that countries in Asia and other parts of Africa were less impacted by inflation in 2022, possibly owing to protectionist trade practices and/or irregular reporting.

    If the mandate of this project were more detailed, I would like to explore the relationship between relative inflation and major trading partners.
    ![high world inflation map](https://github.com/Project-1-Adwoa-and-Jacqueline/project_1/blob/main/high_world_inflation.png)


## US Inflation Analysis: Consumer Price Index
### Dataset:
#### "Consumer Price Index for All Urban Consumers (CPI-U): All items in U.S. city average, all urban consumers, seasonally adjusted"
* Source: [Bureau of Labor Statistics Beta Labs](https://beta.bls.gov/dataViewer/view/timeseries/CUSR0000SA0)
* Copyright Information: public domain
* Use: This dataset describes the seasonally-adjusted consumer price index (CPI-U) - a common metric used to measure inflation in the United States.
### Imports:
* Pathlib, DateTime, Pandas, NumPy, hvPlot
### Results:
**How significant was inflation in the United States?** This data was used to create a line graph (hvPlot) that demonstrates how inflation rose sharply in 2022, based on the seasonally adjusted consumer price index for all urban consumers (CPI-U).

This dataset only required that we change the date the DateTime format to create a simpler x-axis on the graph. Other than this manipulation any other dataframe changes were discretionary. In the future, it would probably be better not to make those discretionary changes to the dataframe, but it was personally helpful to eliminate unnecessary columns to identify how other columns would be used.

In this project, the number of graphs we can show is limited, but ideally it would be good to also show a zoomed-in view of the 2019-2023 period to compare slopes of adjacent years.
    ![inflation line graph](https://github.com/Project-1-Adwoa-and-Jacqueline/project_1/blob/main/inflation_cpiu.png)


## I bonds Analysis
### Datasets:
1. #### "Series I Bond Rates"
    * Source: Department of the Treasury, Treasury Direct website ([Your Treasury Direct](https://www.yourtreasurydirect.com/rates/ibonds))
    * Copyright Information:
        * The dataset is composed of data from the Treasury, and that data is public domain.
        * Your Treasury Direct - a for-profit company - states that "You may not access or use the Services for any purpose other than that for which we make the Services available. The Services may not be used in connection with any commercial endeavors except those that are specifically endorsed or approved by us. As a user of the Services, you agree not to: Systematically retrieve data or other content from the Services to create or compile, directly or indirectly, a collection, compilation, database, or directory without written permission from us." *Essentially, this for-profit website is using public domain information from the federal government and can, therefore, make no specific claims to the data itself. Ideally, the Treasury's website would have made a CSV file, but we were not able to locate one for I bonds, specifically.*
    * Use: This dataset  - a CSV file - describes six-month I bond return rates, including the fixed interest rate and the variable interest rate. 
2. #### "SERIES I SAVINGS BOND EARNINGS RATES EFFECTIVE NOVEMBER 1, 2023"
    * Publisher: [Treasury Direct](https://treasurydirect.gov/files/savings-bonds/i-bond-rate-chart.pdf)
    * Source: Department of the Treasury, Treasury Direct website
    * Copyright Information: public domain
    * Use: This data (a table on a PDF) was used to fill in missing data from the original CSV
    * Surpringly, this data was not available as a CSV, directly on Treasury Direct.
### Imports:
* Pathlib, DateTime, pandas, Matplotlib, NumPy, hvPlot
### Technical notes:
* The variable interest rate was annualized from the given 6-month rate to perform the analysis.
* There were errors and omissions in the dataset (CSV) that needed to be corrected, using the table from the Treasury.
### Results:
**How did inflation impact the I bond market, a risk-free investment for retail investors?** I bond interest rates are determined by a fixed rate and a variable rate. The variable rate is equal to the The variable interest rate is the inflation rate, preceding that six-month period. This dataset was used to create a stacked bar chart (hvPlot), showing how I bond interest rates and inflation were significantly higher in 2022 than previous years. Based on this correlation, we can see the inflation rate itself and I bond interest rates, peaking at almost 10% in 2022. This, in turn, gave investors a high risk-free rate in 2022 - an alternative to investing in equity markets. This chart also demonstrates that inflation and I bond interest rates have not been reduced to levels from before the pandemic, continuing to make I bonds an attractive investment for consumers.

Given more time and a wider scope, I would like to analyze how many I Bonds were purchased during 2022, compared to adjacent years and data from think tanks about consumer sentiment in terms of investing in risk-free securities vs. equity markets.
![ibonds stacked bar chart](https://github.com/Project-1-Adwoa-and-Jacqueline/project_1/blob/main/ibonds_bar_chart.png)


# Stock and Index Analysis
### Datasets:
1. Yahoo Finance API
    * Copyright: "Subject to your compliance with all the terms and conditions of this Agreement, Yahoo grants you a non-exclusive, non-transferable, non-sublicensable right and license to access and use the Yahoo APIs, solely using your own Yahoo API Credentials or Yahoo API Credentials that you are expressly authorized to use, and solely for the purposes of: (i) developing a Yahoo API Client; or (ii) managing a Yahoo commercial account via the Yahoo API Client that you are expressly authorized to manage and access."
    * Use: This API is used for historical stock data.
2. "List of S&P 500 Companies"
    * Publisher: [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
    * Copyright: Creative Commons Attribution-ShareAlike License 4.0
### Imports:
* Pandas, Datetime, Numpy, Pathlib, Matplotlib, yfinance API (open source; no key); streamlit (tool)
### Process & Results
The second aim of our project is to analyze how stocks performed in 2022 – a period of high inflation and interest rates, specifically Ibonds for retail savers. This was done by accessing stocks in the S&P 500 using yfinance API tool, using a list of S&P 500 stocks from Wikipedia. Data preprocessing and cleaning was then executed for easier readability. Next, we derived the top 5 stocks that performed exceptionally during this time period.

**Which stocks in the S&P 500 performed the best?**

In no particular order the following stocks occupied the top seat:
* OXY - Occidental Petroleum Corporation ( together with its subsidiaries, engages in the acquisition, exploration, and development of oil and gas properties in the United States, the Middle East, North Africa, and Latin America. It operates through three segments: Oil and Gas, Chemical, and Midstream and Marketing.)
* CEG - Constellation Energy Corporation ( generates and sells electricity in the United States. The company operates through five segments: Mid-Atlantic, Midwest, New York, ERCOT, and Other Power Regions. It sells natural gas, and other energy-related products and services.)
* HES- Hess Corporation (an exploration and production company, explores, develops, produces, purchases, transports, and sells crude oil, natural gas liquids (NGLs), and natural gas. )
* APA - APA Corporation (through its subsidiaries, explores for, develops, and produces natural gas, crude oil, and natural gas liquids)
* SLB - Schlumberger Limited( engages in the provision of technology for the energy industry worldwide. The company operates through four divisions: Digital & Integration, Reservoir Performance, Well Construction, and Production Systems.)

Further research revealed that the all the Top 5 stocks are in the energy sector. This is due to the fact that the energy sector in 2022 performed exceptionally with a gain of 65.72% against all the S&P's 11 sectors. We saw arising trend in energy price during this particular year which benefited the energy sector. It seems to reason that the upward price trend highly correlated with the performamce of the sector. This was spurred by a global spike in commodity prices following Russia's invasion of Ukraine, energy companies, "“continued commitment to capital discipline has resulted in a strong focus towards [free cash flow] generation which companies allocated towards shareholders returns (via dividends and buybacks) and debt reduction,” Goldman Sachs analysts led by Neil Mehta.

[source](https://www.usbank.com/investing/financial-perspectives/market-news/energy-sector-performance.html)

[forbes](https://www.forbes.com/sites/dereksaul/2022/12/29/energy-stocks-outshone-peers-in-2022/?sh=4512fe775466)


**How did the S&P 500 perform?** Cumulative returns which aggregates the loss and gain over a period of time calculation was implemented to get a closer picture as to how the Top 5 stocks performed using the S&P500 as a benchmark. Over the period, S&P 500 cumulative returns remain steady where as all the Top 5 stocks experienced an upward momentum with CEG slightly topping up over the other stocks.

![cumulative_returns](https://github.com/Project-1-Adwoa-and-Jacqueline/project_1/blob/main/cum_ret.png)


**How risky was the equity market?** To measure the volatility of the stocks, a standard deviation calculation was done over a rolling window of 21 days, to access risk S&P 500 as a benchmark was in a range of about 60 and 175 experiencing a higher high and a lower low in between the range. This could be to the fact some of these stocks in the S&P 500 had  sharp movements in the course of 2022. The Top 5 stocks maintained a steadiness of about 5 and 15 volatilty

![rolling_std]([rolling _std.png](https://github.com/Project-1-Adwoa-and-Jacqueline/project_1/blob/main/rolling%20_std.png)

**Compare the index, top performers, and I bonds as options for investments for retail investors.**
To see how these stocks did in comparison with the I bonds, a sharpe ratio calculation was made:
I bonds resulted in a mean of 8.25 (aggregate annualized interest rate),
* S&P 500 (as a benchmark): 0.88462
* OXY: 0.3339239
* CEG: 0.285530
* HES: 0.409905
* APA: 0.448914
* SLB: 0.426057

To risk investing in these stocks means you risk to reward ratio will be quite rewarding not forgetting the risk associated with these stocks. I bonds on the other hand, maintain a MEAN OF 8.25 (aggregate annualized interest rate).

![Sharpe Ratio](https://github.com/Project-1-Adwoa-and-Jacqueline/project_1/blob/main/sharpe.png)

**Streamlit Tool: Compare different stock portfolios during 2022: [https://cuozhiasjb9gczsuc8skj4.streamlit.app/](https://cuozhiasjb9gczsuc8skj4.streamlit.app/)**
In an attempt to create an interactive app, streamlit was used to create a visualization of the stocks and how it performed in relation to the sharpe ratio of the bonds and that of the stocks. With this app the individual could select a few of the S&P 500 stocks to analyze how it performed in the year 2022 (using the 3y period) and what the reward ratio would be based on the sharpe ratio. All effort was made to deploy the application to streamlit but there were some technical difficulties with the pandas version, changes were made to satisfy the app requirements but there were still issues. All in all the application works fine when hosted locally.

Technical limitation: 
We can deploy the tool locally, but we are having trouble deploying it online. It is related to the pandas version, and we ran out of time to figure out how to fix it.

### Limitations & Plans For Future Research and Development:
The limitation I faced with comparing the stocks and I bonds is the fact that the I-bonds, as a risk free rate remained constant which was expected while the Top5 and S&P 500 had high sharpe ratio. What I would have loved to do was to implement the Monte Carlo Simulation, using the an initial investment and short term investment of about 1-2 years to determine if there were any form of changes between the stock and the I-bonds - will the stock returns still have higher returns than the I-bonds? Would the I-bonds beat the Top5 and S&P 500 benchmark?

### Conclusion:
From the analysis, the top5 stocks outperformed the I-bonds rate remaining constant throughout. I'd recommend a risk-tolerant individual who wants to invest a heavily percentage of his or her money in stocks and the remaining in I-bonds for diversification purposes, since the risk to reward ratio is much higher than that of the I-bonds. For a risk averse person, maybe investing heavily in the I-bonds and a portion of the money is the stocks will be appropriate.  
