from gl import Renderer
import shaders

# Tamaño del Frame para la pantalla
width = 1500
height = 1000

# Create Render
rend = Renderer(width, height)

# Shaders a utilizar
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

# Carga de cada modelo, hay varios por la rotación del objeto
rend.glLoadModel(filename = "models/model.obj",
                 textureName = "textures/model.bmp",
                 translate = (250, 500, 0),
                 rotate = (0, 90, 0),
                 scale = (25,25,25))


rend.glLoadModel(filename = "models/model.obj",
                 textureName = "textures/model.bmp",
                 translate = (750, 500, 0),
                 rotate = (0, 180, 0),
                 scale = (25,25,25))

rend.glLoadModel(filename = "models/model.obj",
                 textureName = "textures/model.bmp",
                 translate = (1250, 500, 0),
                 rotate = (0, 270, 0),
                 scale = (25,25,25))

rend.glLoadModel(filename = "models/model.obj",
                 textureName = "textures/model.bmp",
                 translate = (750, 0, 0),
                 rotate = (0, 360, 0),
                 scale = (25,25,25))

# Render scene
rend.glRender()

# FrameBuffer con la escena renderizada
rend.glFinish("output.bmp")
