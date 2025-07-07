import matplotlib.pyplot as plt
import numpy as np
import os

def create_rgb_scale_visualization():
    # Mengatur backend matplotlib ke 'Agg' untuk environment tanpa display
    plt.switch_backend('Agg')

    # Buat gambar RGB sederhana 8x8 dengan nilai piksel nyata (0–255)
    rgb_image = np.array([
        [[255, 0, 0], [255, 64, 0], [255, 128, 0], [255, 192, 0], [255, 255, 0], [192, 255, 0], [128, 255, 0], [64, 255, 0]],
        [[0, 255, 0], [0, 255, 64], [0, 255, 128], [0, 255, 192], [0, 255, 255], [0, 192, 255], [0, 128, 255], [0, 64, 255]],
        [[0, 0, 255], [64, 0, 255], [128, 0, 255], [192, 0, 255], [255, 0, 255], [255, 0, 192], [255, 0, 128], [255, 0, 64]],
        [[255, 255, 255], [192, 192, 192], [128, 128, 128], [64, 64, 64], [0, 0, 0], [64, 64, 64], [128, 128, 128], [192, 192, 192]],
        [[255, 128, 128], [255, 64, 64], [255, 0, 0], [128, 255, 128], [64, 255, 64], [0, 255, 0], [128, 128, 255], [64, 64, 255]],
        [[0, 0, 255], [0, 64, 255], [0, 128, 255], [0, 192, 255], [0, 255, 255], [0, 255, 192], [0, 255, 128], [0, 255, 64]],
        [[255, 0, 255], [255, 0, 192], [255, 0, 128], [255, 0, 64], [255, 0, 0], [255, 64, 0], [255, 128, 0], [255, 192, 0]],
        [[255, 255, 0], [192, 255, 0], [128, 255, 0], [64, 255, 0], [0, 255, 0], [0, 255, 64], [0, 255, 128], [0, 255, 192]]
    ], dtype=np.uint8)

    # Visualisasi gambar RGB dengan nilai piksel 0–255
    plt.figure(figsize=(6, 6))
    plt.imshow(rgb_image)
    plt.title("Visualisasi Gambar RGB dengan Skala 0–255")
    plt.axis('off')

    # Pastikan direktori output ada
    output_dir = os.path.join('output', 'rgb')
    os.makedirs(output_dir, exist_ok=True)
    
    # Simpan gambar ke file
    output_path = os.path.join(output_dir, 'rgb_scale.png')
    plt.savefig(output_path)
    plt.close()
    
    return output_path

if __name__ == "__main__":
    output_file = create_rgb_scale_visualization()
    print(f"Gambar telah disimpan ke: {output_file}")
