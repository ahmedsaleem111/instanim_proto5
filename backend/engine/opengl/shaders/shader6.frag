#version 330 core

out vec4 FragColor;

in vec3 ourColor;
in vec2 TexCoord;

uniform sampler2D ourTexture1;
uniform sampler2D ourTexture2;
uniform float mixer;

void main() {
    FragColor = mix(texture(ourTexture1, TexCoord), texture(ourTexture2, TexCoord), mixer) * vec4(ourColor, 1.0);
}