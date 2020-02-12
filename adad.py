def change_prefix(path,train_data_prefix):
    path = path.split("tiny-imagenet-200/train")[1]
    path = path.replace("/", "\\")
    path = "".join([train_data_prefix, path])
    return path
change_pre="/home/tian/\u56fe\u7247/tiny-imagenet-200/train/n02106662/images/n02106662_70.JPEG"
train_data_prefix=r"D:\open-data\tiny-imagenet-200\train"
print(change_prefix(change_pre,train_data_prefix))