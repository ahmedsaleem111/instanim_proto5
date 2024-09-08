cd C:\Users\18055\Documents\Local_Repos\instanim\backend\engine\opengl

g++ -o render render.cpp GLAD\glad.cpp -l:libglfw3.a -lopengl32 -lgdi32 -LGLFW
@REM g++ -o render render.cpp GLAD\glad.cpp -l:libglfw3.a -lopengl32 -lgdi32 -LC:\Users\18055\Documents\Local_Repos\instanim\backend\engine\opengl\GLFW

@echo off
start errors.txt
start render.exe
exit

