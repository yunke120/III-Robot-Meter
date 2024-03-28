import os  
from PIL import Image  
  
# 定义函数将彩色图像转换为灰白图像  
def convert_to_grayscale(image_path):  
    image = Image.open(image_path).convert('L')  # 转换为灰白图像  
    image.save(image_path)  # 保存图像  
  
# 定义文件夹路径  
folder_path = "img"  
  
# 遍历文件夹内的所有图像文件并转换为灰白图像  
for filename in os.listdir(folder_path):  
    if filename.endswith(".jpg") or filename.endswith(".png"):  
        image_path = os.path.join(folder_path, filename)  
        convert_to_grayscale(image_path)