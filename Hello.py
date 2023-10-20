import streamlit as st

# 在标题上方加载图片
st.image('Graph/inspector.webp')  # 确保图片路径是正确的

# 使用Markdown和CSS来居中主标题
st.markdown(
    """
    <h1 style="text-align:center;">Rijkwaterstraat project Group 2</h1>
    """,
    unsafe_allow_html=True
)

# 显示5行副标题，每行是一个人的名字和学号，并使用Markdown和CSS来居中
names_and_ids = [
    ("Heisuke Miyoshi", "5733693"),
    ("Klaas Sicking", "4948416"),
    ("Martijn Stok", "5070740"),
    ("Martin van Andel", "4577566"),
    ("Sun Yixin", "5715210")
]

for name, stud_id in names_and_ids:
    st.markdown(
        f"<h2 style='text-align:center;'>{name} - {stud_id}</h2>",
        unsafe_allow_html=True
    )