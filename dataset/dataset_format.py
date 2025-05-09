from PIL import Image
import os

# 设置输入和输出文件夹
input_dir = '/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset3/output_images'  # 替换为包含jpeg图片的文件夹路径
output_dir = '/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset3/output_images_jpg'  # 替换为你希望保存jpg图片的文件夹路径

# 创建输出目录，如果不存在的话
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历文件夹中的所有文件
for image_name in os.listdir(input_dir):
    # 只处理 .jpeg 格式的图片
    if image_name.lower().endswith('.jpeg'):
        image_path = os.path.join(input_dir, image_name)

        # 打开图片
        img = Image.open(image_path)

        # 转换为RGB并保存为 .jpg 格式
        new_image_name = image_name.replace('.jpeg', '.jpg')
        new_image_path = os.path.join(output_dir, new_image_name)
        img.convert('RGB').save(new_image_path, 'JPEG')

print("All .jpeg images have been converted to .jpg.")