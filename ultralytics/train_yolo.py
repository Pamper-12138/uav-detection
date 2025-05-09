from ultralytics import YOLO
import torch
import tensorflow as tf
import pandas as pd
import os
from pathlib import Path
import cv2



# model = YOLO("yolo_models/yolov8s.pt")  # 使用 YOLOv8n 预训练模型
# model = YOLO("/Users/pamper/Desktop/uavdetection/ultralytics-main/yolo_model/yolo_s_0.003_0.03_100_newdata/weights/last.pt")  # 使用 YOLOv8n 预训练模型
# model = YOLO("yolo_models/yolo_200_lr_0.01/last.pt")  # 使用 YOLOv8n 预训练模型
model = YOLO("/Users/pamper/Desktop/uavdetection/ultralytics-main/yolo_model/yolo_moco_s_0.005_0.03_100_newdata/weights/best.pt")  # 使用 YOLOv8n 预训练模型

# results = model.train(
#     data="./dataset/union_dataset/data.yaml",  # 数据集配置文件
#     epochs=100,  # 训练轮数
#     imgsz=416,  # 图像大小
#     batch=16,  # 更小的 batch size
#     device='mps',  # 使用 Metal Performance Shaders 加速训练 (适用于 Mac)
#     save_period=20,  # 每5个 epoch 保存一次模型
#     save=True,  # 启用自动保存
#     # resume=True,
#     lr0=0.01,
#     lrf=0.005,
# )



# 目标保存目录
# save_dir = "./test/yolo_moco_100_lr_0.005_64*64"
# os.makedirs(save_dir, exist_ok=True)  # 如果目录不存在，创建它



# 进行推理
# results = model("../dataset/final.v3-final-dataset.yolov8/test/images")
# metrics = model.valid(data='./dataset/final.v3-final-dataset.yolov8/data.yaml')  # data.yaml 中包含了数据集的路径和类别定义
# 查看评估结果

# # 遍历每个预测结果并保存到指定目录
# for i, result in enumerate(results):
#     save_path = os.path.join(save_dir, f"prediction_{i}.jpg")  # 拼接保存路径
#     result.save(save_path)  # 保存每个预测图像到指定目录
#
#     print(f"Saved prediction {i} to {save_path}")


# 评估测试集
metrics = model.val(data='./dataset/union_dataset/data.yaml', split='valid')  # 指定测试集


# 打印 F1 和 Recall
print("Recall:", metrics.results_dict["metrics/recall"])
print("F1 Score:", metrics.results_dict["metrics/f1"])


