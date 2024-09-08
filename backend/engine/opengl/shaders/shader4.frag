#version 330 core
out vec4 FragColor;
// in vec3 ourColor;
in vec3 ourPosition;
// position values to be clamped between 0 and 1?? hence why we see black for bottom-left corner??

void main()
{
    FragColor = vec4(ourPosition, 1.0);    // note how the position value is linearly interpolated to get all the different colors
}