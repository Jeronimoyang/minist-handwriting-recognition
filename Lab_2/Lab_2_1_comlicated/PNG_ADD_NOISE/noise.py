import os
import cv2
import numpy as np

def add_gaussian_noise(image, mean=50, sigma=100):
    """Add Gaussian noise to an image."""
    h, w, c = image.shape
    noise = np.random.normal(mean, sigma, (h, w, c))
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image

if __name__ == "__main__":
    # 输入和输出目录
    input_dir = "E:/AI_Code/Data/mnist_test/9/"
    output_dir = "E:/AI_Code/Noise/noise_test/9/"

    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 处理所有图片
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 读取图片
            image = cv2.imread(os.path.join(input_dir, filename))

            # 添加高斯噪声
            noisy_image = add_gaussian_noise(image)

            # 保存处理后的图片
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, noisy_image)
