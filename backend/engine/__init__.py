''' instanim engine init '''

import copy
import math
import os
import shutil
import secrets
import hashlib
import sys
import asyncio
import subprocess

import pandas as pd
import numpy as np
import cairo

import utils.utilities as ut


if "INSTANIM_PATH" in os.environ: ENGINE_DIR=os.getenv("INSTANIM_PATH")
else: ENGINE_DIR=os.path.dirname(os.path.realpath(__file__))

''' shortcut functions to get path for '''
# later remove "isClip" to check for formats directly from string...
def getSamplePath(sample, isClip=False):
    if isClip: sub
    else: sub = 'pics/'
    return ENGINE_DIR + r'/samples/'+ sub + sample
def makePreviewPath(name, isClip=False):
    if isClip: sub = 'clips/'
    else: sub = 'pics/'
    return ENGINE_DIR + r'/previews/'+ sub + name
def makeExportPath(name, isClip=False):
    if isClip: sub = 'clips/'
    else: sub = 'pics/'
    return ENGINE_DIR + r'/exports/'+ sub + name 


OPENGL_PATH = ENGINE_DIR + '\\opengl'


rel_tol, abs_tol = 0, 1e-9
FPS = 60 # user can set..




if __name__ == "__main__":

    print(OPENGL_PATH)