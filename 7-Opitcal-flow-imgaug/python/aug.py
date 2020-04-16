import cv2
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np

img = cv2.imread( 'BRACHYLAGUS_IDAHOENSIS.jpg' )
cv2.imshow('Image', img)
cv2.waitKey()

img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
ia.imshow(img)

ia.seed(4)
rotate = iaa.Affine(rotate=(-25, 25))
img_augmented = rotate( image = img )
ia.imshow(img_augmented)


images = [img, img, img, img]
images_aug = rotate(images=images)
ia.imshow( np.hstack(images_aug) )


seq = iaa.Sequential([
    iaa.Affine(rotate=(-25, 25)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2))
])
images_aug = seq(images=images)
ia.imshow(np.hstack(images_aug))

seq = iaa.Sequential([
    iaa.Affine(rotate=(-25, 25)),
    iaa.AdditiveGaussianNoise(scale=(30, 90)),
    iaa.Crop(percent=(0, 0.4))
], random_order=True)
images_aug = seq(images=images)
ia.imshow(np.hstack(images_aug))



seq = iaa.Sequential([
    iaa.CropAndPad(percent=(-0.2, 0.2), pad_mode="edge"),  
    iaa.AddToHueAndSaturation((-60, 60)),  
    iaa.ElasticTransformation(alpha=90, sigma=9),  
    iaa.Cutout()  
], random_order=True)
images_aug = seq(images=images)
ia.imshow(np.hstack(images_aug))