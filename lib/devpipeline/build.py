#!/usr/bin/python3
"""This modules aggregates the available builders that can be used."""

import os.path
import os

import devpipeline.plugin
import devpipeline.toolsupport


# Every builder supported should have an entry in this dictionary.  The key
# needs to match whatever value the "build" key is set to in build.conf, and
# the value should be a function that takes a component and returns a Builder.
_BUILDERS = {}


def _initialize_builders():
    global _BUILDERS

    if not _BUILDERS:
        class NothingBuilder:
            def configure(self, src_dir, build_dir):
                pass

            def build(self, build_dir):
                pass

            def install(self, build_dir, path):
                pass

        _BUILDERS = {
            "nothing": lambda c, cw: cw(NothingBuilder())
        }

        devpipeline.plugin.initialize_simple_plugins(_BUILDERS, "get_builders")


def _make_builder(current_target, common_wrapper):
    """
    Create and return a Builder for a component.

    Arguments
    component - The component the builder should be created for.
    """
    _initialize_builders()
    return devpipeline.toolsupport.tool_builder(
        current_target["current_config"], "build", _BUILDERS,
        current_target, common_wrapper)


class SimpleBuild(devpipeline.toolsupport.SimpleTool):

    """This class does a simple build - configure, build, and install."""

    def __init__(self, real, current_target):
        super().__init__(current_target, real)

    def configure(self, src_dir, build_dir):
        # pylint: disable=missing-docstring
        self._call_helper("Configuring", self.real.configure,
                          src_dir, build_dir)

    def build(self, build_dir):
        # pylint: disable=missing-docstring
        self._call_helper("Building", self.real.build,
                          build_dir)

    def install(self, build_dir, path=None):
        # pylint: disable=missing-docstring
        self._call_helper("Installing", self.real.install,
                          build_dir, path)


def build_task(current_target):
    """
    Build a target.

    Arguments
    target - The target to build.
    """

    target = current_target["current_config"]
    build_path = target.get("dp.build_dir")
    if not os.path.exists(build_path):
        os.makedirs(build_path)
    builder = _make_builder(
        current_target,
        lambda r: SimpleBuild(r, current_target))
    builder.configure(target.get("dp.src_dir"), build_path)
    builder.build(build_path)
    if "no_install" not in target:
        builder.install(build_path, path=target.get("install_path",
                                                    "install"))
