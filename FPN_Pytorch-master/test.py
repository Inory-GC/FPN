import os
# image_set_file = os.path.join(self._data_path, 'ImageSets', 'Main',
#                                       self._image_set + '.txt')
# self._devkit_path + /VOCdevkit2007/VOC2007/ImageSets/Main/val.txt

_data_path = 'data/VOCdevkit2007/VOC2007'
_image_set = 'test'

image_set_file = os.path.join(_data_path, 'ImageSets', 'Main',
                              _image_set + '.txt')

print('image_file:', image_set_file)

if os.path.exists(image_set_file):
    print(True)
else:
    print(False)
    file = open(image_set_file, 'w')
    file.close()