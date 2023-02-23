import os
import argparse
from tqdm import tqdm
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--image-dir', dest='image_dir', type=str, help='Images directory')
    return parser.parse_args()


def remove_gray_images(image_dir):
    counter = 0
    for im_name in tqdm(os.listdir(image_dir)):
        im_path = os.path.join(image_dir, im_name)
        with Image.open(im_path) as img:
            if img.mode != 'RGB':
                # print(im_path)
                # os.remove(im_path)
                counter += 1
    print(counter)
    

if __name__ == "__main__":
    args = get_args()
    remove_gray_images(args.image_dir)
    # image_dir = "/home/isheffer/data/coco/train2017"
    # remove_gray_images(image_dir)
    