# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2017-2018 BigML
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


""" Comparing remote and local predictions

"""
from world import world, setup_module, teardown_module, show_doc
import create_source_steps as source_create
import create_dataset_steps as dataset_create
import create_model_steps as model_create
import create_time_series_steps as time_series_create
import create_forecast_steps as forecast_create
import compare_forecasts_steps as forecast_compare
import create_pca_steps as pca_create
import create_projection_steps as projection_create
import compare_predictions_steps as compare_predictions


class TestComparePrediction(object):

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
            Scenario: Successfully comparing forecasts from time series:
                Given I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a time series with "<params>"
                And I wait until the time series is ready less than <time_3> secs
                And I create a local time series
                When I create a forecast for "<input_data>"
                Then the forecast is "<forecasts>"
                And I create a local forecast for "<data_input>"
                Then the local forecast is "<forecasts>"

                Examples:
                | data             | time_1  | time_2 | time_3 | input_data  | forecasts | params
            ['data/grades.csv', '10', '10', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["A,Ad,N"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast":  [69.90959, 69.92755, 69.94514, 69.96236, 69.97922], "model": "A,Ad,N"}]}', '{"objective_fields": ["000001", "000005"]}'],


        """
        examples = [
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5}}', '{"000005": [{"point_forecast": [73.96192, 74.04106, 74.12029, 74.1996, 74.27899], "model": "M,M,N"}]}', '{"objective_fields": ["000001", "000005"]}'],
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["M,N,N"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast":  [68.39832, 68.39832, 68.39832, 68.39832, 68.39832], "model": "M,N,N"}]}', '{"objective_fields": ["000001", "000005"]}'],
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["A,A,N"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast": [72.46247, 72.56247, 72.66247, 72.76247, 72.86247], "model": "A,A,N"}]}', '{"objective_fields": ["000001", "000005"]}'],
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5}, "000001": {"horizon": 3, "ets_models": {"criterion": "aic", "limit": 2}}}', '{"000005": [{"point_forecast": [73.96192, 74.04106, 74.12029, 74.1996, 74.27899], "model": "M,M,N"}], "000001": [{"point_forecast": [55.51577, 89.69111, 82.04935], "model": "A,N,A"}, {"point_forecast": [56.67419, 91.89657, 84.70017], "model": "A,A,A"}]}', '{"objective_fields": ["000001", "000005"]}']]
        show_doc(self.test_scenario1, examples)

        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            time_series_create.i_create_a_time_series_with_params(self, example[6])
            time_series_create.the_time_series_is_finished_in_less_than(self, example[3])
            time_series_create.create_local_time_series(self)
            forecast_create.i_create_a_forecast(self, example[4])
            forecast_create.the_forecast_is(self, example[5])
            forecast_compare.i_create_a_local_forecast(self, example[4])
            forecast_compare.the_local_forecast_is(self, example[5])


    def test_scenario2(self):
        """
            Scenario: Successfully comparing forecasts from time series with "A" seasonality
                Given I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a time series with "<params>"
                And I wait until the time series is ready less than <time_3> secs
                And I create a local time series
                When I create a forecast for "<input_data>"
                Then the forecast is "<forecasts>"
                And I create a local forecast for "<data_input>"
                Then the local forecast is "<forecasts>"

                Examples:
                | data             | time_1  | time_2 | time_3 | input_data  | forecasts | params
            ['data/grades.csv', '10', '10', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["A,Ad,A"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast":[66.16225, 72.17308, 66.65573, 73.09698, 70.51449], "model": "A,Ad,A"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}']
        """
        examples = [

            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5}}', '{"000005": [{"point_forecast": [73.96192, 74.04106, 74.12029, 74.1996, 74.27899], "model": "M,M,N"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}'],
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["M,N,A"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast":  [67.43222, 68.24468, 64.14437, 67.5662, 67.79028], "model": "M,N,A"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}'],
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["A,A,A"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast": [74.73553, 71.6163, 71.90264, 76.4249, 75.06982], "model": "A,A,A"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}']]
        show_doc(self.test_scenario2, examples)

        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            time_series_create.i_create_a_time_series_with_params(self, example[6])
            time_series_create.the_time_series_is_finished_in_less_than(self, example[3])
            time_series_create.create_local_time_series(self)
            forecast_create.i_create_a_forecast(self, example[4])
            forecast_create.the_forecast_is(self, example[5])
            forecast_compare.i_create_a_local_forecast(self, example[4])
            forecast_compare.the_local_forecast_is(self, example[5])

    def test_scenario3(self):
        """
            Scenario: Successfully comparing forecasts from time series with "M" seasonality
                Given I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a time series with "<params>"
                And I wait until the time series is ready less than <time_3> secs
                And I create a local time series
                When I create a forecast for "<input_data>"
                Then the forecast is "<forecasts>"
                And I create a local forecast for "<data_input>"
                Then the local forecast is "<forecasts>"

                Examples:
                | data             | time_1  | time_2 | time_3 | input_data  | forecasts | params

,
            ['data/grades.csv', '10', '10', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["M,Ad,M"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast": [73.75816, 74.60699, 66.71212, 72.49586, 71.76787], "model": "M,Ad,M"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}'],
            ['data/grades.csv', '10', '10', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["M,Md,M"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast": [74.3725, 75.02963, 67.15826, 73.19628, 71.66919], "model": "M,Md,M"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}']

        """
        examples = [
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["M,N,M"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast":  [68.99775, 72.76777, 66.5556, 70.90818, 70.92998], "model": "M,N,M"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}'],
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["M,A,M"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast": [70.65993, 78.20652, 69.64806, 75.43716, 78.13556], "model": "M,A,M"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}'],
            ['data/grades.csv', '30', '30', '120', '{"000005": {"horizon": 5, "ets_models": {"names": ["M,M,M"], "criterion": "aic", "limit": 3}}}', '{"000005": [{"point_forecast": [71.75055, 80.67195, 70.81368, 79.84999, 78.27634], "model": "M,M,M"}]}', '{"objective_fields": ["000001", "000005"], "period": 12}']]
        show_doc(self.test_scenario3, examples)

        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            time_series_create.i_create_a_time_series_with_params(self, example[6])
            time_series_create.the_time_series_is_finished_in_less_than(self, example[3])
            time_series_create.create_local_time_series(self)
            forecast_create.i_create_a_forecast(self, example[4])
            forecast_create.the_forecast_is(self, example[5])
            forecast_compare.i_create_a_local_forecast(self, example[4])
            forecast_compare.the_local_forecast_is(self, example[5])


    def test_scenario4(self):
        """
            Scenario: Successfully comparing forecasts from time series with trivial models
                Given I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a time series with "<params>"
                And I wait until the time series is ready less than <time_3> secs
                And I create a local time series
                When I create a forecast for "<input_data>"
                Then the forecast is "<forecasts>"
                And I create a local forecast for "<data_input>"
                Then the local forecast is "<forecasts>"

                Examples:
                | data             | time_1  | time_2 | time_3 | input_data  | forecasts | params

        """
        examples = [
            ['data/grades.csv', '10', '1000', '1000', '{"000005": {"horizon": 5, "ets_models": {"names": ["naive"]}}}', '{"000005": [{"point_forecast": [61.39, 61.39, 61.39, 61.39, 61.39], "model": "naive"}]}', '{"objective_fields": ["000001", "000005"], "period": 1}'],
            ['data/grades.csv', '10', '1000', '1000', '{"000005": {"horizon": 5, "ets_models": {"names": ["naive"]}}}', '{"000005": [{"point_forecast": [78.89, 61.39, 78.89, 61.39, 78.89], "model": "naive"}]}', '{"objective_fields": ["000001", "000005"], "period": 2}'],
            ['data/grades.csv', '10', '1000', '1000', '{"000005": {"horizon": 5, "ets_models": {"names": ["mean"]}}}', '{"000005": [{"point_forecast": [68.45974, 68.45974, 68.45974, 68.45974, 68.45974], "model": "mean"}]}', '{"objective_fields": ["000001", "000005"], "period": 1}'],
            ['data/grades.csv', '10', '1000', '1000', '{"000005": {"horizon": 5, "ets_models": {"names": ["mean"]}}}', '{"000005": [{"point_forecast": [69.79553, 67.15821, 69.79553, 67.15821, 69.79553], "model": "mean"}]}', '{"objective_fields": ["000001", "000005"], "period": 2}'],
            ['data/grades.csv', '10', '1000', '1000', '{"000005": {"horizon": 5, "ets_models": {"names": ["drift"]}}}', '{"000005": [{"point_forecast": [61.50545, 61.6209, 61.73635, 61.8518, 61.96725], "model": "drift"}]}', '{"objective_fields": ["000001", "000005"], "period": 1}'],
            ['data/grades.csv', '10', '1000', '1000', '{"000005": {"horizon": 5, "ets_models": {"names": ["drift"]}}}', '{"000005": [{"point_forecast": [61.50545, 61.6209, 61.73635, 61.8518, 61.96725], "model": "drift"}]}', '{"objective_fields": ["000001", "000005"], "period": 2}']]
        show_doc(self.test_scenario4, examples)

        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            time_series_create.i_create_a_time_series_with_params(self, example[6])
            time_series_create.the_time_series_is_finished_in_less_than(self, example[3])
            time_series_create.create_local_time_series(self)
            forecast_create.i_create_a_forecast(self, example[4])
            forecast_create.the_forecast_is(self, example[5])
            forecast_compare.i_create_a_local_forecast(self, example[4])
            forecast_compare.the_local_forecast_is(self, example[5])


    def test_scenario5(self):
        """
            Scenario: Successfully comparing projections for PCAs:
                Given I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a PCA with "<params>"
                And I wait until the PCA is ready less than <time_3> secs
                And I create a local PCA
                When I create a projection for "<input_data>"
                Then the projection is "<projection>"
                And I create a local projection for "<data_input>"
                Then the local projection is "<projection>"

                Examples:
                | data             | time_1  | time_2 | time_3 | input_data  | projection | params


        """
        examples = [
            ['data/iris.csv', '30', '30', '120', '{}',
             '{"PC2": 0, "PC3": 1e-05, "PC1": 2e-05, "PC6": 0, "PC4": 0, "PC5": -2e-05}', '{}'],
            ['data/iris.csv', '30', '30', '120', '{"petal length": 1}',
             '{"PC2": 0.10109, "PC3": 0.16123, "PC1": 3.07314, "PC6": -0.1652, "PC4": 0.28663, "PC5": -0.16477}', '{}'],
            ['data/iris.csv', '30', '30', '120', '{"species": "Iris-versicolor"}',
             '{"PC2": 2.15914, "PC3": -1.54734, "PC1": -1.20336, "PC6": -0.08233, "PC4": -0.96098, "PC5": 0.07091}', '{}'],
            ['data/iris.csv', '30', '30', '120', '{"petal length": 1, "sepal length": 0, "petal width": 0, "sepal width": 0, "species": "Iris-versicolor"}',
             '{"PC2": 8.33399, "PC3": 5.01889, "PC1": 5.47656, "PC6": 0.02629, "PC4": -0.76555, "PC5": 0.09413}', '{}']]
        show_doc(self.test_scenario5, examples)

        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            pca_create.i_create_a_pca_with_params(self, example[6])
            pca_create.the_pca_is_finished_in_less_than(self, example[3])
            compare_predictions.create_local_pca(self)
            projection_create.i_create_a_projection(self, example[4])
            projection_create.the_projection_is(self, example[5])
            compare_predictions.i_create_a_local_projection(self, example[4])
            compare_predictions.the_local_projection_is(self, example[5])



    def test_scenario6(self):
        """
            Scenario: Successfully comparing projections for PCAs:
                Given I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a PCA with "<params>"
                And I wait until the PCA is ready less than <time_3> secs
                And I create a local PCA
                When I create a projection for "<input_data>"
                Then the projection is "<projection>"
                And I create a local projection for "<data_input>"
                Then the local projection is "<projection>"

                Examples:
                | data             | time_1  | time_2 | time_3 | input_data  | projection | params
        """
        examples = [
            ['data/spam_tiny.csv', '30', '30', '30', '{"fields": {"000001": {"optype": "text", "term_analysis": {"token_mode": "all"}}}}', '{"Message": "early"}', '{}', '{"PC40": 0, "PC38": 0.01197, "PC39": -1e-05, "PC18": -0.30635, "PC19": 0.15681, "PC14": 0.24903, "PC15": 0.2853, "PC16": -0.03769, "PC17": -0.03074, "PC10": -0.20212, "PC11": 0.55543, "PC12": -0.15796, "PC13": -0.186, "PC43": 0, "PC42": 0, "PC41": 0, "PC25": -0.05249, "PC24": -0.2261, "PC27": -0.08064, "PC26": 0.12261, "PC21": 0.23743, "PC20": -0.29411, "PC23": -0.35753, "PC22": 0.29116, "PC47": 0, "PC49": 0, "PC48": 0, "PC29": 0.0918, "PC28": 0.24181, "PC32": -0.02223, "PC46": 0, "PC31": -0.06144, "PC45": 0, "PC36": -0.00743, "PC44": 0, "PC37": -0.01394, "PC34": 0.09211, "PC35": 0.07081, "PC33": 0.08747, "PC8": 0.01767, "PC9": 0.24043, "PC2": -0.17494, "PC3": 0.26523, "PC1": 1.6119, "PC6": 0.67905, "PC7": -0.0393, "PC4": -0.08702, "PC5": 0.13242, "PC50": 0, "PC30": -0.03738}'],
    ['data/spam.csv', '30', '30', '30', '{"fields": {"000001": {"optype": "text", "term_analysis": {"token_mode": "all"}}}}', '{"Message": "early"}', '{}', '{"PC560": 0, "PC259": -0.00773, "PC258": 0.04902, "PC554": -2e-05, "PC555": 0.00048, "PC552": 0.00018, "PC553": -3e-05, "PC550": -0.00046, "PC551": 0.00019, "PC251": -0.00567, "PC250": 0.05941, "PC253": 0.09695, "PC252": -0.23688, "PC255": -0.04982, "PC254": -0.13867, "PC257": -0.13916, "PC256": 0.05418, "PC43": 0.08686, "PC42": -0.16503, "PC41": -0.01947, "PC40": -0.09511, "PC47": -0.14033, "PC46": 0.29207, "PC45": 0.02295, "PC44": -0.02894, "PC49": -0.13356, "PC48": -0.21307, "PC332": -0.02838, "PC333": 0.00447, "PC330": 0.09832, "PC331": 0.00227, "PC336": 0.10526, "PC337": -0.0243, "PC334": -0.01767, "PC335": -0.07488, "PC338": 0.01696, "PC339": 0.0272, "PC141": 0.09478, "PC140": -0.12973, "PC143": 0.08848, "PC142": 0.06037, "PC145": -0.04621, "PC144": 0.14305, "PC147": 0.04841, "PC146": 0.0648, "PC149": -0.12082, "PC148": 0.00132, "PC387": -0.01617, "PC386": 0.01712, "PC385": 0.06258, "PC384": 0.0179, "PC383": -0.02, "PC382": 0.01124, "PC381": -0.04208, "PC380": -0.01693, "PC519": -0.00086, "PC389": 0.01021, "PC388": -0.02336, "PC581": 0, "PC556": -0.0001, "PC583": 0, "PC582": 0, "PC585": 0, "PC584": 0, "PC587": 0, "PC557": 0, "PC589": 0, "PC588": 0, "PC8": 0.77185, "PC9": 0.43433, "PC2": 1.62401, "PC3": 0.65596, "PC1": 1.1867, "PC6": 0.29764, "PC7": -0.10726, "PC4": 0.72867, "PC5": -0.97838, "PC38": -0.2902, "PC39": -0.06089, "PC32": -0.15371, "PC33": 0.31096, "PC30": 0.47035, "PC31": -0.10414, "PC36": 0.31575, "PC37": 0.03171, "PC34": -0.4212, "PC35": -0.11748, "PC299": 0.02622, "PC298": 0.06238, "PC295": 0.01525, "PC294": 0.00781, "PC297": 0.02746, "PC296": 0.0399, "PC291": -0.00102, "PC290": 0.03122, "PC293": -0.08383, "PC292": -0.02192, "PC453": -0.02945, "PC452": -0.01815, "PC451": -0.00998, "PC450": -0.02919, "PC457": -0.02259, "PC456": -0.00938, "PC455": 0.02332, "PC454": 0.00702, "PC512": -0.00126, "PC513": -0.0023, "PC459": -0.00428, "PC458": -0.04694, "PC516": -0.01062, "PC517": -0.00529, "PC514": 0.00753, "PC515": 0.00211, "PC509": -0.00207, "PC508": 0.01171, "PC206": -0.09304, "PC207": -0.08959, "PC204": -0.00877, "PC205": 0.11803, "PC202": 0.13881, "PC203": -0.03187, "PC200": 0.10573, "PC201": 0.0166, "PC208": 0.07402, "PC209": 0.01823, "PC639": 0, "PC638": 0, "PC637": 0, "PC636": 0, "PC635": 0, "PC634": 0, "PC633": 0, "PC632": 0, "PC631": 0, "PC630": 0, "PC507": 0.00397, "PC506": 0.011, "PC349": -0.01467, "PC348": -0.01775, "PC343": 0.03446, "PC342": 0.00177, "PC341": 0.01203, "PC340": -0.01938, "PC347": 0.01309, "PC346": -0.03476, "PC345": -0.00254, "PC344": -0.00223, "PC118": 0.02583, "PC119": -0.1533, "PC116": -0.14799, "PC117": 0.07593, "PC114": -0.11968, "PC115": -0.10557, "PC112": 0.03841, "PC113": -0.10774, "PC110": 0.10157, "PC111": 0.15881, "PC417": 0.00939, "PC416": 0.02312, "PC415": -0.02884, "PC414": 0.01426, "PC413": -0.0235, "PC412": 0.00031, "PC411": 0.04366, "PC410": -0.02353, "PC419": 0.02098, "PC418": 0.01074, "PC85": 0.11165, "PC563": 0, "PC562": 0, "PC248": 0.07305, "PC249": 0.03639, "PC567": 0, "PC566": 0, "PC565": 0, "PC564": 0, "PC242": -0.17882, "PC243": 0.09006, "PC240": -0.10115, "PC241": -0.03022, "PC246": 0.12995, "PC247": 0, "PC244": -0.02565, "PC245": 0.03223, "PC78": 0.01463, "PC79": 0.08106, "PC76": -0.1117, "PC77": 0.36391, "PC74": 0.01606, "PC75": 0.00157, "PC72": 0.32372, "PC73": 0.19988, "PC70": 0.12158, "PC71": 0.05259, "PC94": 0.13581, "PC95": 0.14569, "PC96": -0.12308, "PC97": -0.04808, "PC90": 0.03966, "PC91": 0.03302, "PC309": 0.06329, "PC308": -0.08198, "PC307": 0.07417, "PC306": -0.10445, "PC305": 0.02323, "PC304": -0.02005, "PC303": 0.11291, "PC302": -0.05606, "PC301": -0.09993, "PC300": -0.08212, "PC152": -0.10084, "PC153": 0.13864, "PC150": -0.14771, "PC151": -0.0912, "PC156": -0.0207, "PC157": 0.05674, "PC154": 0.09954, "PC155": 0.1071, "PC158": 0.04847, "PC159": 0.00745, "PC390": -0.04411, "PC391": -0.01279, "PC392": 0.02571, "PC393": -0.0008, "PC394": -0.02196, "PC395": -0.0179, "PC396": 0.02454, "PC397": -0.01386, "PC398": 0.02572, "PC399": -0.00552, "PC592": 0, "PC593": 0, "PC590": 0, "PC591": 0, "PC596": 0, "PC597": 0, "PC594": 0, "PC595": 0, "PC598": 0, "PC599": 0, "PC527": -0.00023, "PC526": 0.00249, "PC525": -0.00044, "PC524": 0.00215, "PC523": 0.00426, "PC522": 0.00198, "PC288": 0.07414, "PC289": -0.00097, "PC286": 0.06387, "PC287": -0.08433, "PC284": 0.03245, "PC285": -0.05211, "PC282": -0.01777, "PC283": -0.06055, "PC280": -0.03412, "PC281": 0.00161, "PC448": -0.03816, "PC449": -0.00648, "PC444": -0.01761, "PC445": -0.00454, "PC446": -0.00332, "PC447": -0.00026, "PC440": -0.0025, "PC441": -0.02732, "PC442": 0.04714, "PC443": -0.00779, "PC549": -0.00036, "PC548": -0.00072, "PC233": 0.1529, "PC232": -0.07745, "PC231": 0.01319, "PC230": -0.02562, "PC237": -0.0181, "PC236": -0.1072, "PC235": 0.05871, "PC234": 0.08369, "PC239": -0.12613, "PC238": 0.08465, "PC25": -0.05189, "PC24": 0.03773, "PC27": -0.2713, "PC26": -0.21128, "PC21": 0.14541, "PC20": 0.194, "PC23": -0.01968, "PC22": -0.08367, "PC29": 0.15754, "PC28": -0.04742, "PC628": 0, "PC629": 0, "PC620": 0, "PC559": 0, "PC622": 0, "PC623": 0, "PC624": 0, "PC625": 0, "PC626": 0, "PC627": 0, "PC354": 0.08814, "PC355": -0.01598, "PC356": -0.05687, "PC357": 0.05258, "PC350": -0.06777, "PC351": 0.04339, "PC352": -0.00202, "PC353": -0.06768, "PC578": 0, "PC358": -0.02448, "PC359": -0.01661, "PC579": 0, "PC521": 0.00453, "PC499": -0.01135, "PC498": 0.00381, "PC497": -0.00442, "PC496": -0.014, "PC495": -0.00614, "PC494": -0.02365, "PC493": 0.01533, "PC492": 0.01748, "PC491": 0.00105, "PC490": 0.00378, "PC129": -0.05167, "PC128": -0.06481, "PC123": 0.04975, "PC122": -0.0431, "PC121": 0.13246, "PC120": 0.03659, "PC127": -0.17542, "PC126": 0.05075, "PC125": 0.02246, "PC124": -0.14646, "PC529": 4e-05, "PC528": 0.00065, "PC400": -0.00076, "PC401": -0.00826, "PC402": 0.01908, "PC403": -0.00531, "PC404": -0.00363, "PC405": -0.01148, "PC406": -0.03119, "PC407": -0.01869, "PC408": 0.02103, "PC409": -7e-05, "PC586": 0, "PC18": -0.01177, "PC19": 0.08077, "PC580": 0, "PC14": -1.07937, "PC15": 0.35006, "PC16": 0.00242, "PC17": 0.15093, "PC10": -0.2489, "PC11": 0.22074, "PC12": 0.45436, "PC13": 0.37047, "PC277": 0.13491, "PC276": -0.03629, "PC275": -0.06707, "PC274": 0.05559, "PC273": 0.1381, "PC272": -0.0368, "PC271": 0.09624, "PC270": -0.01544, "PC279": -0.04512, "PC278": 0.06699, "PC475": 0.00329, "PC474": 0.0229, "PC477": 0.01223, "PC476": 0.01518, "PC471": 0.00798, "PC470": -0.00526, "PC473": 0.01313, "PC472": -0.00152, "PC574": 0, "PC575": 0, "PC576": 0, "PC577": 0, "PC479": 0.00661, "PC478": -0.01428, "PC572": 0, "PC573": 0, "PC69": -0.04958, "PC68": 0.15642, "PC61": -0.11131, "PC60": 0.05147, "PC63": 0.17035, "PC62": -0.19311, "PC65": 0.14813, "PC64": 0.18248, "PC67": -0.17425, "PC66": 0.10193, "PC318": -0.0507, "PC319": 0.06267, "PC520": -0.00948, "PC84": 0.0347, "PC83": 0.21009, "PC82": 0.00622, "PC81": -0.16235, "PC80": -0.3582, "PC310": 0.05539, "PC311": 0.0015, "PC312": 0.05801, "PC313": 0.04566, "PC314": 0.0897, "PC315": -0.05835, "PC316": 0.0389, "PC317": 0.01199, "PC87": 0.0381, "PC86": 4e-05, "PC541": 0.0037, "PC611": 0, "PC610": 0, "PC613": 0, "PC612": 0, "PC615": 0, "PC614": 0, "PC617": 0, "PC616": 0, "PC619": 0, "PC618": 0, "PC540": -0.00083, "PC169": 0.03818, "PC168": -0.02015, "PC167": -0.03828, "PC166": 0.01764, "PC165": -0.25551, "PC164": 0.02672, "PC163": -0.12418, "PC162": 0.09232, "PC161": 0.0532, "PC160": 0.05935, "PC369": -0.06074, "PC368": 0.05102, "PC365": 0.06832, "PC364": 0.00302, "PC367": 0.02593, "PC366": 0.04913, "PC361": -0.06195, "PC360": 0.01898, "PC363": 0.03689, "PC362": -0.08502, "PC89": 0.0441, "PC88": 0.10904, "PC530": 0.00184, "PC531": -0.00132, "PC532": -0.00207, "PC533": 0.00032, "PC534": -0.0026, "PC535": 0.00464, "PC536": -0.00707, "PC537": 0.00079, "PC538": -5e-05, "PC539": 0.0027, "PC439": 0.03536, "PC438": 0.04525, "PC431": 0.00107, "PC430": -0.0386, "PC433": -0.02673, "PC432": -0.00799, "PC435": -0.01959, "PC434": -0.03489, "PC437": -0.00118, "PC436": 0.01551, "PC185": -0.05337, "PC184": -0.01298, "PC187": -0.0302, "PC186": 0.11656, "PC181": 0.05174, "PC180": -0.05343, "PC183": 0.02801, "PC182": 0.04176, "PC189": -0.00974, "PC188": 0.04895, "PC545": -0.00012, "PC544": 0.00203, "PC547": -0.00062, "PC546": 0.00104, "PC228": 0.0523, "PC229": 0.12079, "PC543": 0.00086, "PC542": -0.00178, "PC224": 0.03592, "PC225": 0.0879, "PC226": 0.08224, "PC227": 0.0503, "PC220": 0.08227, "PC221": 0.01417, "PC222": 0.07476, "PC223": -0.03199, "PC50": -0.09492, "PC51": 0.01215, "PC52": 0.32354, "PC53": -0.15548, "PC54": 0.28744, "PC55": -0.28549, "PC56": 0.16144, "PC57": -0.51051, "PC58": -0.28637, "PC59": -0.07355, "PC99": -0.18784, "PC321": 0.01487, "PC320": 0.01043, "PC323": 0.0419, "PC322": -0.0129, "PC325": -0.05315, "PC324": -0.00858, "PC327": 0.01857, "PC326": 0.01134, "PC329": 0.0481, "PC328": -0.10739, "PC642": 0, "PC488": -0.00627, "PC489": 0.00576, "PC480": -0.00288, "PC481": 0.03366, "PC482": 0.01996, "PC483": 0.00726, "PC484": -0.00878, "PC485": -0.0048, "PC486": -0.01944, "PC487": -0.02148, "PC134": -0.0338, "PC135": -0.10992, "PC136": 0.08446, "PC137": 0.10144, "PC130": 0.04197, "PC131": 0.03073, "PC132": -0.19713, "PC133": 0.00449, "PC138": -0.00624, "PC139": -0.17952, "PC640": 0, "PC641": 0, "PC569": 0, "PC568": 0, "PC570": 0, "PC571": 0, "PC621": 0, "PC558": 0, "PC518": -0.0023, "PC260": -0.03078, "PC261": 0.09154, "PC262": -0.02646, "PC263": 0.11998, "PC264": 0.01038, "PC265": 0.04205, "PC266": 0.00339, "PC267": -0.02907, "PC268": -0.06851, "PC269": -0.08861, "PC466": 0.0138, "PC467": -0.00415, "PC464": -0.00801, "PC465": -0.00579, "PC462": -0.00642, "PC463": -0.01395, "PC460": -0.00165, "PC461": -0.01447, "PC501": -0.00512, "PC500": 0.00161, "PC503": -0.00245, "PC502": 0.0087, "PC505": 0.01437, "PC504": 0.0138, "PC468": -0.00011, "PC469": -0.01536, "PC510": -0.00832, "PC511": 0.00088, "PC98": -0.24738, "PC215": 0.03024, "PC214": -0.01895, "PC217": 0.02984, "PC216": 0.04322, "PC211": 0.00299, "PC210": -0.08888, "PC213": 0.03243, "PC212": 0.01252, "PC219": -0.00659, "PC218": 0.0115, "PC602": 0, "PC603": 0, "PC600": 0, "PC601": 0, "PC606": 0, "PC607": 0, "PC604": 0, "PC605": 0, "PC608": 0, "PC609": 0, "PC178": 0.13574, "PC179": 0.14944, "PC170": 0.02478, "PC171": 0.0133, "PC172": -0.02336, "PC173": -0.16465, "PC174": 0.06454, "PC175": -0.04141, "PC176": -0.05478, "PC177": -0.01943, "PC378": -0.02186, "PC379": 0.00232, "PC376": 0.09315, "PC377": 0.07764, "PC374": -0.02662, "PC375": -0.01417, "PC372": 0.04878, "PC373": 0.00568, "PC370": -0.07867, "PC371": 0.01388, "PC92": -0.11035, "PC93": -0.08297, "PC109": -0.15727, "PC108": -0.01346, "PC105": 0.17392, "PC104": -0.39938, "PC107": -0.0309, "PC106": 0.07547, "PC101": 0.11683, "PC100": 0.2178, "PC103": 0.11055, "PC102": -0.01503, "PC561": 0, "PC428": -0.03048, "PC429": 0.01201, "PC422": -0.00019, "PC423": -0.00556, "PC420": 0.02788, "PC421": -0.01742, "PC426": -0.00894, "PC427": 0.01501, "PC424": 0.04366, "PC425": -0.01386, "PC196": 0.08742, "PC197": 0.0562, "PC194": 0.02696, "PC195": 0.03802, "PC192": -0.11544, "PC193": -0.06581, "PC190": 0.02556, "PC191": 0.04423, "PC198": -0.01251, "PC199": -0.08449}']]
        show_doc(self.test_scenario6, examples)
        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            source_create.i_update_source_with(self, example[4])
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            pca_create.i_create_a_pca_with_params(self, example[6])
            pca_create.the_pca_is_finished_in_less_than(self, example[3])
            projection_create.i_create_a_projection(self, example[5])
            projection_create.the_projection_is(self, example[7])
            compare_predictions.create_local_pca(self)
            compare_predictions.i_create_a_local_projection(self, example[5])
            compare_predictions.the_local_projection_is(self, example[7])
