import unittest

from xcube_gen_vito.iproc import init_plugin


class VitoS2PlusPluginTest(unittest.TestCase):

    # noinspection PyMethodMayBeStatic
    def test_init_plugin(self):
        # Smoke test
        init_plugin()
