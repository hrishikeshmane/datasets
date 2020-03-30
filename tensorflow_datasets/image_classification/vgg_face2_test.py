# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Test for VGGFace2 dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import vgg_face2


class VggFace2Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = vgg_face2.VggFace2
  SPLITS = {
      "train": 6,  # Number of fake train example
      "test": 5,  # Number of fake test example
  }


if __name__ == "__main__":
  testing.test_main()
