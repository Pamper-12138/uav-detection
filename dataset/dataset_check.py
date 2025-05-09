import os

# 文件夹路径
label_dir = "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/union_dataset/train/labels"
image_dir = "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/union_dataset/train/images"

# 获取所有 txt 文件
txt_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]
total_txt_count = len(txt_files)  # 总标注文件数

# 记录没有对应图片的标注文件
missing_image_files = []

# 统计图片数量
total_image_count = 0

# 遍历检查标注文件是否有对应的图片
for txt_file in txt_files:
    txt_path = os.path.join(label_dir, txt_file)
    base_name = txt_file.replace(".txt", "")

    # 获取对应的图像文件路径（假设图像文件扩展名为 .jpg, .jpeg, .png）
    image_path_jpg = os.path.join(image_dir, base_name + ".jpg")
    image_path_jpeg = os.path.join(image_dir, base_name + ".jpeg")
    image_path_png = os.path.join(image_dir, base_name + ".png")

    # 如果没有找到对应的图片文件，记录该标注文件
    if not (os.path.exists(image_path_jpg) or os.path.exists(image_path_jpeg) or os.path.exists(image_path_png)):
        missing_image_files.append(txt_file)
    else:
        # 如果图片存在，统计总数
        total_image_count += 1

# 输出未找到对应图像文件的标注文件列表
if missing_image_files:
    print("\n⚠️ 以下标注文件没有找到对应的图像文件：")
    for missing_file in missing_image_files:
        print(f" - {missing_file}")
else:
    print("\n✅ 所有标注文件都对应了图像文件！")

# 输出图片总数
print(f"\n📊 总共有 {total_image_count} 张图片对应标注文件。")
print("✅ 文件检查完成！")