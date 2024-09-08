#pragma once
#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

#include "GLM/glm.hpp"
#include "GLM/gtc/matrix_transform.hpp"
#include "GLM/gtc/type_ptr.hpp"

#include "GLAD/glad.h"
#include "GLFW/glfw3.h"
#include <typeinfo>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"





void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}




// have input control
void processInput(GLFWwindow* window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) // will return "GLFW_RELEASE" if not pressed
        glfwSetWindowShouldClose(window, true);
}




void logVertexShaderErrors(std::ofstream* errs, unsigned int shader) {

    int success;
    char infoLog[512];
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);

    if (!success) {
        glGetShaderInfoLog(shader, 512, NULL, infoLog); // retreive any error messages...

        // write error messages to errors.txt
        *errs << "ERROR::SHADER::VERTEX::COMPILATION_FAILED\n" << infoLog << std::endl;
    }

}

void logFragmentShaderErrors(std::ofstream* errs, unsigned int shader) {

    int success;
    char infoLog[512];
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);

    if (!success) {
        glGetShaderInfoLog(shader, 512, NULL, infoLog); // retreive any error messages...

        // write error messages to errors.txt
        *errs << "ERROR::SHADER::FRAGMENT::COMPILATION_FAILED\n" << infoLog << std::endl;
    }

}



void logLinkShadersErrors(std::ofstream* errs, unsigned int program) {

    int success;
    char infoLog[512];
    glGetProgramiv(program, GL_LINK_STATUS, &success);

    if (!success) {
        glGetProgramInfoLog(program, 512, NULL, infoLog); // retreive any error messages...

        // write error messages to errors.txt
        *errs << "ERROR::SHADER::PROGRAM::LINK_FAILED\n" << infoLog << std::endl;
    }

}




float scalePer(float r, float tr, float ts) {
    return exp(ts*log(r)/tr);
}




// class Shader {
//     public:
//         unsigned int ID;
//         Shader() {
//             ID = glCreateProgram();
//         }
//         void setSource(const char* vertexShaderPath, const char* fragmentShaderPath, std::ofstream* errs) {

//             std::string vertexCode;
//             std::string fragmentCode;
//             std::ifstream vShaderFile;
//             std::ifstream fShaderFile;

//             vShaderFile.exceptions (std::ifstream::failbit | std::ifstream::badbit);
//             fShaderFile.exceptions (std::ifstream::failbit | std::ifstream::badbit);

//             try 
//             {
//                 // open files
//                 vShaderFile.open(vertexShaderPath);
//                 fShaderFile.open(fragmentShaderPath);
//                 std::stringstream vShaderStream, fShaderStream;
//                 // read file's buffer contents into streams
//                 vShaderStream << vShaderFile.rdbuf();
//                 fShaderStream << fShaderFile.rdbuf();		
//                 // close file handlers
//                 vShaderFile.close();
//                 fShaderFile.close();
//                 // convert stream into string
//                 vertexCode = vShaderStream.str();
//                 fragmentCode = fShaderStream.str();			

//             }
//             catch (std::ifstream::failure& e)
//             {
//                 *errs << "ERROR::SHADER::FILE_NOT_SUCCESSFULLY_READ: " << e.what() << std::endl;
//             }


//             const char* vShaderCode = vertexCode.c_str();
//             const char * fShaderCode = fragmentCode.c_str();

//             // *errs << vShaderCode << std::endl;
//             // *errs << fShaderCode << std::endl;


//             // 2. compile shaders
//             unsigned int vertex, fragment;
//             // vertex shader
//             vertex = glCreateShader(GL_VERTEX_SHADER);
//             glShaderSource(vertex, 1, &vShaderCode, NULL);
//             glCompileShader(vertex);

//             logVertexShaderErrors(errs, vertex);

//             // fragment Shader
//             fragment = glCreateShader(GL_FRAGMENT_SHADER);
//             glShaderSource(fragment, 1, &fShaderCode, NULL);
//             glCompileShader(fragment);

//             logFragmentShaderErrors(errs, fragment);


//             glAttachShader(ID, vertex);
//             glAttachShader(ID, fragment);
//             glLinkProgram(ID);



//             logLinkShadersErrors(errs, ID);


//             // delete the shaders as they're linked into our program now and no longer necessary
//             glDeleteShader(vertex);
//             glDeleteShader(fragment);


//         }

//         void use() {
//             glUseProgram(ID);
//         }        

//         void end() {
//             glDeleteProgram(ID);
//         }


// };




// unsigned int setBuffers() {

//     static unsigned int VBO, VAO, EBO;

//     glGenVertexArrays(1, &VAO);
//     glGenBuffers(1, &VBO);
//     glGenBuffers(1, &EBO);

//     return VBO, VAO, EBO;
// }





// #ifndef GLFW_ACTIVATE
// #define GLFW_ACTIVATE   {                                                                   \
//                             if (!glfwInit()) {                                              \
//                                 std::cerr << "Failed to initialize GLFW" << std::endl;      \
//                                 return -1;                                                  \
//                             }                                                               \
//                             glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);                  \                            
//                             glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);                  \
//                             glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);  \
//                         } 
// #endif