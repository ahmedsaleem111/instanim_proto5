from backend.engine.render import *

# interpretation of frames such that for say a given fps, there are "fps" many
# frames distributed event in that interval


'''

For each entity, must have:
- Total frames it covers
- start frame index (relative to scene)
- keyFrames to hold key frames (dictionary of pars, values are a dictionary, key: frame-number, value: value & method)
   (0-key has no method, all other keys' have methods that are SMOOTH by default; if other key methods are NONE, previous time interpolation assumes previous keyframe value)
- setStartKeyFrame function to set pars at start frame in keyFrames (called automatically at input in every subclass, NOT in entity base class)
- addKeyFrames method to add key frames (frame specified relative to start)
- __iter__ to return self with buffer (matrix) with pars initialized to start values
- __next__ to return buffer (matrix) with pars updated for incremented frame (throw StopIteration if frame excedes frames count)
- __getitem__ to return buffer (matrix)  with pars updated select frame (more on this... seems inefficient as it will go throw iterator process by scratch...)
- name to represent identity of entity
- __call__ method to reset entity with new inputs (hence start key frame)
- all child entities have a default pars dictionary (class attribute)
'''

# debating whether to set attributes also... or just return as pars?? doing BOTH for now...


# methods
class keyFrameMethods:
    NONE = lambda val1, val2, frame1, frame2, frame: val2 if frame == frame2 else val1
    LINEAR = lambda val1, val2, frame1, frame2, frame:  val1 + (val2 - val1)*((frame - frame1)/(frame2 - frame1))
    # should work on scalar AND all arrays... as long as dimensions match (verify later)
    SMOOTH = 2 # more on this...



def setStartKeyFrame(ent, keyFrames, keyFramesFrames, keyFramesCount, **pars):
    for par, default in ent.pars.items():
        if par in pars.keys(): keyFrames[par] = {'0': pars[par]}
        else: keyFrames[par] = {'0': default} 
        keyFramesFrames[par] = {'0': 0}
        keyFramesCount[par] = 1
        setattr(ent, par, keyFrames[par]['0'])



class entity:

    def __init__(self, name, startFrame=0, frames=1):
        self.name = name
        self.startFrame = startFrame
        self.frames = frames
        self.keyFrames = {} # frames, values, methods
        self.keyFramesFrames = {} # frames only
        self.keyFramesCount = {} # current count of keyFrames

    def reset(self):
        for par in self.pars: setattr(self, par, self.keyFrames[par]['0']) # resetting to initial values                 


    def addKeyFrames(self, *keyFrames):
        for keyFrame in keyFrames:
            if not isinstance(keyFrame, list): raise TypeError('Please package each "keyFrame" data into a list')
            self.addKeyFrame(*keyFrame)

    # duplicate frame number overwritten
    def addKeyFrame(self, par, val, frame, method = keyFrameMethods.SMOOTH):
        if not (frame >= 0 and frame < self.frames): raise ValueError('frame out of bound')
        if frame == 0: quantity = val # first frame has just value
        else: quantity = [val, method] # all subsequent frames will include method also

        strFrame = str(frame)
        
        if not strFrame in self.keyFrames[par]: # only set and increment if frame wasn't previously keyed
            self.keyFramesFrames[par][str(self.keyFramesCount[par])] = frame
            self.keyFramesCount[par] += 1

        self.keyFrames[par][strFrame] = quantity


    def __iter__(self):
        self.frame = 0
        self.buffer = {} # to tell WHICH keyFrame (by its ordered index) was last covered
        self.notBuffered = {} # to hold pars that only have single keyFrame (won't be buffered)
        return self


    def __next__(self):
        print(f"frame: {self.startFrame + self.frame}, buffer: {self.buffer}")

        if self.frame == self.frames: 
            self.reset() 
            raise StopIteration
        
        pars = {}

        if self.frame == 0:
            for par, parKeyFrames in self.keyFrames.items():
                quantity = parKeyFrames['0']
                pars[par] = quantity
                setattr(self, par, quantity) 

                if len(parKeyFrames) > 1: self.buffer[par] = 0 
                # only setting to buffer if there's more than one key-frame for a par                
                # if setting, buffer will start at the first keyFrame
                else: self.notBuffered[par] = parKeyFrames['0'] # these pars will not be buffered

            self.bufferPars = list(self.buffer.keys()) 
            # to iterate through buffers' pars and not through buffer directly since buffer will likely update

        else:
            strFrame = str(self.frame) # will be referenced a lot...

            for par in self.bufferPars:
                parKeyFrames = self.keyFrames[par]
                strBuffer = str(self.buffer[par]) # also referenced a lot, for each par...
                # essentially buffer index for previous key-frame as a string

                if strFrame in parKeyFrames.keys(): # at key-frame
                    print('key-frame hit')
                    self.buffer[par] += 1 # moving buffer to that next keyFrame ordered index ^
                    
                    quantity = parKeyFrames[strFrame][0] # value will be value at that key frame        

                else: # in between key-frames OR after a key-frame (if no next key-frame)
                    parKeyFramesFrames = self.keyFramesFrames[par]
                    previousKeyFrame = parKeyFramesFrames[strBuffer] # previous key-frame number
                    
                    try: previousKeyFrameValue = parKeyFrames[str(previousKeyFrame)][0] # previous value; 0th is value, 1st is method (not needed)
                    except TypeError: previousKeyFrameValue = parKeyFrames[str(previousKeyFrame)]

                    try:
                        nextKeyFrame = parKeyFramesFrames[str(self.buffer[par] + 1)] # next key-frame number
                        [nextKeyFrameValue, method] = parKeyFrames[str(nextKeyFrame)]

                        quantity = method(previousKeyFrameValue, nextKeyFrameValue, previousKeyFrame, nextKeyFrame, self.frame) # interpolated via method

                    except KeyError: # there was no next key-frame...
                        # setting value to previous key-frame value
                        quantity = previousKeyFrameValue

                pars[par] = quantity
                setattr(self, par, quantity)

            for par, quantity in self.notBuffered.items(): 
                pars[par] = quantity
                setattr(self, par, quantity)
                
        self.frame += 1
        return pars





# def setBuffer(buffer, par, parKeyFrames):
#     buffer[par] =



# assuming insertion at center
class box(entity):

    pars = {
        'x':0,
        'y':1,
        'width':10,
        'height':10,
        'border':True,
        'borderColor': 'white',
        'borderAlpha': 1,
        'borderWidth': 1,
        'fill': False,
        'fillColor': 'coral',
        'fillAlpha': 1
    }

    def __init__(self, name, startFrame=0, frames=1, **pars):
        super().__init__(name, startFrame=startFrame, frames=frames)
        setStartKeyFrame(self, self.keyFrames, self.keyFramesFrames, self.keyFramesCount, **pars)
        # will also initialize attributes "pars" to start/default values


    def draw(self, context): # cairo context
        assert isinstance(context, cairo.Context)

        bx, by = self.x - self.width/2, self.y - self.height/2

        # Drawing Fill
        if self.fill is True:
            context.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)

            context.set_source_rgba(*dsp.colorAsNumPy(self.fillColor), self.fillAlpha)

            context.rectangle(self.x, self.y, self.width, self.height)

            context.close_path()

            context.fill()

        # Drawing Border
        context.set_source_rgba(*dsp.colorAsNumPy(self.borderColor), self.borderAlpha)
        context.set_line_width(self.borderWidth)

        context.rectangle(self.x, self.y, self.width, self.height)

        context.close_path()
        context.stroke()




# class wheelBox(entity):

#     pars = {
#         'x':0,
#         'y':1,
#         'width':10,
#         'height':10,
#         'borderColor': 'white',
#         'borderAlpha': 1,
#         'borderWidth': 1,
#         'wheelStart': 0, # 0 degrees
#         'wheelCoverage': 1, # complete coverage
#     }

#     def __init__(self, tag, **pars):
#         super().__init__(tag)
#         startKeyFrame(self, **pars)






# # assuming insertion at center?
# class text(entity):
#     pars = {
#         'x':0,
#         'y':1,
#         'scale': [1, 1],
#         'fillColor': 'coral',
#         'fillAlpha': 1,
#         'lineColor': 'white',
#         'fillAlpha': 1,
#     }

#     def __init__(self,
#         tag,
#         LaTeX_string = r'Hello World!',
#         mainFont = r'Consolas',
#         mathFont = r'Cambria',
#         **pars
#     ):
#         super().__init__(tag)
#         startKeyFrame(self, **pars)
#         self.LaTeX_string = LaTeX_string
#         self.mainFont = mainFont
#         self.mathFont = mathFont


#         WIDTH = 3
#         HEIGHT = 2
#         PIXEL_SCALE = 200

#         surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
#                                     WIDTH*PIXEL_SCALE,
#                                     HEIGHT*PIXEL_SCALE)
#         ctx = cairo.Context(surface)
#         ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

#         ctx.rectangle(0, 0, WIDTH, HEIGHT)
#         ctx.set_source_rgb(0.8, 0.8, 1)
#         ctx.fill()

#         # Drawing code
#         ctx.set_source_rgb(1, 0, 0)
#         ctx.set_font_size(0.25)
#         ctx.select_font_face("Arial",
#                             cairo.FONT_SLANT_NORMAL,
#                             cairo.FONT_WEIGHT_NORMAL)
#         ctx.move_to(0.5, 0.5)
#         ctx.show_text("Drawing text")
#         # End of drawing code

#         surface.write_to_png('text.png')


