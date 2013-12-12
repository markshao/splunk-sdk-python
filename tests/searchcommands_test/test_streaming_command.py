#!/usr/bin/env python
#
# Copyright 2011-2013 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from searchcommands_test.utilities import chdir, open_data_file
from splunklib.searchcommands import dispatch, test
import countmatches

chdir(countmatches)

argv = ['fieldname=word_count', 'pattern=\\w+', 'text']

dispatch(
    countmatches.CountMatchesCommand, ['countmatches', '__GETINFO__'] + argv)

dispatch(
    countmatches.CountMatchesCommand, ['countmatches', '__EXECUTE__'] + argv,
    input_file=open_data_file('tweets.csv'))