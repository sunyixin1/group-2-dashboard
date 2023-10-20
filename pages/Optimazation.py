import streamlit as st
import os

st.title("Path finding & Range Model")

st.title("Path finding")
# 设置文件夹路径
IMG_DIR = r"Graph"

# 创建start point和goal point的选择列表
start_points = ["start_point1", "start_point2", "start_point3"]
goal_points = ["goal_point1", "goal_point2", "goal_point3"]

# 使用streamlit创建选择框
selected_start = st.selectbox('Choose a start point:', start_points)
selected_goal = st.selectbox('Choose a goal point:', goal_points)

# 根据选择的点获取图片名称
start_index = start_points.index(selected_start) + 1
goal_index = goal_points.index(selected_goal) + 1
img_name = f"path_plot{start_index}{goal_index}.png"

# 构建完整的文件路径
img_path = os.path.join(IMG_DIR, img_name)

# 在Streamlit上显示图像
st.image(img_path, caption=img_name, use_column_width=True)

######################################################################################################################
######################################################################################################################Range
######################################################################################################################
st.title("Range")

def main():
    st.title("选择坐标展示相应图像")

    # 定义坐标和对应的图像文件路径
    coords_to_image = {
        "(119329.13, 483480.692)": "Graph/Range_plot1.png",
        "(117836.772, 426330.494)": "Graph/Range_plot2.png",
        "(199665.357, 355307.629)": "Graph/Range_plot3.png",
        "(33234.539, 392319.29)": "Graph/Range_plot4.png",
        "(199014.108, 497183.81)": "Graph/Range_plot5.png"
    }

    # 为用户提供一个选择框来选择坐标
    selected_coord = st.selectbox("Choose a point：", list(coords_to_image.keys()))

    # 根据选择的坐标展示对应的图像
    st.image(coords_to_image[selected_coord], caption=selected_coord, use_column_width=True)

if __name__ == "__main__":
    main()

 #############################################################
 #############################################################
 #############################################################



# 定义日期和对应的文件名前缀
DATES = {
    '2019-11-21': '1',
    '2019-11-05': '2',
    '2019-10-15': '3',
    '2019-09-23': '4',
    '2019-08-14': '5'
}

# Streamlit应用的主函数
def main():
    st.title('Optimization Result')

    # 用户可以从选择框中选择日期
    selected_date = st.selectbox('Select a date:', list(DATES.keys()))
    
    # 根据所选日期获取文件名前缀
    file_prefix = DATES[selected_date]

    # 默认加载inspector的图
    st.button('Show Inspector')
    if st.button('Show Incident'):
        load_html_map(file_prefix + "2")
    elif st.button('Show Both'):
        load_html_map(file_prefix + "3")
    else:
        load_html_map(file_prefix + "1")

def load_html_map(suffix):
    base_path = "Graph"
    filename = f"map{suffix}.html"
    filepath = os.path.join(base_path, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        html_content = file.read()
        st.components.v1.html(html_content, height=800)


if __name__ == '__main__':
    main()