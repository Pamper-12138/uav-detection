import os
import shutil

# 路径配置
label_dir = "../dataset/dataset3/labels"  # YOLO 格式的标签文件夹
image_dir = "../dataset/dataset3/images"  # 图片文件夹
output_label_dir = "../dataset/dataset3/output_labels"  # 筛选后的标签存放路径
output_image_dir = "../dataset/dataset3/output_images"  # 筛选后的图片存放路径

# 目标类别（无人机的 class_id，例如 1）
drone_class = 1

# 最大目标面积阈值（小于 20% 才保留）
max_bbox_area = 0.20

# 统计信息
total_images = len(os.listdir(image_dir))  # 总图片数
filtered_images = 0  # 筛选后图片数
original_order = sorted(os.listdir(image_dir))  # 原始顺序
filtered_order = []  # 筛选后的顺序

# 创建目标存储文件夹
os.makedirs(output_label_dir, exist_ok=True)
os.makedirs(output_image_dir, exist_ok=True)

# 遍历所有标签文件（按顺序处理）
for label_file in sorted(os.listdir(label_dir)):
    label_path = os.path.join(label_dir, label_file)
    # 适配图片格式（.jpg 或 .jpeg）
    image_path_jpg = os.path.join(image_dir, label_file.replace(".txt", ".jpg"))
    image_path_jpeg = os.path.join(image_dir, label_file.replace(".txt", ".jpeg"))

    # 检查图片文件是否存在
    if not os.path.exists(image_path_jpg) and not os.path.exists(image_path_jpeg):
        continue

    # 选择存在的图片文件
    image_path = image_path_jpg if os.path.exists(image_path_jpg) else image_path_jpeg

    with open(label_path, "r") as f:
        lines = f.readlines()

    keep = False  # 是否保留该文件
    new_lines = []

    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        bbox_width = float(parts[3])
        bbox_height = float(parts[4])
        bbox_area = bbox_width * bbox_height  # 计算归一化的目标面积

        # 只保留无人机类别，并且面积小于 20%
        if class_id == drone_class and bbox_area < max_bbox_area:
            keep = True
            new_lines.append(line)

    # 只保留符合条件的文件
    if keep:
        shutil.copy(image_path, os.path.join(output_image_dir, os.path.basename(image_path)))
        with open(os.path.join(output_label_dir, label_file), "w") as f:
            f.writelines(new_lines)
        filtered_images += 1
        filtered_order.append(os.path.basename(image_path))

# 打印结果
print(f"\n📊 总图片数: {total_images}")
print(f"✅ 筛选后保留的图片数: {filtered_images}")
print(f"📂 筛选后的图片已存入 {output_image_dir}")

# 检查顺序是否保持不变
if original_order[:filtered_images] == filtered_order:
    print("✅ 处理后文件顺序未改变！")
else:
    print("⚠ 警告：文件顺序可能发生了变化，请检查！")