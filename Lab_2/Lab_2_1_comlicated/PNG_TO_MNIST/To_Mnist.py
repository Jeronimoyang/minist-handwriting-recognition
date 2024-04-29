import os
import numpy as np
import struct
import cv2

def load_images_and_labels(data_folder):
    """Load images and generate labels from subfolder names."""
    images = []
    labels = []

    label_map = {}  # 用于存储类别名称到数字标签的映射
    label_counter = 0  # 用于生成唯一的数字标签

    for folder_name in sorted(os.listdir(data_folder)):
        label_folder = os.path.join(data_folder, folder_name)
        if os.path.isdir(label_folder):
            if folder_name not in label_map:
                label_map[folder_name] = label_counter
                label_counter += 1
            label = label_map[folder_name]
            for filename in sorted(os.listdir(label_folder)):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    image_path = os.path.join(label_folder, filename)
                    # 加载图像并转换为灰度图
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    image = image.astype(np.uint8)
                    images.append(image)
                    labels.append(label)

    return np.array(images), np.array(labels), label_map

def save_idx3_ubyte(images, output_file):
    """Save images as idx3-ubyte format."""
    with open(output_file, 'wb') as f:
        magic = 2051
        num_images = len(images)
        if num_images > 0:
            rows, cols = images[0].shape
            f.write(struct.pack('>IIII', magic, num_images, rows, cols))
            for image in images:
                f.write(struct.pack('>' + 'B' * (rows * cols), *image.flatten()))
        else:
            print("No images to save.")

def save_idx1_ubyte(labels, output_file):
    """Save labels as idx1-ubyte format."""
    with open(output_file, 'wb') as f:
        magic = 2049
        num_items = len(labels)
        if num_items > 0:
            f.write(struct.pack('>II', magic, num_items))
            f.write(struct.pack('>' + 'B' * num_items, *labels))
        else:
            print("No labels to save.")

if __name__ == "__main__":
    # 数据文件夹路径
    data_folder = "E:/AI_Code/Noise/noise_test/"

    # 加载图像和生成标签
    images, labels, label_map = load_images_and_labels(data_folder)

    # 保存为MNIST数据集格式的文件
    save_idx3_ubyte(images, "E:/AI_Code/To_Mnist/t10k-images-idx3-ubyte")
    save_idx1_ubyte(labels, "E:/AI_Code/To_Mnist/t10k-labels-idx1-ubyte")

    # 保存标签映射
    with open("label_map.txt", 'w') as f:
        for label_name, label_id in label_map.items():
            f.write(f"{label_name}: {label_id}\n")
