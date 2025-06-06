---
comments: true
description: Learn how to set up and run YOLOv5 on AzureML. Follow this quickstart guide for easy configuration and model training on an AzureML compute instance.
keywords: YOLOv5, AzureML, machine learning, compute instance, quickstart, model training, virtual environment, Python, AI, deep learning
---

# YOLOv5 🚀 on AzureML

This guide provides a quickstart to use YOLOv5 from an AzureML compute instance.

Note that this guide is a quickstart for quick trials. If you want to unlock the full power AzureML, you can find the documentation to:

- [Create a data asset](https://learn.microsoft.com/azure/machine-learning/how-to-create-data-assets)
- [Create an AzureML job](https://learn.microsoft.com/azure/machine-learning/how-to-train-model)
- [Register a model](https://learn.microsoft.com/azure/machine-learning/how-to-manage-models)

## Prerequisites

You need an [AzureML workspace](https://learn.microsoft.com/azure/machine-learning/concept-workspace?view=azureml-api-2).

## Create a compute instance

From your AzureML workspace, select Compute > Compute instances > New, select the instance with the resources you need.

<img width="1741" alt="create-compute-arrow" src="https://github.com/ultralytics/docs/releases/download/0/create-compute-arrow.avif">

## Open a Terminal

Now from the Notebooks view, open a Terminal and select your compute.

![open-terminal-arrow](https://github.com/ultralytics/docs/releases/download/0/open-terminal-arrow.avif)

## Setup and run YOLOv5

Now you can, create a virtual environment:

```bash
conda create --name yolov5env -y
conda activate yolov5env
conda install pip -y
```

Clone YOLOv5 repository with its submodules:

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
git submodule update --init --recursive # Note that you might have a message asking you to add your folder as a safe.directory just copy the recommended command
```

Install the required dependencies:

```bash
pip install -r yolov5/requirements.txt
pip install onnx>=1.10.0
```

Train the YOLOv5 model:

```bash
python train.py
```

Validate the model for [Precision](https://www.ultralytics.com/glossary/precision), [Recall](https://www.ultralytics.com/glossary/recall), and mAP

```bash
python valid.py --weights yolov5s.pt
```

Run inference on images and videos:

```bash
python detect.py --weights yolov5s.pt --source path/to/images
```

Export models to other formats:

```bash
python detect.py --weights yolov5s.pt --source path/to/images
```

## Notes on using a notebook

Note that if you want to run these commands from a Notebook, you need to [create a new Kernel](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-access-terminal?view=azureml-api-2#add-new-kernels) and select your new Kernel on the top of your Notebook.

If you create Python cells it will automatically use your custom environment, but if you add bash cells, you will need to run `source activate <your-env>` on each of these cells to make sure it uses your custom environment.

For example:

```bash
%%bash
source activate newenv
python valid.py --weights yolov5s.pt
```
