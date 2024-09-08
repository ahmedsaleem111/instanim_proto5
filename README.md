Current working iteration of "instanim" application. Incorporates not just the engine, but all externals around it to make a complete web application.

Will be migrating from Cairo to OpenGL as the primary graphics backend for both 2D and 3D graphics. Cairo will be moved to a backup option for 2D graphics only. 

All OpenGL functionality will be coded in C++ for better performance. The OpenGL layer will essentially be the "render" layer. Calls from layers above will be in Python mostly.

See "instanim_protoX" (X is iteration count) modules for all previous iterations.
