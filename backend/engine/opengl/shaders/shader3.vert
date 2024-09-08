#version 330 core
layout (location = 0) in vec3 aPos; // position has attribute position 0
layout (location = 1) in vec3 aColor; // color has attribute position 1

uniform float stepX;
out vec3 ourColor; // output a color to the fragment shader

void main()
{
    gl_Position = vec4(aPos.x + stepX, aPos.y, aPos.z, 1.0f);
    ourColor = aColor; // set ourColor to input color from the vertex data
}
