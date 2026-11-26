from importlib.metadata import version

import access.optimisation


def test_version_comes_from_the_installed_metadata():
    """The package reports the version setuptools_scm gave the installed distribution."""
    assert access.optimisation.__version__ == version("access-configuration-optimisation")


def test_access_is_a_namespace_package():
    """``access`` is shared with access-profiling, access-config-utils and esmf-trace, so it must stay a namespace."""
    import access

    assert getattr(access, "__file__", None) is None
