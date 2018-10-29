# -*- coding:utf-8 -*-
import imageio


def create_gif(images, opt):
    frames = []
    for image in images:
        frames.append(imageio.imread(image))
    imageio.mimsave(opt, frames, 'GIF', duration=0.02)


def main():
    name = 'Tongzhou'
    fmt = 'png'
    num = 601
    optName = 'Tongzhou.gif'

    images = []
    for i in range(num):
        id = str(i).zfill(4)
        image = name + '.' + id + '.' + fmt
        images.append(image)
    print(images)

    create_gif(images, optName)


if __name__ == '__main__':
    main()
