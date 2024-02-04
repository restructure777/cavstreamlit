import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルのパス
file_path = 'data/cav_table3.csv'

#---------全体の表の表示-----------
# Streamlitアプリのタイトル
st.title('全国の自動運転バス(実証実験)状況一覧')

# CSVファイルを読み込む
data = pd.read_csv(file_path)

# Streamlitでデータフレームを表示
st.dataframe(data)

#---------事業者と車種のグラフ表示-----------
# CSVファイルを読み込む
df = pd.read_csv(file_path)

# Streamlitアプリのタイトル
st.title('主な事業者別・車種別集計')

# 選択オプション
options = ['主な自動運転事業者', '車種等']

# ユーザーがオプションを選択できるドロップダウンメニューを作成
selected_option = st.selectbox('データの種類を選択してください', options)

# 選択に応じて異なるグラフを表示
if selected_option == '主な自動運転事業者':
    # 「主な自動運転事業者」の値の出現回数をカウント
    company_counts = df['主な自動運転事業者'].value_counts()

    # 水平の棒グラフをプロット
    plt.figure(figsize=(10, 8))
    company_counts.plot(kind='barh')
    plt.xlabel('Count')
    plt.ylabel('Company Type')
    plt.title('Frequency of Company Types')
    plt.gca().invert_yaxis()  # y軸を逆順にする

    # Streamlitでグラフを表示
    st.pyplot(plt)

elif selected_option == '車種等':
    # 「車種等」の値の出現回数をカウント
    vehicle_counts = df['車種等'].value_counts()

    # 水平の棒グラフをプロット
    plt.figure(figsize=(10, 8))
    vehicle_counts.plot(kind='barh')
    plt.xlabel('Count')
    plt.ylabel('Vehicle Type')
    plt.title('Frequency of Vehicle Types')
    plt.gca().invert_yaxis()  # y軸を逆順にする

    # Streamlitでグラフを表示
    st.pyplot(plt)

#---------事業者ごとにフィルタリング-----------
# Streamlitアプリのタイトル
st.title('主な事業者別の状況')

# CSVファイルを読み込む
data = pd.read_csv(file_path)

# 表示する事業者のリスト
companies = [
    'BOLDLY Inc.',
    'AISANTECHNOLOGY CO.,LTD.',
    'TIER IV, Inc.',
    'Advanced Smart Mobility Co., Ltd.',
    'Nippon Mobility Inc.'
]

# ユーザーが選択した事業者を格納するリスト
selected_companies = []

# 各事業者に対してチェックボックスを作成
for index, company in enumerate(companies):
    if st.checkbox(company, key=f"{company}_{index}"):  # インデックスをキーに追加
        selected_companies.append(company)

# ユーザーが選択した事業者に基づいてデータをフィルタリング
if selected_companies:
    filtered_data = data[data['主な自動運転事業者'].str.contains('|'.join(selected_companies))]
    st.dataframe(filtered_data)  # フィルタリングしたデータフレームを表示

    # 選択した事業者ごとに「車種等」内容について円グラフで内訳を表示
    for company in selected_companies:
        company_data = filtered_data[filtered_data['主な自動運転事業者'].str.contains(company)]
        vehicle_counts = company_data['車種等'].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(vehicle_counts, labels=vehicle_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title(f'{company} ')
        st.pyplot(plt)

    # 選択した事業者ごとに「latitude」「longitude」の内容を元に地図上へプロット
    st.subheader("自動運転実施場所")
    map_data = filtered_data[['latitude', 'longitude']].dropna()
    st.map(map_data)
else:
    st.write("事業者を選択してください。")
