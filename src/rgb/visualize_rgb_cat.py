import matplotlib.pyplot as plt
import numpy as np
import os

def create_rgb_cat_visualization():
    # Mengatur backend matplotlib ke 'Agg' untuk environment tanpa display
    plt.switch_backend('Agg')

    # Buat contoh sederhana gambar hewan (ikon kucing) dengan array RGB 8x8
    # Warna: Putih (background), Hitam (kontur), Pink (telinga, hidung)
    cat_image = np.array([
        [[255, 255, 255], [0, 0, 0],     [255, 192, 203], [255, 255, 255], [255, 255, 255], [255, 192, 203], [0, 0, 0],     [255, 255, 255]],
        [[0, 0, 0],       [0, 0, 0],     [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0],     [0, 0, 0]],
        [[0, 0, 0],       [255, 255, 255],[0, 0, 0],      [255, 255, 255], [255, 255, 255], [0, 0, 0],       [255, 255, 255],[0, 0, 0]],
        [[0, 0, 0],       [255, 255, 255],[255, 255, 255],[255, 105, 180], [255, 105, 180], [255, 255, 255], [255, 255, 255],[0, 0, 0]],
        [[0, 0, 0],       [255, 255, 255],[0, 0, 0],      [255, 255, 255], [255, 255, 255], [0, 0, 0],       [255, 255, 255],[0, 0, 0]],
        [[0, 0, 0],       [0, 0, 0],     [255, 255, 255], [0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0],     [0, 0, 0]],
        [[255, 255, 255], [0, 0, 0],     [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0],     [255, 255, 255]],
        [[255, 255, 255], [255, 255, 255],[0, 0, 0],      [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255],[255, 255, 255]]
    ], dtype=np.uint8)

    # Visualisasi gambar kucing RGB
    plt.figure(figsize=(6, 6))
    plt.imshow(cat_image)
    plt.title("Contoh Gambar RGB: Ikon Kucing")
    plt.axis('off')

    # Pastikan direktori output ada
    output_dir = os.path.join('output', 'rgb')
    os.makedirs(output_dir, exist_ok=True)
    
    # Simpan gambar ke file
    output_path = os.path.join(output_dir, 'rgb_cat.png')
    plt.savefig(output_path)
    plt.close()
    
    return output_path

if __name__ == "__main__":
    output_file = create_rgb_cat_visualization()
    print(f"Gambar telah disimpan ke: {output_file}")
