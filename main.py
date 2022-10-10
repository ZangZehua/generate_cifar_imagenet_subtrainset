import os
import shutil
import random


class_number = 100
image_number_each_class = 500
pick_rate = 0.1
data_folder = "/data/data/CIFAR-100/unlabeled"
target_folder = "/data/data/CIFAR-100/train"
if not os.path.exists(target_folder):
    os.mkdir(target_folder)
class_file_list = os.listdir(data_folder)
print(class_file_list)

for c in range(class_number):
    print("-----------------------")
    current_path = os.path.join(data_folder, class_file_list[c])
    target_path = os.path.join(target_folder, class_file_list[c])
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    print(current_path)
    print(target_path)
    image_file_list = os.listdir(current_path)
    selected_image_path = random.sample(range(0, image_number_each_class), int(pick_rate*image_number_each_class))
    for image in selected_image_path:
        image_path = os.path.join(current_path, image_file_list[image])
        target_image_path = os.path.join(target_path, image_file_list[image])
        shutil.copyfile(image_path, target_image_path)


