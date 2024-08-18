import numpy as np
import streamlit as st
import pandas as pd
from connect import sql_conn
from function import graph, cal_fin
from sqlalchemy import create_engine
import requests
import yfinance as yf

api_key = 'cqmt8m9r01qjs6oci5i0cqmt8m9r01qjs6oci5ig'
url = f'https://finnhub.io/api/v1/stock/symbol?exchange=US&token={api_key}'

######### DB 연결부 ##########
db_conn = sql_conn.DBConn()
conn, cur = db_conn.active_conn()

if conn is None or cur is None:
    st.error("DB가 그대를 거부하리")
else:
    st.success("DB연결 성공적.")
##############################

# 데이터 요청
response = requests.get(url)
symbols_data = response.json()
symbols = [item['symbol'] for item in symbols_data]
descriptions = {item['symbol']: item['description'] for item in symbols_data}

# 검색어 입력
search_term = st.text_input("심볼을 검색하세요:")

if search_term:
    search_term = search_term.lower()
    filtered_symbols = [
        (symbol, description) for symbol, description in descriptions.items()
        if search_term in description.lower()
    ]
else:
    filtered_symbols = list(descriptions.items())

# Initialize session state for selected_symbol if not exists
# if 'selected_symbol' not in st.session_state:
#     st.session_state.selected_symbol = []
if 'selected_symbol' not in st.session_state:
    st.session_state.selected_symbol = None

# 검색된 심볼 목록에서 선택 (단일 선택 지원)
selected_symbol_str = st.selectbox(
    "검색한 회사명을 포함하는 심볼 리스트중에서 심볼을 선택하세요:",
    [f"{symbol} - {description}" for symbol, description in filtered_symbols],
    key='unique_selectbox_symbol'  # 고유한 키 제공
)

# Extract the selected symbol key
if selected_symbol_str:
    selected_symbol_key = selected_symbol_str.split(" - ")[0]
    selected_description = descriptions.get(selected_symbol_key, "설명 없음")
else:
    selected_symbol_key = None
    selected_description = "설명 없음"

# 선택된 심볼의 재무제표 데이터를 리스트에 추가
if selected_symbol_key:
    company = yf.Ticker(selected_symbol_key)
    financials = company.financials
    if not financials.empty:
        financials_df = financials.T  # Transpose to make columns as financial metrics
        st.write(f"선택한 심볼:{selected_symbol_key} - {selected_description}")
        st.write(financials_df)
    else:
        st.write("선택한 심볼에 대해 재무 데이터를 찾을 수 없습니다.")
else:
    st.write("심볼을 선택하세요.")

# 선택된 심볼 및 설명 출력
if selected_symbol_key:
    #st.write(f"선택한 심볼: {selected_description}")

    # 선택된 심볼에 대한 재무 지표 계산 및 출력 (가정: cal_fin.get_financial_ratios 함수가 있음)
    fidf = cal_fin.get_financial_ratios(selected_symbol_key)
    st.write(fidf)

    # 그래프 추천 및 출력 (가정: graph.recommend_graph 함수가 있음)
    # quest = st.text_input("어떠한 형태의 그래프를 그리고 싶으십니까?", key='unique_graph_question')  # 고유한 키 제공
    # graph.recommend_graph(fidf, quest)