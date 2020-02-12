cmake_minimum_required( VERSION 3.0.0 )
project( image_processing )

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable( image_processing image_processing.cpp )

target_link_libraries( image_processing ${OpenCV_LIBS} )