# 使用支持 Python 3.9 的基础镜像
FROM python:3.9-slim

# 安装 PyTorch 及其他依赖
RUN pip install --upgrade pip && \
    pip install torch==1.9.0 torchvision==0.10.0 torchaudio==0.10.0

# 设置工作目录
WORKDIR /app

# 复制代码和依赖文件到容器中
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置默认命令
CMD ["python", "/app/ultralytics/train_yolo.py"]