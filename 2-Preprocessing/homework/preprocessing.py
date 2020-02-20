import cv2

def count_disparity( img, res ):
  #img - res
  return NotImplementedError

def count_premitive_metric():
  #sum(count_disparity(img, res))
  return NotImplementedError

def my_homework(img):
  # Return value is image
  return NotImplementedError

def main():
  #Open the image
  
  res = my_homework( img )
  cv2.imshow( 'Result', res )
  
  #Use pre-defined method
  opencv_method_result = '''...'''


  disparity = count_disparity( img, opencv_method_result )
  metric = count_premitive_metric( disparity )
  print( metric )
  cv2.imshow( 'Disparity', disparity )
  cv2.waitKey()

if __name__ == "__main__":
    main()