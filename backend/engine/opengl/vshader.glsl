#version 330 core
layout (location = 0) in vec3 aPos;
uniform float angle;

void main() {
    mat4 rotation = mat4(
        vec4(cos(angle), -sin(angle), 0.0, 0.0),
        vec4(sin(angle), cos(angle), 0.0, 0.0),
        vec4(0.0, 0.0, 1.0, 0.0),
        vec4(0.0, 0.0, 0.0, 1.0)
    );
    gl_Position = rotation * vec4(aPos.x, aPos.y, aPos.z, 1.0);
}