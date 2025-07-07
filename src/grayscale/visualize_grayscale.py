import matplotlib.pyplot as plt
import numpy as np
import os

def create_grayscale_visualization():
    # Mengatur backend matplotlib ke 'Agg' untuk environment tanpa display
    plt.switch_backend('Agg')

    # Buat gambar grayscale sederhana 8x8 dengan nilai piksel nyata (0–255)
    grayscale_image = np.array([
        [0, 32, 64, 96, 128, 160, 192, 255],
        [0, 32, 64, 96, 128, 160, 192, 255],
        [0, 32, 64, 96, 128, 160, 192, 255],
        [0, 32, 64, 96, 128, 160, 192, 255],
        [0, 32, 64, 96, 128, 160, 192, 255],
        [0, 32, 64, 96, 128, 160, 192, 255],
        [0, 32, 64, 96, 128, 160, 192, 255],
        [0, 32, 64, 96, 128, 160, 192, 255]
    ], dtype=np.uint8)

    # Visualisasi gambar dengan nilai piksel 0–255
    plt.figure(figsize=(6, 6))
    plt.imshow(grayscale_image, cmap='gray', vmin=0, vmax=255)
    plt.colorbar(label="Nilai Piksel (0–255)")
    plt.title("Visualisasi Gambar Grayscale dengan Skala 0–255")
    plt.axis('off')

    # Pastikan direktori output ada
    output_dir = os.path.join('output', 'grayscale')
    os.makedirs(output_dir, exist_ok=True)
    
    # Simpan gambar ke file
    output_path = os.path.join(output_dir, 'grayscale_scale.png')
    plt.savefig(output_path)
    plt.close()
    
    return output_path

if __name__ == "__main__":
    output_file = create_grayscale_visualization()
    print(f"Gambar telah disimpan ke: {output_file}") 