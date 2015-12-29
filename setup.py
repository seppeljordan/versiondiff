#!/usr/bin/env python

# Copyright 2014 Sebastian Jordan

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

long_description=open('README')

setup(name='humboldt.versiondiff',
      version='0.1',
      description='Compare versions of buildout setups',
      long_description=long_description,
      author='Sebastian Jordan',
      author_email='jordanse@hu-berlin.de',
      url='https://scm.cms.hu-berlin.de/gitlab/cms-www/versiondiff',
      scripts=['versiondiff'],
      license="GPL",
  )
