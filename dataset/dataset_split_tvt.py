import os
import shutil
import random

# 文件夹路径
base_dir = "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/union_dataset"
image_dir = os.path.join(base_dir, "images")
label_dir = os.path.join(base_dir, "labels")

# 输出划分后的目录
train_image_dir = os.path.join(base_dir, "train/images")
val_image_dir = os.path.join(base_dir, "valid/images")
test_image_dir = os.path.join(base_dir, "test/images")

train_label_dir = os.path.join(base_dir, "train/labels")
val_label_dir = os.path.join(base_dir, "valid/labels")
test_label_dir = os.path.join(base_dir, "test/labels")

# 创建目标目录
for directory in [train_image_dir, val_image_dir, test_image_dir, train_label_dir, val_label_dir, test_label_dir]:
    os.makedirs(directory, exist_ok=True)

# 获取所有图片和标签文件
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
label_files = [f.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt') for f in image_files]

# 确保每个图片文件有对应的标签文件
assert len(image_files) == len(label_files), "图片和标签数量不匹配！"

# 同时打乱图片和标签列表
combined = list(zip(image_files, label_files))
random.shuffle(combined)
image_files, label_files = zip(*combined)

# 划分比例
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# 计算数据集大小
total_count = len(image_files)
train_count = int(total_count * train_ratio)
val_count = int(total_count * val_ratio)
test_count = total_count - train_count - val_count

# 划分数据集
train_images = image_files[:train_count]
train_labels = label_files[:train_count]

val_images = image_files[train_count:train_count + val_count]
val_labels = label_files[train_count:train_count + val_count]

test_images = image_files[train_count + val_count:]
test_labels = label_files[train_count + val_count:]

# 函数：移动文件到指定目录
def move_files(image_list, label_list, image_dir, label_dir, target_image_dir, target_label_dir):
    for img, lbl in zip(image_list, label_list):
        # 移动图片
        shutil.copy(os.path.join(image_dir, img), os.path.join(target_image_dir, img))
        # 移动标签
        shutil.copy(os.path.join(label_dir, lbl), os.path.join(target_label_dir, lbl))

# 移动训练集、验证集、测试集的文件
move_files(train_images, train_labels, image_dir, label_dir, train_image_dir, train_label_dir)
move_files(val_images, val_labels, image_dir, label_dir, val_image_dir, val_label_dir)
move_files(test_images, test_labels, image_dir, label_dir, test_image_dir, test_label_dir)

# 输出划分结果
print(f"训练集大小: {len(train_images)}")
print(f"验证集大小: {len(val_images)}")
print(f"测试集大小: {len(test_images)}")
print("✅ 文件已成功复制到目标目录！")