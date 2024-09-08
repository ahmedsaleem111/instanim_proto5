from typing import Any
from backend.engine.dynamics import *






class Scene:

    def __init__(self,
        entities=[],
        frames=600, 
        width=1920, height=1080,
        backgroundColor='black',               
        backgroundAlpha=1,
    ):                 
        self.entities = []
        entNames = []
        for ent in entities:
            assert isinstance(ent, entity)
            if ent.name in entNames: raise Exception('All entities must be unique by name')
            entNames.append(ent.name)
            self.entities.append(ent)

        self.frames = frames
        self.width = width
        self.height = height
        self.backgroundColor = backgroundColor
        self.backgroundAlpha = backgroundAlpha


    def __iter__(self):
        self.frame = 0
        self.buffer = {} # will hold entities (by name only) to draw in current frame
        return self


    def __next__(self):
        if self.frame == self.frames:
            # do we really need to reset...? more on this...
            for ent in self.entities: 
                assert isinstance(ent, entity)                
                ent.reset() 
            raise StopIteration

        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)

        context = cairo.Context(surf)    
        mat = cairo.Matrix(xx=1, xy=0, x0=0, yx=0, yy=-1, y0=self.height)
        context.transform(mat)   

        # setting background
        context.set_source_rgba(*dsp.colorAsNumPy(self.backgroundColor), self.backgroundAlpha)
        context.rectangle(0, 0, self.width, self.height)
        context.fill()

        for ent in self.entities:
            assert isinstance(ent, entity)


            if self.frame == ent.startFrame: # add to buffer once start frame is reached
                iter(ent)
                self.buffer[ent.name] = None # value doesn't matter (place-holder) 
            if ent.name in self.buffer.keys():
                try: 
                    pars = next(ent) # may remove pars in the future...
                    ent.draw(context)
                except StopIteration: del self.buffer[ent.name] # remove from buffer once have covered complete duration

        self.frame += 1
        return surf


    def __getitem__(self, frame):
        for i, surf in enumerate(self): 
            if i == frame: return surf 
            

    async def a_preview(self, fileName, fps=30, override=False):
        if override: pth_ = fileName
        else: pth_ = ENGINE_DIR+r"/exports/clips/" + fileName

        frame_tasks = list()
        length = self.frames # right? verify...
        for i, surf in enumerate(self):

            task = asyncio.create_task(pre_proc_frame(i, surf, length))
            frame_tasks.append(task)
            task.add_done_callback(frame_tasks.remove)

        all_frames_data = await asyncio.gather(*frame_tasks)

        pipe = ffmpegCairoPipe(self.width, self.height, pth_, fps=fps)
        pipe.open()

        for i, frame_data in all_frames_data: render_with_ffmpeg(frame_data, pipe)

        pipe.close()


    def exportImage(self, fileName, frame = 0, override=False):
        if override: pth_ = fileName
        else: pth_ = ENGINE_DIR+r"/exports/pics/" + fileName

        surf = self[frame]
        surf.write_to_png(pth_)


    ''' fps is for ALL frames within interval [0, scene_dur] where first frame is at t = 0 '''
    ''' incomplete'''
    def export(self, fileName, fps=30):
        asyncio.run(self.a_preview(fileName, fps))







