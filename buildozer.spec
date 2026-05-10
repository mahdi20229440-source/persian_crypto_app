[app]

title = Persian Crypto
package.name = persiancrypto
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,ttf

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

permissions = INTERNET

android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.arch = armeabi-v7a, arm64-v8a
