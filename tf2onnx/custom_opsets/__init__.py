# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.
""" custom tf2onnx mapping functions. """

from . import ms
from .. import constants

DOMAIN_OPSETS = {
    constants.MICROSOFT_DOMAIN: ms.OPSETS
}