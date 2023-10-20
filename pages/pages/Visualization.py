import streamlit as st
import os

st.title("Initial Data Visualization")

# Streamlit 应用开始
st.title("Heat map")

# 使用 Streamlit 创建交互式选择框
incident_dropdown = st.selectbox(
    "Please choose the type of incident：",
    ['all', 'vehicle_obstruction', 'accident', 'general_obstruction']
)

# 构建图片文件路径
image_path = f"Graph/{incident_dropdown}.png"

# 如果图片存在，则展示图片
if os.path.exists(image_path):
    st.image(image_path, caption=f"{incident_dropdown} 热力图", use_column_width=True)
else:
    st.warning(f"{incident_dropdown} not exist。")

###########################
###########################
###########################

st.title("Bar Chart Analysis")

# Define widgets for Streamlit below the heatmap
incident_type_st = st.selectbox("Incident Type:", ["all", "vehicle_obstruction", "accident", "general_obstruction"], index=1)
weekday_st = st.slider("Weekday:", 0, 4, 0)

# Generate the filename based on user input
filename = f"Graph/{incident_type_st}_{list('Mon Tue Wed Thu Fri')[weekday_st]}.png"

# Check if the file exists
if os.path.exists(filename):
    # Display the saved image using Streamlit
    st.image(filename, use_column_width=True)
else:
    st.write("Image not found. Please select different options or generate the image.")

##############################################
##############################################
##############################################Bubble map

# 加载并展示 folium_map.html
st.title("NAME NAME NAME")
with open("Graph/folium_map.html", "r", encoding="utf-8") as f:
    folium_map_html = f.read()
    st.components.v1.html(folium_map_html, height=800)

# 加载并展示 scatter_map.html
st.title("NAME NAME NAME1")
with open("Graph/scatter_map.html", "r", encoding="utf-8") as f:
    scatter_map_html = f.read()
    st.components.v1.html(scatter_map_html, height=800)