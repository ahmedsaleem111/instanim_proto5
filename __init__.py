''' instanim package init '''

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from flask import Flask, render_template
import flask_cors as CORS

import copy
import math
import os
import shutil
import secrets
import hashlib
import sys
import asyncio

from copy import deepcopy

import cairocffi as cairo

from PIL import Image

import pandas as pd
import numpy as np
# import cairo

import utils.utilities as ut


if "INSTANIM_PATH" in os.environ: instanim_dir=os.getenv("INSTANIM_PATH")
else: instanim_dir=os.path.dirname(os.path.realpath(__file__))

''' shortcut functions to get path for '''
# later remove "isClip" to check for formats directly from string...
def getSamplePath(sample, isClip=False):
    if isClip: sub
    else: sub = 'pics/'
    return instanim_dir + r'/samples/'+ sub + sample
def makePreviewPath(name, isClip=False):
    if isClip: sub = 'clips/'
    else: sub = 'pics/'
    return instanim_dir + r'/previews/'+ sub + name
def makeExportPath(name, isClip=False):
    if isClip: sub = 'clips/'
    else: sub = 'pics/'
    return instanim_dir + r'/exports/'+ sub + name 





rel_tol, abs_tol = 0, 1e-9


''' Instanim Exception Heirarchy '''
# Universal (to all)
class NotParameter(Exception): pass
class LockedParameter(Exception): pass
class NotTag(Exception): pass
class NotUnique(Exception): pass
class DuplicateInputs(Exception): pass
class LenError(ValueError): pass
class BoundsError(ValueError): pass
class SizeError(ValueError): pass
class HasContainer(Exception): pass
class HasItem(Exception): pass


# render.py module
class RenderException(Exception): pass

# entities.py module

# --> for class entity
class EntityException(Exception): pass
class EntityNotUnique(NotUnique): pass
class EntityDuplicateStartsInputs(EntityException): pass
class EntityStartLinkNotUnique(NotUnique): pass
class EntityStopLinkNotUnique(NotUnique): pass

# --> for class link
class LinkException(Exception): pass
class LinkNotUnique(NotUnique): pass
class LinkDuplicateStartEntities(LinkException): pass
class LinkDuplicateStartInputs(LinkException): pass
class LinkDuplicateStopEntities(LinkException): pass
class LinkDuplicateStopOutputs(LinkException): pass
class LinkFaultyInputsDesign(LinkException): pass
class LinkFaultyOutputsDesign(LinkException): pass

# --> for class fabric
class FabricException(Exception): pass
class FabricNotUnique(NotUnique): pass


# surface.py module

# --> for class surface
class SurfaceException(Exception): pass
class SurfaceNotUnique(NotUnique): pass


# dynamics.py module

# --> for rateform
class RateformException(Exception): pass
class InvalidInverseCurve(RateformException): pass

# --> for class Dynamic
class UnboundEventChange(Exception): pass

# --> for class TransitionMatrix
class TransitionException(Exception): pass
class TransitionMergeError(TransitionException): pass
class TransitionApplyError(TransitionException): pass
class TransitionFaultyDesign(TransitionException): pass

# --> for Class Action
class ActionException(Exception): pass

# --> for Class Sweep
class SweepException(Exception): pass

# --> for class Animation
class AnimationNotUnique(NotUnique): pass
class AnimationException(Exception): pass
class AnimationDecompositionError(AnimationException): pass

# --> for class Scene
class SceneException(Exception): pass
class SceneNotUnique(NotUnique): pass


''' Universal Keys/Hashes for method/call accessibility restrictions '''

# Hash/key related Exception subclasses
class AccessDenied(Exception): pass
class AccessLimited(Exception): pass

# tree static_contain_item
treeStaticContainItemKey = ut.randomString(100)
treeStaticContainItemHash = ut.sha256_encode(treeStaticContainItemKey)
# entity add start/stop links methods
entityAddStartLinkKey = ut.randomString(100)
entityAddStartLinkHash = ut.sha256_encode(entityAddStartLinkKey)
entityAddStopLinkKey = ut.randomString(100)
entityAddStopLinkHash = ut.sha256_encode(entityAddStopLinkKey) 
entityCheckDuplicateStartsInputsKey = ut.randomString(100)
entityCheckDuplicateStartsInputsHash = ut.sha256_encode(entityCheckDuplicateStartsInputsKey)
# # binding __init__
# bindingKey = ut.randomString(100)
# bindingHash = ut.sha256_encode(bindingKey)
# entity lock pars 
entityLockParsKey = ut.randomString(100)
entityLockParsHash = ut.sha256_encode(entityLockParsKey)
# entity unlock pars 
entityUnlockParsKey = ut.randomString(100)
entityUnlockParsHash = ut.sha256_encode(entityUnlockParsKey)
# fabric __init__
fabricKey = ut.randomString(100)
fabricHash = ut.sha256_encode(fabricKey)
# fabric set direct forms
setFormsKey = ut.randomString(100)
setFormsHash = ut.sha256_encode(setFormsKey)
setFormsOverrideKey = ut.randomString(100)
setFormsOverrideHash = ut.sha256_encode(setFormsOverrideKey)
# fabric add-remove-links
fabricAddRemoveKey = ut.randomString(100)
fabricAddRemoveHash = ut.sha256_encode(fabricAddRemoveKey)
# __init__ of all 2D constructs in render.py (frame2D, branch2D, all primitive2D, etc..)
render2DKey = ut.randomString(100)
render2DHash = ut.sha256_encode(render2DKey)
# surface __init__
surfaceKey = ut.randomString(100)
surfaceHash = ut.sha256_encode(surfaceKey)
# entity2D __init__
entity2DKey = ut.randomString(100)
entity2DHash = ut.sha256_encode(entity2DKey)
# window2D "set_links"
window2DsetLinksKey = ut.randomString(100)
window2DsetLinksHash = ut.sha256_encode(window2DsetLinksKey)
# window2D "copy_forms"
window2DCopyFormsKey = ut.randomString(100)
window2DCopyFormsHash = ut.sha256_encode(window2DCopyFormsKey)
# shape2D "external_contain"
shape2DexternalContainKey = ut.randomString(100)
shape2DexternalContainHash = ut.sha256_encode(shape2DexternalContainKey)
# scaleRule generate
scaleStepRuleKey = ut.randomString(100)
scaleStepRuleHash = ut.sha256_encode(scaleStepRuleKey)
# State __init__
StateKey = ut.randomString(100)
StateHash = ut.sha256_encode(StateKey)
# metaLink __init__
metaLinkKey = ut.randomString(100)
metaLinkHash = ut.sha256_encode(metaLinkKey)
# Dynamic __init__
DynamicKey = ut.randomString(100)
DynamicHash = ut.sha256_encode(DynamicKey)
# Sweeps access
sweepsKey = ut.randomString(100)
sweepsHash = ut.sha256_encode(sweepsKey)
# Transitions access
transitionsKey = ut.randomString(100)
transitionsHash = ut.sha256_encode(transitionsKey)
# Animation Decompose
AnimationDecomposeKey = ut.randomString(100)
AnimationDecomposeHash = ut.sha256_encode(AnimationDecomposeKey)
# Scene __init__
SceneKey = ut.randomString(100)
SceneHash = ut.sha256_encode(SceneKey)

''' 
    Universal Keys/Hashes for debugging 
    (generally for complex methods/constructs with many local variables) 
'''

# Transition Matrix "Apply" method
TransitionApplyDebugKey = ut.randomString(100)
TransitionApplyDebugHash = ut.sha256_encode(TransitionApplyDebugKey)


'''
Universal Structures
'''

structs = {
    'color': 'size-3 list, tuple, or NumPy array with values within [0, 1] OR valid keys from "colors" dictionary in "displays" module.', # what about gradients? more on this...
    'alpha': 'real number within [0, 1]'  # what about gradients? more on this...
}


def describe_structure(struct_key):
    return f'All "{struct_key}" structures must be {structs[struct_key]}.'



'''
Run parameters
'''

renderMode = '2D' # other option 2D/3D also



'''
Globals
'''
BUFFER = None





if __name__ == "__main__":

    print(instanim_dir)