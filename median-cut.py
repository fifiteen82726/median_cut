from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

class MC():
  def __init__(self, img):
    self.img = img
    self.rows, self.cols, color = img.shape
    self.img_a = []
    self.depth = 0
    self.mapping = {1: }
    self.q_image = {1: }

    for i in xrange(self.rows):
      for j in xrange(self.cols):
        self.img_a.append(img[i][j])

  def median_cut(self, img_array, bits):
    img_array = self.img_a
    np.amax(img_array, axis=0) - np.amin(img_array, axis=0)

  def helper(self, current_cut, target):
    if current_cut >= target
      return

    self.sort_by_max_difference_dimension(self, image_arr)


  def sort_by_max_difference_dimension(self, image_arr):
    diff_a = np.amax(img_array, axis=0) - np.amin(img_array, axis=0)
    index = np.argmax(diff_a)
    sort(image_arr, key=lambda x:x[index])


image = np.asarray(Image.open('img/t1.jpg').convert('RGB'))
bits = [1,2,4,8]
MC(image).median_cut([1])




data = np.zeros((2, 2, 3), dtype=np.uint8)




