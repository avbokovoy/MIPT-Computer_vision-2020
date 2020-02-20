import cv2
import numpy as np

def main():
  vcap = cv2.VideoCapture(0)
    
  while(1):
    ret, img = vcap.read()
    img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    cv2.imshow( 'Original image', img )

    #Спектр изображения
    freq = np.fft.fft2( img )
    fshift = np.fft.fftshift( freq )
    magnitude_spectrum = 20 * np.log( np.abs(fshift) )
    magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
    cv2.imshow( 'Frequancy', magnitude_spectrum )

    #Гистограммное выравнивание
    hist_eq_img = cv2.equalizeHist( img )
    cv2.imshow( 'Equalized image', hist_eq_img )

    #Свертка
    kernel = np.ones( (3,3) ) / 9
    filtered = cv2.filter2D( img, -1, kernel )
    cv2.imshow( 'Filtered', filtered )

    #Медианный фильтр
    med = cv2.medianBlur( img, 3 )
    cv2.imshow( 'Median', med )

    #Фильтр Гауса
    gauss = cv2.GaussianBlur( img, (3,3), 0 ) 
    cv2.imshow( 'Gauss', gauss ) 

    #Билатеральный фильтр
    bil = cv2.bilateralFilter( img, 9, 75, 75 )
    cv2.imshow( 'Bilateral', bil )


    cv2.waitKey(2)


if __name__ == "__main__":
    main()