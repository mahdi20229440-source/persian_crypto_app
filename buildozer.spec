[app]

# (str) Title of your application
title = PersianCryptoApp

# (str) Package name
package.name = persiancryptoapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source and destination folders for the application
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (str) Main python file
source.main = main.py

# (list) Application requirements
# comma separated e.g. requirements = python3,kivy
requirements = python3,kivy,arabic-reshaper,python-bidi

# (str) Kivy version to use
kivy.version = 2.3.0

# (str) Android target SDK version
android.targetsdk = 33

# (str) Android minimum SDK version
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK version
android.sdk = 24

# (str) Android Java compiler version
android.javac_version = 17

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android theme
android.theme = @android:style/Theme.NoTitleBar

# (list) Android permissions
android.permissions = INTERNET

# (str) Application orientation (landscape, portrait, all)
orientation = portrait

# (int) Fullscreen mode
fullscreen = 0

# (bool) If your application includes a `build.py` file, this will be executed before the build
# pre-build = False

# (bool) If your application includes a `post-build.py` file, this will be executed after the build
# post-build = False

# (list) Additional files to include in the APK
# If you have custom fonts or images, put them here
# If you have sub-folders in your project, add them too (e.g. data/)
android.add_aab_deps = Vazirmatn-Bold.ttf

# (str) Log level
log_level = 2

# (bool) Enable Android debug mode
debug = 1

# (list) Exclude the following from the APK
# don't forget to include space at the end of each line
exclude_dirs = .buildozer, .git, .github

# (list) Include the following in the APK
# don't forget to include space at the end of each line
include_dirs = 

[buildozer]
# (str) The directory where buildozer will put its stuff
build_dir = .buildozer

# (str) The target machine's architecture for the build
# arch = x86_64

# (str) The default Docker image for building
# docker_image = kivy/buildozer:stable

# (str) The build platform (android, ios, desktop)
# platform = android
