platform_name = ""
if "Windows" == platform.system():
    platform_name = "Windows"
    os.environ['KIVY_IMAGE'] = 'pil,sdl2'
    os.environ['KIVY_WINDOW'] = 'pil,sdl2'
elif os.uname()[1] == 'raspberrypi':
    platform_name = "RaspberyPi"
    os.environ['KIVY_WINDOW'] = 'sdl2'  # Necessary to RaspberryPi
    os.environ['KIVY_GL_BACKEND'] = 'sdl2'
print("[Info] Detected Platform: " + platform_name)