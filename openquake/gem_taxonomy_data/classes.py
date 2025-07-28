# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2024 GEM Foundation
#
# Openquake Gem Taxonomy is free software: you can redistribute it and/or
# modify it # under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
import os
import json
from .version import __version__ as GemTaxonomyDataVersion


class GemTaxonomyData:
    DEFAULT_TAX_VERSION = '3.3'
    AVAILABLE_TAX_VERSIONS = ['3.3', '4.0']

    BASE_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')

    @classmethod
    @property
    def __version__(cls):
        return GemTaxonomyDataVersion

    def load(self, standard_version='default'):
        if standard_version == 'default':
            standard_version = self.DEFAULT_TAX_VERSION

        if '/' in standard_version or '\\' in standard_version:
            raise ValueError('no file separators are allowed.')

        return json.load(open(os.path.join(
            self.BASE_DATA_PATH,
            'taxonomy%s_standard.json' % standard_version)))
