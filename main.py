from utils import xiaohongshu_generator
import streamlit as st

st.header("小红书AI写作助手")
with st.sidebar:
    deepseek_api_key = st.text_input("请输入你的deepseek_api密钥：", type="password")
    st.markdown("[获取deepseek api密钥](https://platform.deepseek.com/api_keys)")

theme = st.text_input("主题")
submit = st.button("开始写作")

if submit and not deepseek_api_key:
    st.info("密钥未输入")
    st.stop()
if submit and not theme:
    st.info("主题未输入")
    st.stop()
if submit:
    with st.spinner("AI正在创作中..."):
        result = xiaohongshu_generator(theme, deepseek_api_key)

    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### 小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### 小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### 小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### 小红书标题5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)