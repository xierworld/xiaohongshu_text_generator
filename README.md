测试版本为python-3.10
# 简介
<br>该项目实现了一个小红书爆款文案生成系统</br>
<br>代码关键在于通过Pydantic模型约束输出结构，并且导入langchain.output_parsers模块下的PydanticOutputParser再加上对系统消息的提示词，强制校验JSON格式</br>
<br>构建了一个基于提示词、模型、输出解析器的chain</br>
<br>prompt的设置也是必不可少的</br>

# 启动应用
可以在main.py文件的终端下输入streamlit run main.py，也可以在[share](https://share.streamlit.io/)上部署应用
