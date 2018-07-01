#!/usr/bin/python3

import importlib
import pkgutil


def _iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


def _find_plugins(ns_pkg):
    return {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in _iter_namespace(ns_pkg)
    }


_PLUGINS = {}


def _load_plugins():
    global _PLUGINS

    if not _PLUGINS:
        try:
            import devpipeline_plugins
            _PLUGINS = _find_plugins(devpipeline_plugins)
        except ImportError:
            # if the import fails, it means no plugins are installed
            pass


def query_plugins(query_fn, found_fn):
    _load_plugins()
    for module in _PLUGINS.values():
        try:
            element = getattr(module, query_fn)
            if element:
                found_fn(element())
        except AttributeError:
            # the plugin doesn't have the requested function; just ignore,
            # since it's the same scenario as the plugin not existing.
            pass


def initialize_simple_plugins(plugin_handles, query_fn):
    def add_plugin(scms):
        for key, fn in scms.items():
            if key not in plugin_handles:
                plugin_handles[key] = fn
            else:
                raise Exception(
                    "Multiple plugins registering \"{}\"".format(key))

    query_plugins(query_fn, add_plugin)
