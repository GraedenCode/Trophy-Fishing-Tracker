import streamlit as st
import pandas
from streamlit import empty

df = pandas.read_csv('FishingTracker.csv')

st.set_page_config(layout='wide')

def update_current_rank(checkbox,box_num, rank):
    try:
        if st.session_state[checkbox] == True:
            df.loc[box_num, rank] = True
        elif st.session_state[checkbox] == False:
            df.loc[box_num, rank] = False
        df.to_csv('FishingTracker.csv', index=False)
    except KeyError:
        pass


def print_fish(data, col_num, box_num):
        container = st.container(height=220, border=True)
        with container:
            st.title(data['fish_name'])
            left, right = st.columns(2, vertical_alignment='bottom')
            with left:
                st.image('Images/' + data['image'], width=100)
            with right:
                for i, rank in enumerate(['Bronze','Silver','Gold','Diamond']):
                    st.checkbox(label=rank,
                                key=data['image'].strip('.png') + rank,
                                value=data[rank],
                                on_change=update_current_rank(data['image'].strip('.png')+ rank, box_num, rank)
                                )


col1, col2, col3, col4 = st.columns(4)

x = 4
y = 0

for col_num,col in enumerate([col1,col2,col3,col4]):
    with col:
        if col_num == 0:
            for box_num, data in df[:x].iterrows():
                print_fish(data, col_num, box_num)
        else:
            for box_num, data in df[y:x].iterrows():
                print_fish(data, col_num, box_num)
    x = x + 4
    y = y + 4