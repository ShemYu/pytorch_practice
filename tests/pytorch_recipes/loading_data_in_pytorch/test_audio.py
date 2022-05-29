import os

from src.pytorch_recipes.loading_data_in_pytorch.audio import SampleData


def test_sample_data_download():
    SampleData().download()
    assert os.path.exists("./waves_yesno/")
