import os
import shutil

# 定义源数据集文件夹路径
dataset_dirs = {
    "dataset1": {
        "images": "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset1/images",
        "labels": "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset1/labels"
    },
    "dataset2": {
        "images": "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset2/output_images",
        "labels": "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset2/output_labels"
    },
    "dataset3": {
        "images": "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset3/output_images",
        "labels": "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/dataset3/output_labels"
    }
}

# 定义目标目录路径
combined_images_dir = "images"
combined_labels_dir = "labels"

# 创建目标文件夹（如果不存在）
os.makedirs(combined_images_dir, exist_ok=True)
os.makedirs(combined_labels_dir, exist_ok=True)

# 遍历每个数据集，合并图片和标签
for dataset_name, paths in dataset_dirs.items():
    image_dir = paths["images"]
    label_dir = paths["labels"]

    # 获取当前数据集的所有图片和标签文件
    image_files = [f for f in os.listdir(image_dir) if f.endswith((".jpg", ".jpeg", ".png"))]
    label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]

    # 处理图像文件
    for image_file in image_files:
        # 生成新文件名，加入数据集标识
        new_image_name = f"{dataset_name}_{image_file}"
        src_image_path = os.path.join(image_dir, image_file)
        dst_image_path = os.path.join(combined_images_dir, new_image_name)

        # 复制图片到新目录
        shutil.copy(src_image_path, dst_image_path)
        print(f"📷 复制图像文件: {new_image_name}")

    # 处理标签文件
    for label_file in label_files:
        # 生成新文件名，加入数据集标识
        new_label_name = f"{dataset_name}_{label_file}"
        src_label_path = os.path.join(label_dir, label_file)
        dst_label_path = os.path.join(combined_labels_dir, new_label_name)

        # 复制标签到新目录
        shutil.copy(src_label_path, dst_label_path)
        print(f"📝 复制标签文件: {new_label_name}")

print("✅ 数据集合并完成！")