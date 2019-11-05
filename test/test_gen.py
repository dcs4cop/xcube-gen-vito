import os
import unittest

from test.sampledata import create_s2plus_dataset
from xcube.core.gen.gen import gen_cube
from xcube.core.dsio import rimraf
from test.helpers import get_inputdata_path

INPUT_FILE = get_inputdata_path('s2plus-input.nc')
OUTPUT_FILE = 's2plus-output.nc'


def clean_up():
    files = [INPUT_FILE, OUTPUT_FILE]
    for file in files:
        rimraf(os.path.join('.', file))


class VitoS2PlusProcessTest(unittest.TestCase):

    def setUp(self):
        clean_up()
        dataset = create_s2plus_dataset()
        dataset.to_netcdf(INPUT_FILE)
        dataset.close()

    def tearDown(self):
        clean_up()

    # noinspection PyMethodMayBeStatic
    def test_process_inputs_single(self):
        status = process_inputs_wrapper(
            input_paths=[INPUT_FILE],
            output_path='s2plus-output.nc',
            output_writer='netcdf4',
            append_mode=False)
        self.assertEqual(True, status)


# noinspection PyShadowingBuiltins
def process_inputs_wrapper(input_paths=None,
                           output_path=None,
                           output_writer='netcdf4',
                           append_mode=False):
    return gen_cube(input_paths=input_paths,
                    input_processor_name='vito-s2plus-l2',
                    output_size=(6, 4),
                    output_region=(0.2727627754211426, 51.3291015625, 0.273336261510849, 51.329463958740234),
                    output_resampling='Nearest',
                    output_variables=[('rrs_443', None),
                                      ('rrs_665', None)],
                    output_path=output_path,
                    output_writer_name=output_writer,
                    dry_run=False,
                    monitor=None)
