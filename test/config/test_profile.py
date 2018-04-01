#!/usr/bin/python3

"""Tests related to working with profiles"""

import os.path
import unittest

import devpipeline.config.paths
import devpipeline.config.profile

_CONFIG_DIR = "{}/../files".format(os.path.dirname(os.path.abspath(__file__)))
_PROFILE_CONFIG = devpipeline.config.profile.read_profiles(
    devpipeline.config.paths.get_profile_path(_CONFIG_DIR))


class TestConfigProfile(unittest.TestCase):
    """Verify profiles are loaded and applied appropriately"""

    def _validate(self, expected, override, actual):
        self.assertTrue(override in expected)
        expected_overrides = expected[override]
        self.assertEqual(len(expected_overrides), len(actual))
        for key, value in expected_overrides.items():
            self.assertTrue(key in actual)
            self.assertEqual(value, actual[key])

    def test_none(self):
        """Verify nothing happens when no profiles are active"""
        def _dont_call(profile, values):
            # pylint: disable=unused-argument
            raise Exception("Shouldn't have been called")

        count = devpipeline.config.profile.apply_all_profiles(_PROFILE_CONFIG,
                                                              [], _dont_call)
        self.assertEqual(0, count)

    def test_single(self):
        """Verify a single profile can alter a configuration"""
        expected = {
            "debug": {
                "build_type": "Debug"
            }
        }

        count = devpipeline.config.profile.apply_all_profiles(
            _PROFILE_CONFIG, ["debug"],
            lambda p, v: self._validate(expected, p, v))
        self.assertEqual(1, count)

    def test_multiple(self):
        """Verify multiple profiles can alter a configuration"""
        expected = {
            "debug": {
                "build_type": "Debug"
            },
            "clang": {
                "cc": "clang",
                "cxx": "clang++"
            }
        }

        count = devpipeline.config.profile.apply_all_profiles(
            _PROFILE_CONFIG, ["debug", "clang"],
            lambda p, v: self._validate(expected, p, v))
        self.assertEqual(2, count)


if __name__ == "__main__":
    unittest.main()
