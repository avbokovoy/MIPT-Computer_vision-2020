#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

int main( int argc, char** argv )
{
  /* Базовый класс для изображений (и не только).
   * https://docs.opencv.org/4.2.0/d3/d63/classcv_1_1Mat.html
   * 
   * Пустой экземпляр класса
   */
  cv::Mat matEmpty;
  std::cout << matEmpty << std::endl;
  /*
   * Пустая матрица размера 2х2
   * cv::Mat::Mat( int rows, int cols, int type )
   * 
   * Список типов:
   * https://docs.opencv.org/4.2.0/d1/d1b/group__core__hal__interface.html#ga2b02a49f1f211e23c1fc11705a1f0ce7
   */
  cv::Mat mat2x2( 2, 2, CV_8UC3 );
  std::cout << mat2x2 << std::endl;
  /*
   * Пустая матрица, инициализированная с помощью класса
   * cv::Size(cols, rows)
   * Обратите внимание на порядок cols, rows
   */ 
  cv::Size matSize( 3, 5 );
  cv::Mat mat5x3( matSize, CV_8UC1 );
  std::cout << mat5x3 << std::endl;
  /*
   * Матрица со значениями по умолчанию
   * ВАЖНО: Формат по умолчанию для трехкомпонентных цветных изображений - BGR, а не RGB
   */
  cv::Mat mat320x320predifined( cv::Size( 320, 320 ), CV_8UC3, cv::Scalar( 0, 255, 0 ) );
  cv::imshow( "Predefined matrix", mat320x320predifined );
  cv::waitKey();
  /*
   * Инициализация известными значениями
   */
  cv::Mat mat2x2predifined = ( cv::Mat_<uint8_t>(2, 2) << 1, 2, 3, 4 );
  std::cout << mat2x2predifined << std::endl;
  /*
   * Копирование определенного столбца или колонки
   */
  cv::Mat rowClone  = mat2x2predifined.row(1).clone();
  cv::Mat rowCopyTo;
  mat2x2predifined.row(1).copyTo( rowCopyTo );

  cv::Mat colClone = mat2x2predifined.col(0).clone();
  
  std::cout << "rowClone:  " << rowClone << std::endl;
  std::cout << "rowCopyTo: " << rowCopyTo << std::endl;
  std::cout << "colClone:  " << colClone << std::endl;
  /*
   * Получить размер изображения
   */
  std::cout << mat320x320predifined.size() << std::endl; 
  int height = mat320x320predifined.size().height;
  int width  = mat320x320predifined.size().width;
  int rows   = mat320x320predifined.rows;
  int cols   = mat320x320predifined.cols;
  std::cout << "Width: " << width << " " << "height: " << height << std::endl;
  std::cout << "Rows:  " << rows << " " << "cols: " << cols << std::endl;
  /*
   * Заполнение матрицы случайными значениями
   */
  cv::Mat matRandom( 640, 480, CV_8UC3 );
  cv::randu( matRandom, cv::Scalar::all(0), cv::Scalar::all(255) );
  cv::imshow( "Random matrix", matRandom );
  cv::waitKey();
  /*
   * Вывод в разных форматах
   */
  std::cout << "Default: " << std::endl << mat2x2predifined << std::endl << std::endl;
  std::cout << "Python:  " << std::endl << cv::format( mat2x2predifined, cv::Formatter::FMT_PYTHON ) << std::endl << std::endl;
  std::cout << "CSV:     " << std::endl << cv::format( mat2x2predifined, cv::Formatter::FMT_CSV ) << std::endl << std::endl;
  std::cout << "MATLAB:  " << std::endl << cv::format( mat2x2predifined, cv::Formatter::FMT_MATLAB ) << std::endl << std::endl;
  std::cout << "NumPy:   " << std::endl << cv::format( mat2x2predifined, cv::Formatter::FMT_NUMPY ) << std::endl << std::endl;
  std::cout << "C:       " << std::endl << cv::format( mat2x2predifined, cv::Formatter::FMT_C ) << std::endl << std::endl;
  /*
   * Получить доступ к элементу i, j
   * https://docs.opencv.org/4.2.0/d3/d63/classcv_1_1Mat.html#a330d9adb78976b6efd4116c940924294
   */
  std::cout << matRandom.at<cv::Vec3b>(320, 240) << std::endl;
  matRandom.at<cv::Vec3b>(320, 240) = cv::Vec3b( 0, 255, 128 );
  std::cout << matRandom.at<cv::Vec3b>(320, 240) << std::endl;
  /*
   * Запись изображения в файл
   */
  cv::imwrite( "img/my_image.jpg", matRandom );
  /*
   * Чтение из файла
   */
  cv::Mat colorImage = cv::imread( "img/my_image.jpg" );
  cv::imshow( "Image from file", colorImage );
  cv::waitKey();
  /*
   * "Пробег" по всем элементам массива
   */
  for( int i = 0; i < colorImage.rows; ++i )
  {
    for( int j = 0; j < colorImage.cols; ++j )
    {
      std::cout << colorImage.at<cv::Vec3b>( i, j ) << std::endl;
    }
  }
  //С помощью итератора
  for( auto it = colorImage.begin<cv::Vec3b>(); it != colorImage.end<cv::Vec3b>(); ++it )
  {
    std::cout << *it << std::endl;
  }

  return 0;
}