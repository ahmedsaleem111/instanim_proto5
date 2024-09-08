cd C:\Users\18055\Documents\Local_Repos\instanim\backend\engine\opengl

@REM g++ -o test test.cpp 
g++ -o test test.cpp GLAD\glad.cpp -l:libglfw3.a -lopengl32 -lgdi32 -LC:\Users\18055\Documents\Local_Repos\instanim\backend\engine\opengl\GLFW

@echo off
start test.exe

exit

