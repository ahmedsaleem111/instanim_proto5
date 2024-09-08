from backend.engine import *
import backend.engine.utilities.displays as dsp


# import subprocess



def renderOPENGL():
    # Run the batch file
 
    print(OPENGL_PATH)

    from subprocess import Popen
    # p = Popen("render.bat", cwd=OPENGL_PATH)
    # stdout, stderr = p.communicate()
    p = Popen("C:\\Users\\18055\\Documents\\Local_Repos\\instanim\\backend\\engine\\opengl\\render.bat")
    stdout, stderr = p.communicate()


if __name__ == "__main__":
    renderOPENGL()


