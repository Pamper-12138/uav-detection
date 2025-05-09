import os
import shutil

# 原始数据集文件夹路径
data_dir = "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/Database1"

# 目标存放路径（存放匹配的图片和标签）
output_image_dir = "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset3/images"
output_label_dir = "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset3/labels"

# 确保目标文件夹存在
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# 获取所有文件（带扩展名）
all_files = os.listdir(data_dir)

# 提取所有图片文件和标注文件的名称（去掉扩展名）
image_files = {os.path.splitext(f)[0] for f in all_files if f.lower().endswith((".jpg", ".jpeg", ".png"))}
label_files = {os.path.splitext(f)[0] for f in all_files if f.lower().endswith(".txt")}

# 找出匹配的文件
matched_files = image_files & label_files  # 取交集，得到同时有图片和标注的文件
missing_labels = image_files - label_files  # 只有图片但无标签的文件

# 处理匹配的文件（移动到目标文件夹）
for file_name in matched_files:
    # 移动图片
    for ext in [".jpg", ".jpeg", ".png"]:
        image_path = os.path.join(data_dir, file_name + ext)
        if os.path.exists(image_path):
            shutil.move(image_path, os.path.join(output_image_dir, os.path.basename(image_path)))

    # 移动标注文件
    label_path = os.path.join(data_dir, file_name + ".txt")
    if os.path.exists(label_path):
        shutil.move(label_path, os.path.join(output_label_dir, os.path.basename(label_path)))

# 删除无对应标签的图片
for file_name in missing_labels:
    for ext in [".jpg", ".jpeg", ".png"]:
        image_path = os.path.join(data_dir, file_name + ext)
        if os.path.exists(image_path):
            os.remove(image_path)  # 删除文件
            print(f"🗑 已删除无标签的图片: {image_path}")

# 输出最终结果
print(f"✅ 处理完成！匹配的图片和标注已移动到 {output_image_dir} 和 {output_label_dir}")
if missing_labels:
    print(f"✅ 已删除 {len(missing_labels)} 张无对应标签的图片")
else:
    print("✅ 所有图片均有对应的标注文件，无需删除")

