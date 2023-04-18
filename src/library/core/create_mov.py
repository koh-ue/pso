#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: FIXME: XXX: HACK: NOTE: INTENT: USAGE:

import os
import re
import glob
from PIL import Image
import moviepy.editor as mp

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def save_gif(problem_name, duration, loop):
    files = sorted(glob.glob(f'../../../figures/{problem_name}/{problem_name}_process/*.png'), key=natural_keys)
    images = list(map(lambda file : Image.open(file), files))
    images[0].save(f'../../../figures/{problem_name}/{problem_name}.gif', 
                   save_all=True, 
                   append_images=images[1:], 
                   duration=duration, 
                   loop=loop)

def gif2mp4(filename):
    output_filename = os.path.splitext(filename)[0] + '.mp4'
    movie_file = mp.VideoFileClip(filename)
    movie_file.write_videofile(output_filename)
    movie_file.close()