import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

# CSV 파일 로드
df = pd.read_csv('height_weight.csv')

# 스트림릿 제목
st.title('Height vs Weight Scatter Plot')

# 산포도 그리기
fig, ax = plt.subplots()
ax.scatter(df['H'], df['W'])
ax.set_xlabel('Height (H)')
ax.set_ylabel('Weight (W)')
ax.set_title('Height vs Weight')

# 스트림릿에 플롯 표시
st.pyplot(fig)