# filename: plot_stocks_plotly.py

import yfinance as yf
import plotly.graph_objects as go

def download_stock_data(ticker, start_date, end_date):
    """ Download stock data from Yahoo Finance for given ticker. """
    return yf.download(ticker, start=start_date, end=end_date)

def calculate_gains(df, column='Adj Close'):
    """ Calculate the YTD gains as a percentage. """
    return ((df[column] - df[column].iloc[0]) / df[column].iloc[0]) * 100

def plot_data(nvda_gains, tsla_gains):
    """ Plot the data using Plotly and save it to a file. """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=nvda_gains.index, y=nvda_gains, mode='lines', name='NVDA YTD Gain %'))
    fig.add_trace(go.Scatter(x=tsla_gains.index, y=tsla_gains, mode='lines', name='TSLA YTD Gain %'))
  
    fig.update_layout(
        title='YTD Stock Gains for NVDA and TSLA',
        xaxis_title='Date',
        yaxis_title='Gain (%)',
        template="plotly_dark"
    )
  
    fig.write_image('ytd_stock_gains.png')
    fig.show()

def main():
    start_date = '2024-01-01'
    end_date = '2024-06-16'
    
    # Download data
    nvda_data = download_stock_data('NVDA', start_date, end_date)
    tsla_data = download_stock_data('TSLA', start_date, end_date)
    
    # Calculate YTD gains
    nvda_gains = calculate_gains(nvda_data)
    tsla_gains = calculate_gains(tsla_data)
    
    # Plotting data using Plotly
    plot_data(nvda_gains, tsla_gains)

if __name__ == "__main__":
    main()