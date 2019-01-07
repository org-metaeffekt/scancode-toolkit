#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
from unittest.case import TestCase

from packagedcode.utils import parse_repo_url


class TestParseUrl(TestCase):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_parse_repo_url_basic(self):
        url = 'https://pear2.php.net'
        result = parse_repo_url(url)
        expected = 'https://pear2.php.net'
        assert expected == result

    def test_parse_repo_url_svn(self):
        url = 'http://svn.example.org/projectA/'
        result = parse_repo_url(url)
        expected = 'http://svn.example.org/projectA/'
        assert expected == result

    def test_parse_repo_url_github(self):
        url = 'https://github.com/igorw/monolog'
        result = parse_repo_url(url)
        expected = 'https://github.com/igorw/monolog'
        assert expected == result

    def test_parse_repo_url_bitbucket(self):
        url = 'git@bitbucket.org:vendor/my-private-repo.git'
        result = parse_repo_url(url)
        expected = 'https://bitbucket.org/vendor/my-private-repo.git'
        assert expected == result

