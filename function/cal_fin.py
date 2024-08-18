import yfinance as yf
import pandas as pd

# 매출 총 이익률 계산
def gross_profit_margin(ticker):
    company = yf.Ticker(ticker)
    financials = company.financials
    if not financials.empty:
        latest_data = financials.iloc[:, 0]
        if 'Gross Profit' in latest_data and 'Total Revenue' in latest_data:
            total_revenue = latest_data['Total Revenue']
            if total_revenue != 0:
                gross_profit = (latest_data['Gross Profit'] / total_revenue) * 100
                return gross_profit
    return None

# Net Profit Margin 계산
def net_profit_margin(ticker):
    company = yf.Ticker(ticker)
    financials = company.financials
    if not financials.empty:
        latest_data = financials.iloc[:, 0]
        if 'Net Income' in latest_data and 'Total Revenue' in latest_data:
            total_revenue = latest_data['Total Revenue']
            if total_revenue != 0:
                net_profit = (latest_data['Net Income'] / total_revenue) * 100
                return net_profit
    return None

# Operating Margin 계산
def operating_margin(ticker):
    company = yf.Ticker(ticker)
    financials = company.financials
    if not financials.empty:
        latest_data = financials.iloc[:, 0]
        if 'Operating Income' in latest_data and 'Total Revenue' in latest_data:
            total_revenue = latest_data['Total Revenue']
            if total_revenue != 0:
                operating_margin_result = (latest_data['Operating Income'] / total_revenue) * 100
                return operating_margin_result
    return None

# ROA 계산
def balance_sheet(ticker):
    company = yf.Ticker(ticker)
    financials = company.financials
    balance_sheet = company.balance_sheet
    if not balance_sheet.empty and not financials.empty:
        if 'Total Assets' in balance_sheet.index and 'Net Income' in financials.index:
            total_assets = balance_sheet.loc['Total Assets'].iloc[0]
            net_income = financials.loc['Net Income'].iloc[0]
            if total_assets != 0:
                roa = (net_income / total_assets) * 100
                return roa
    return None

# ROE 계산
def shareholders_equity(ticker):
    company = yf.Ticker(ticker)
    financials = company.financials
    balance_sheet = company.balance_sheet
    if not balance_sheet.empty and not financials.empty:
        if 'Total Stockholder Equity' in balance_sheet.index and 'Net Income' in financials.index:
            net_income = financials.loc['Net Income'].iloc[0]
            shareholders_equity = balance_sheet.loc['Total Stockholder Equity'].iloc[0]
            if shareholders_equity != 0:
                roe = (net_income / shareholders_equity) * 100
                return roe
    return None

# Current Ratio 계산
def current_ratio(ticker):
    company = yf.Ticker(ticker)
    balance_sheet = company.balance_sheet
    if not balance_sheet.empty:
        if 'Total Current Assets' in balance_sheet.index and 'Total Current Liabilities' in balance_sheet.index:
            current_assets = balance_sheet.loc['Total Current Assets'].iloc[0]
            current_liabilities = balance_sheet.loc['Total Current Liabilities'].iloc[0]
            if current_liabilities != 0:
                current_ratio_cal = current_assets / current_liabilities
                return current_ratio_cal
    return None

# Debt Ratio 계산
def debt_ratio(ticker):
    company = yf.Ticker(ticker)
    balance_sheet = company.balance_sheet
    if not balance_sheet.empty:
        if 'Total Liabilities Net Minority Interest' in balance_sheet.index and 'Total Assets' in balance_sheet.index:
            total_liabilities = balance_sheet.loc['Total Liabilities Net Minority Interest'].iloc[0]
            total_assets = balance_sheet.loc['Total Assets'].iloc[0]
            if total_assets != 0:
                debt_ratio = total_liabilities / total_assets
                return debt_ratio
    return None

# P/E Ratio 계산
def pe_ratio(ticker):
    company = yf.Ticker(ticker)
    stock_info = company.info
    if 'forwardEps' in stock_info and 'regularMarketPrice' in stock_info:
        forward_eps = stock_info['forwardEps']
        regular_market_price = stock_info['regularMarketPrice']
        if forward_eps != 0:
            pe_ratio_cal = regular_market_price / forward_eps
            return pe_ratio_cal
    return None

# Dividend Yield 계산
def dividend_yield(ticker):
    company = yf.Ticker(ticker)
    stock_info = company.info
    if 'dividendYield' in stock_info and stock_info['dividendYield'] is not None:
        dividend_yield_cal = stock_info['dividendYield'] * 100
        return dividend_yield_cal
    return None

# 모든 재무 비율 가져오기
def get_financial_ratios(ticker):
    data = {
        'Gross Profit Margin': gross_profit_margin(ticker),
        'Net Profit Margin': net_profit_margin(ticker),
        'Operating Margin': operating_margin(ticker),
        'ROA': balance_sheet(ticker),
        'ROE': shareholders_equity(ticker),
        'Current Ratio': current_ratio(ticker),
        'Debt Ratio': debt_ratio(ticker),
        'P/E Ratio': pe_ratio(ticker),
        'Dividend Yield': dividend_yield(ticker)
    }
    return pd.DataFrame(data, index=[ticker])
