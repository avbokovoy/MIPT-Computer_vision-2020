import numpy as np
import cv2

def convert_bgr_2_grayscale( img ):
  return NotImplementedError

def convert_bgr_2_hsv( img ):
  return NotImplementedError

def convert_bgr_2_yuv( img ):
  return NotImplementedError

# Опционально
def convert_bgr_2_cmyk( img ):
  return NotImplementedError

def main():
  #Чтение изображения img
   
  grayImage = convert_bgr_2_grayscale( img )
  hsvImage  = convert_bgr_2_hsv( img )
  yuvImage  = convert_bgr_2_yuv( img )
  cmykImage = convert_bgr_2_cmyk( img )

  grayImage = cv2.cvtColor( grayImage, cv2.COLOR_GRAY2BGR )
  hsvImage  = cv2.cvtColor( hsvImage, cv2.COLOR_HSV2BGR )
  yuvImage  = cv2.cvtColor( yuvImage, cv2.COLOR_YUV2BGR )
  
  cv2.imshow( 'Gray', grayImage )
  cv2.imshow( 'HSV', hsvImage )
  cv2.imshow( 'YUV', yuvImage )
  cv2.imshow( 'CMYK', cmykImage )
  #cv2.imshow()

  cv2.waitKey()

if __name__ == "__main__":
    main()
