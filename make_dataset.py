# dataset maker for https://github.com/Engineering-Course/CIHP_PGN
# author: qzane@live.com

import os,sys,shutil
from PIL import Image
import numpy as np

DATA_TYPE = ['png','PNG','jpg','JPG']
def main():
    USAGE = "python %s /path_to_images name_of_dataset" % sys.argv[0]
    USAGE += "\nPlease put this code to the same path as test_pgn.py"
    if len(sys.argv)!=3 or '--help' in sys.argv or '-h' in sys.argv:
        print(USAGE)
        os._exit(0)
    path_img = sys.argv[1]
    name_dataset = sys.argv[2]
    path_dataset = os.path.join('.', 'datasets', name_dataset)
    if os.path.isdir(path_dataset):
        raise(Exception("the target dataset already exists, please delete that first."))
        #shutil.rmtree(path_dataset)
    os.makedirs(path_dataset)
    path_edge = os.path.join(path_dataset, 'edges')
    path_images = os.path.join(path_dataset, 'images')
    path_list = os.path.join(path_dataset, 'list')
    for p in [path_edge, path_images, path_list]:
        os.makedirs(p)
    files = [i for i in os.listdir(path_img) if i.split('.')[-1] in DATA_TYPE]
    for f in files:
        im = Image.open(os.path.join(path_img, f))
        # im = im.resize((im.size[0]*720//im.size[1],720), Image.LANCZOS) # if you run out of GPU memory
        im1 = Image.new('L', im.size)
        im.save(os.path.join(path_images, f))
        im1.save(os.path.join(path_edge, '.'.join(f.split('.')[:-1])+'.png'))
    with open(os.path.join(path_list, 'val.txt'), 'w') as flist:
        for f in files:
            flist.write('/images/%s /edges/%s\n'%(f,'.'.join(f.split('.')[:-1])+'.png'))
    with open(os.path.join(path_list, 'val_id.txt'), 'w') as flist:
        for f in files:
            flist.write('%s\n'%'.'.join(f.split('.')[:-1]))



if __name__ == '__main__':
    main()
    print("success!!!")