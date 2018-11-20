# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 BigML
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
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


""" Creating PCA

"""
from world import world, setup_module, teardown_module
import create_source_steps as source_create
import create_dataset_steps as dataset_create
import create_pca_steps as pca_create

class TestPCA(object):

    def setup(self):
        """
            Debug information
        """
        print "\n-------------------\nTests in: %s\n" % __name__

    def teardown(self):
        """
            Debug information
        """
        print "\nEnd of tests in: %s\n-------------------\n" % __name__

    def test_scenario1(self):
        """
            Scenario: Successfully creating a PCA from a dataset:
                Given I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a PCA from a dataset
                And I wait until the PCA is ready less than <time_3> secs
                And I update the PCA name to "<pca_name>"
                When I wait until the PCA is ready less than <time_4> secs
                Then the PCA name is "<pca_name>"

                Examples:
                | data                | time_1  | time_2 | time_3 | time_4 | pca_name |
                | ../data/iris.csv | 10      | 10     | 20     | 20 | my new pca name |
        """
        print self.test_scenario1.__doc__
        examples = [
            ['data/iris.csv', '10', '10', '20', '20', 'my new pca name']]
        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            pca_create.i_create_a_pca_from_dataset(self)
            pca_create.the_pca_is_finished_in_less_than(self, example[3])
            pca_create.i_update_pca_name(self, example[5])
            pca_create.the_pca_is_finished_in_less_than(self, example[4])
            pca_create.i_check_pca_name(self, example[5])
