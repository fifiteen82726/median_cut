from PIL import Image
import numpy as np

class MC():
  def __init__(self, img):
    self.img = img
    self.rows, self.cols, color = img.shape
    self.img_a = []
    self.mapping = {1: {}, 2: {}, 4: {}, 8: {}}
    self.q_image = {1: np.copy(img), 2: np.copy(img), 4: np.copy(img), 8: np.copy(img)}

    for i in xrange(self.rows):
      for j in xrange(self.cols):
        self.img_a.append(img[i][j])

  def median_cut(self):
    img_array = self.img_a
    # current_cut, target_cut
    self.helper(img_array, 0, 8)
    self.generate_compressive_image()

  # generate 4 compressive image by given bits number and created mapping table
  def generate_compressive_image(self):
    for n in [1,2,4,8]:
      for i in xrange(self.rows):
        for j in xrange(self.cols):
          pixel_v = self.img[i][j]
          self.q_image[n][i][j] = self.mapping[n][tuple(pixel_v)]

      self.save_image(self.q_image[n], n)

  def save_image(self, image, bit_number):
    img = Image.fromarray(image)
    name = 'quantized-image' + str(bit_number) + '.jpg'
    img.save(name)

  # Recursively partition the pixel group and make mapping tables
  def helper(self, image_arr, current_cut, target):
    if current_cut >= target:
      return
    current_cut += 1

    self.sort_by_max_difference_dimension(image_arr)
    lens = len(image_arr)
    left = image_arr[0:lens/2]
    right = image_arr[lens/2:lens]
    if current_cut in [1,2,4,8]:
      self.compute_mean(left, current_cut)
      self.compute_mean(right, current_cut)

    self.helper(left, current_cut, target)
    self.helper(right, current_cut, target)

  # It's a sub function of helper, use it to sort the pixel array by maximun difference value of dimensional value
  def sort_by_max_difference_dimension(self, image_arr):
    diff_a = np.amax(image_arr, axis=0) - np.amin(image_arr, axis=0)
    index = np.argmax(diff_a)
    image_arr.sort(key=lambda x: x[index])

  # It's a sub function of helper, use it to calculate the mean value of its small group
  def compute_mean(self, image_arr, current_cut):
    mean = np.mean(image_arr, axis=0)
    for pixel in image_arr:
      self.mapping[current_cut][tuple(pixel)] = mean

image = np.asarray(Image.open('img/t1.jpg').convert('RGB'))
MC(image).median_cut()