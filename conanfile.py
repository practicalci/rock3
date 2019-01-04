#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools

class Rock3Conan(ConanFile):
    name = "rock3"
    version = "0.1"
    license = "MIT" # Use SPDX Identifiers https://spdx.org/licenses/
    author = "Giovanni Saponaro"
    url = "https://github.com/practicalci/rock3"
    description = "rock3 project"

    settings = "os", "compiler", "build_type", "arch"
    requires = "rock2/0.1@gsaponaro/testing"
    generators = "cmake"

    def imports(self):
        self.copy("*.so", dst="lib", src="lib")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
