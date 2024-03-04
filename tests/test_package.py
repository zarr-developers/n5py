from __future__ import annotations

import importlib.metadata

import n5py as m


def test_version():
    assert importlib.metadata.version("n5py") == m.__version__
