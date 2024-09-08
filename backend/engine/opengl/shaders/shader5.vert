#version 330 core
layout (location = 0) in vec3 aPos; // position has attribute position 0
layout (location = 1) in vec3 aColor; // color has attribute position 1


uniform mat4 transform;

out vec3 ourColor; // output a color to the fragment shader

void main()
{
    gl_Position = transform * vec4(aPos, 1.0f);
    ourColor = aColor; // set ourColor to input color from the vertex data
}
