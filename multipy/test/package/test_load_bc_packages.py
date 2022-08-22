# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# Owner(s): ["oncall: package/deploy"]

from pathlib import Path
from unittest import skipIf

from multipy.package import PackageImporter
from torch.testing._internal.common_utils import IS_FBCODE, IS_SANDCASTLE, run_tests

try:
    from .common import PackageTestCase
except ImportError:
    # Support the case where we run this file directly.
    from common import PackageTestCase

class TestLoadBCPackages(PackageTestCase):
    """Tests for checking loading has backwards compatiblity with multipy.package"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.packaging_directory = f"{Path(__file__).parent}/package_bc"

    @skipIf(
        IS_FBCODE or IS_SANDCASTLE,
        "Tests that use temporary files are disabled in fbcode",
    )
    def test_load_bc_packages_nn_module(self):
        """Tests for backwards compatible nn module"""
        importer1 = PackageImporter(f"{self.packaging_directory}/test_nn_module.pt")
        loaded1 = importer1.load_pickle("nn_module", "nn_module.pkl")

    @skipIf(
        IS_FBCODE or IS_SANDCASTLE,
        "Tests that use temporary files are disabled in fbcode",
    )
    def test_load_bc_packages_torchscript_module(self):

        """Tests for backwards compatible torchscript module"""
        importer2 = PackageImporter(f"{self.packaging_directory}/test_torchscript_module.pt")
        loaded2 = importer2.load_pickle("torchscript_module", "torchscript_module.pkl")

    @skipIf(
        IS_FBCODE or IS_SANDCASTLE,
        "Tests that use temporary files are disabled in fbcode",
    )
    def test_load_bc_packages_fx_module(self):
        """Tests for backwards compatible fx module"""
        importer3 = PackageImporter(f"{self.packaging_directory}/test_fx_module.pt")
        loaded3 = importer3.load_pickle("fx_module", "fx_module.pkl")

class TestLoadBCTorchPackages(TestLoadBCPackages):
    """Tests for checking loading has backwards compatiblity with torch.package"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.packaging_directory= f"{Path(__file__).parent}/package_bc_torch"

if __name__ == "__main__":
    run_tests()
