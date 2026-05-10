[app]
title = CryptoPriceApp
package.name = cryptopriceapp
package.domain = org.example
source.dir = .
version = 0.1
source.main = main.py
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer
kivy.version = 2.3.0
android.permissions = INTERNET
android.targetsdk = 33
android.minapi = 21
orientation = portrait
fullscreen = 0
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
log_level = 2
warn_on_root = 1

[buildozer]
build_dir = .buildozer
log_level = 2
