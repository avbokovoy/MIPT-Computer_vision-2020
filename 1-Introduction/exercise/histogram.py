import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_histogram( img ):
  return NotImplementedError

def main():
  # Чтение изображение и конвертация в grayscale формат
  

  histogram = compute_histogram(img)
  plt.hist( histogram )
  plt.show()

if __name__ == "__main__":
  main()