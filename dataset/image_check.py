from PIL import Image
import os

# 设置文件夹路径
image_dir = "/Users/pamper/Desktop/uavdetection/ultralytics-main/dataset/images"  # 替换为你的图片文件夹路径

# 统计真正是 JPEG 格式的文件
jpeg_count = 0
total_count = 0
non_jpeg_files = []

for file in os.listdir(image_dir):
    file_path = os.path.join(image_dir, file)
    try:
        with Image.open(file_path) as img:
            total_count += 1
            if img.format in ["JPEG", "JPG"]:  # 真实格式是 JPEG
                jpeg_count += 1
            else:
                non_jpeg_files.append(file)  # 记录非 JPEG 文件
    except Exception:
        non_jpeg_files.append(file)  # 无法打开的文件

# 输出统计结果
print(f"📂 目录：{image_dir}")
print(f"✅ 真实 JPEG 格式图片数量: {jpeg_count}")
print(f"📌 总文件数量: {total_count}")
print(f"⚠️ 不是 JPEG 格式的文件数量: {len(non_jpeg_files)}")

if non_jpeg_files:
    print("\n🔍 以下文件**不是** JPEG 格式（可能是伪 JPG 或其他格式）：")
    for f in non_jpeg_files:
        print(f" - {f}")