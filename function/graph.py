import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def draw_line_plot(df, x_var, y_var):
    st.write(f"Line plot between {x_var} and {y_var}")
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x=x_var, y=y_var, ax=ax)
    st.pyplot(fig)

def draw_bar_plot(df, x_var):
    st.write(f"Bar plot of {x_var}")
    fig, ax = plt.subplots()
    sns.barplot(x=x_var, y=df[x_var].index, data=df, ax=ax)
    st.pyplot(fig)

def draw_histogram(df, x_var):
    st.write(f"Histogram of {x_var}")
    fig, ax = plt.subplots()
    sns.histplot(df[x_var], ax=ax, bins=30)
    st.pyplot(fig)

def draw_pie_chart(df, x_var):
    st.write(f"Pie chart of {x_var}")
    fig, ax = plt.subplots()
    df[x_var].value_counts().plot.pie(ax=ax, autopct='%1.1f%%')
    st.pyplot(fig)

def draw_box_plot(df, x_var):
    st.write(f"Box plot of {x_var}")
    fig, ax = plt.subplots()
    sns.boxplot(x=df[x_var], ax=ax)
    st.pyplot(fig)

def draw_scatter_plot(df, x_var, y_var):
    if x_var and y_var:
        st.write(f"Scatter plot between {x_var} and {y_var}")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_var, y=y_var, ax=ax)
        st.pyplot(fig)

def draw_pair_plot(df):
    st.write("Pair Plot")
    pair_plot = sns.pairplot(df)
    st.pyplot(pair_plot)

def recommend_graph(df, question):
    question = question.lower()
    
    if '시간' in question and '추세' in question:
        # 시계열 그래프 추천
        if 'date' in df.columns:
            return 'line'
        else:
            return 'bar'

    elif '분포' in question:
        # 히스토그램 추천
        return 'histogram'

    elif '비교' in question:
        # 막대 그래프 추천
        return 'bar'

    elif '상관' in question:
        # 산점도 추천
        return 'scatter'

    elif '비율' in question:
        # 원형 그래프 추천
        return 'pie'

    elif '상자 그림' in question:
        # 상자 그림 추천
        return 'box'

    elif '쌍 그림' in question:
        # 쌍 그림 추천
        return 'pair'

    else:
        return 'line'  # 기본적으로 선 그래프를 추천

# 시각화 생성 함수
def create_graph(df, graph_type, x_var=None, y_var=None):
    if graph_type == 'line':
        if x_var and y_var:
            draw_line_plot(df, x_var, y_var)
        else:
            st.write("Need x and y variables for a line plot.")
    
    elif graph_type == 'bar':
        if x_var:
            draw_bar_plot(df, x_var)
        else:
            st.write("Need x variable for a bar plot.")
    
    elif graph_type == 'histogram':
        if x_var:
            draw_histogram(df, x_var)
        else:
            st.write("Need x variable for a histogram.")
    
    elif graph_type == 'pie':
        if x_var:
            draw_pie_chart(df, x_var)
        else:
            st.write("Need x variable for a pie chart.")
    
    elif graph_type == 'box':
        if x_var:
            draw_box_plot(df, x_var)
        else:
            st.write("Need x variable for a box plot.")
    
    elif graph_type == 'scatter':
        if x_var and y_var:
            draw_scatter_plot(df, x_var, y_var)
        else:
            st.write("Need x and y variables for a scatter plot.")
    
    elif graph_type == 'pair':
        draw_pair_plot(df)
    
    else:
        st.write("Unknown graph type.")