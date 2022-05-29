import os

import torch
import torchaudio


class SampleData:
    """Tutorial url: https://pytorch.org/tutorials/recipes/recipes/loading_data_recipe.html"""

    def download(
        self,
        root: str = "./",
        url: str = "http://www.openslr.org/resources/1/waves_yesno.tar.gz",
        folder_in_archive: str = "waves_yesno",
    ) -> None:
        torchaudio.datasets.YESNO(
            root=root,
            url=url,
            folder_in_archive=folder_in_archive,
            download=True,
        )
