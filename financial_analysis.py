import pandas as pd



nifty50_data = pd.read_csv("/content/nifty50_closing_prices.csv")



# check for missing values

missing_values = nifty50_data.isnull().sum()

# check for date column format

date_format_check = pd.to_datetime(nifty50_data['Date'], errors='coerce').notna().all()

# check if the data has sufficient rows for time-series analysis

sufficient_rows = nifty50_data.shape[0] >= 20  # Minimum rows needed for rolling/moving averages

# preparing a summary of the checks

data_preparation_status</span> = {

    "Missing Values in Columns": missing_values[missing_values > 0].to_dict(),</span>

    "Sufficient Rows for Time-Series Analysis": sufficient_rows

}

data_preparation_status

{'Missing Values in Columns': {'HDFC.NS': 24}, 'Date Column Format Valid': True, 'Sufficient Rows for Time-Series Analysis': True}

# drop the HDFC.NS column since it contains 100% missing values



<span class="cm-comment"># convert the 'Date' column to datetime format

nifty50_data['Date'] = pd.to_datetime(nifty50_data['Date'])

# sort the dataset by date to ensure proper time-series order

nifty50_data = nifty50_data.sort_values(by='Date')</pre>

# reset index for a clean dataframe

nifty50_data.reset_index(drop=True, inplace=True)

# calculate descriptive statistics

descriptive_stats = nifty50_data.describe().T  # Transpose for better readability

descriptive_stats = descriptive_stats[['mean', 'std', 'min', 'max']]

descriptive_stats.columns <span class="cm-operator">= ['Mean', 'Std Dev', 'Min', 'Max']

print(descriptive_stats)

                       Mean     Std Dev           Min           MaxRELIANCE.NS     2976.912506   41.290551   2903.000000   3041.850098HDFCBANK.NS     1652.339579   28.258220   1625.050049   1741.199951ICICIBANK.NS    1236.770818   36.438726   1174.849976   1338.449951INFY.NS         1914.558324   30.240685   1862.099976   1964.500000TCS.NS          4478.349976   70.822718   4284.899902   4553.750000KOTAKBANK.NS    1809.422918   32.936318   1764.150024   1904.500000HINDUNILVR.NS   2845.333344   65.620694   2751.050049   2977.600098ITC.NS           507.739581    5.472559    497.299988    519.500000LT.NS           3647.099976   60.511574   3536.949951   3793.899902SBIN.NS          802.233332   17.442330    768.599976    824.799988BAJFINANCE.NS   7203.118754  306.658594   6722.200195   7631.100098BHARTIARTL.NS   1572.574997   67.346274   1449.150024   1711.750000HCLTECH.NS      1753.743744   46.874886   1661.449951   1813.750000ASIANPAINT.NS   3231.654175   88.793647   3103.199951   3383.250000AXISBANK.NS     1191.879155   27.369408   1158.750000   1245.000000DMART.NS        5143.058329  155.593701   4901.500000   5361.399902MARUTI.NS      12320.356201  109.587342  12145.750000  12614.500000ULTRACEMCO.NS  11472.318807  172.673053  11200.900391  11798.299805TITAN.NS        3654.899974   95.697721   3474.899902   3797.199951SUNPHARMA.NS    1819.299993   34.792913   1750.650024   1866.099976M&M.NS          2763.954183   56.045817   2654.250000   2950.850098NESTLEIND.NS    2539.102081   46.123738   2492.500000   2699.550049WIPRO.NS         529.764582   11.824190    512.400024    551.900024ADANIGREEN.NS   1891.595835   54.031206   1788.199951   2003.949951TATASTEEL.NS     152.277083    1.893183    148.169998    155.699997JSWSTEEL.NS      943.729167   15.778456    917.150024    981.549988POWERGRID.NS     335.285414    3.013865    328.549988    340.850006ONGC.NS          309.819995   16.989364    285.250000    330.750000NTPC.NS          407.133334    8.990767    389.649994    423.950012COALINDIA.NS     507.735413   20.470753    477.950012    538.849976BPCL.NS          347.529167    9.011248    324.450012    360.700012IOC.NS           173.630416    3.702380    165.039993    181.339996TECHM.NS        1626.229172   21.236330   1579.199951   1656.050049INDUSINDBK.NS   1428.679164   33.914618   1381.300049   1484.750000DIVISLAB.NS     5171.531250  247.674895   4723.149902   5498.649902GRASIM.NS       2718.235443   35.912080   2636.699951   2784.350098CIPLA.NS        1627.025004   29.773691   1562.849976   1671.800049BAJAJFINSV.NS   1796.470825   99.422795   1602.099976   1916.800049TATAMOTORS.NS   1044.662498   52.496391    962.049988   1121.650024HEROMOTOCO.NS   5619.377096  247.092728   5244.399902   6013.250000DRREDDY.NS      6785.795817  175.124908   6502.549805   7062.450195SHREECEM.NS    25299.906169  429.919834  24692.199219  26019.650391BRITANNIA.NS    5935.202026  144.164343   5703.350098   6210.549805UPL.NS           596.343750   16.975821    566.150024    619.200012EICHERMOT.NS    4863.831258   68.442418   4726.649902   4963.149902SBILIFE.NS      1849.331243   43.189734   1761.300049   1928.650024ADANIPORTS.NS   1462.916677   26.223794   1408.199951   1503.500000BAJAJ-AUTO.NS  10999.654134  659.810841   9779.700195  11950.299805HINDALCO.NS      681.885417   15.952804    647.700012    711.849976

# assign weights to a subset of stocks (example: RELIANCE.NS, HDFCBANK.NS, ICICIBANK.NS)

weights = [0.4, 0.35, 0.25]

portfolio_data = nifty50_data[['RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS']]

# calculate daily returns

daily_returns = portfolio_data.pct_change().dropna()

# calculate portfolio returns

portfolio_returns = (daily_returns * weights).sum(axis=1)

# display portfolio returns

portfolio_returns.head()

# Calculate standard deviation (volatility)

volatility = daily_returns.std()

# Calculate VaR (95% confidence level)

confidence_level = 0.05

VaR = daily_returns.quantile(confidence_level)

# Display risk metrics

risk_metrics = pd.DataFrame({'Volatility (Std Dev)': volatility, 'Value at Risk (VaR)': VaR})

print(risk_metrics)

              Volatility (Std Dev)  Value at Risk (VaR)RELIANCE.NS               0.008708            -0.013624HDFCBANK.NS               0.006901            -0.005987ICICIBANK.NS              0.011594            -0.008577

<span class="cm-keyword">import plotly</span>.figure_factory as ff

# calculate correlation matrix

correlation_matrix = daily_returns.corr()

fig</span> = ff.create_annotated_heatmap(

    z=correlation_matrix.values,

    x=list(correlation_matrix.columns),

    y=list(correlation_matrix.index),

    annotation_text=correlation_matrix.round(2).values,

    colorscale='RdBu', 

    showscale=True

)

fig.update_layout(

    title="Correlation Matrix of Stock Returns",</pre>

    title_x=0.5,

    font=dict(size=12),

    plot_bgcolor='white',

fig.show()

import plotly.graph_objects as go

nifty50_data['RELIANCE_5d_MA'] = nifty50_data['RELIANCE.NS'].rolling(window=5).mean()

nifty50_data['RELIANCE_20d_MA'] = nifty50_data['RELIANCE.NS'].rolling(window ).mean()

=E2=80=8B

fig = go.Figure()

fig.add_trace(go.<span class="cm-property">Scatter(

    x=nifty50_data['Date'],

    y=nifty50_data['RELIANCE.NS'],

    mode='lines',

    name='RELIANCE.NS Price'

))

fig.add_trace(go.Scatter(

    y=nifty50_data['RELIANCE_5d_MA'],

    name='5-Day MA'

fig.add_trace(go.Scatter(

<span role="presentation" style="padding-right: 0.1px;">    x=nifty50_data['Date'],

    y=nifty50_data['RELIANCE_20d_MA'],

    name='20-Day MA'

))</pre>

</pre>

    title="Moving Averages for RELIANCE.NS",

    xaxis_title="Date",

    yaxis_title="Price",

    template="plotly_white",

    legend=dict(title="Legend")
    )
fig.show()
