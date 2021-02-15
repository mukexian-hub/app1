import streamlit as st
st.write('测试第一个程序')
opt = st.sidebar.selectbox('输入第一个选择项',['A','B'])
st.write('您输入的选择项是：',opt)
