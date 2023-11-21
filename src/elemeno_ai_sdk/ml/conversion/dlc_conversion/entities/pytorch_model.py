import logging
from typing import Dict, Union

import torch

from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class PytorchModel(Model):
    """
    Class for Pytorch model
    """

    command: str
    path: str
    config: Dict[str, str]

    def __init__(self, path: str, config: Dict[str, Union[str, Dict[str, str]]]) -> None:
        """
        Initialize the Pytorch model

        Args:
            path (str): path of the model
            config (Dict[str, Union[str, Dict[str, str]]]): model config and options
        """
        super().__init__("pytorch", path, config)

    def validate(self) -> None:
        """
        Validate the model

        Raises:
            Exception: if validation fails
        """
        try:
            torch.load(self.path, map_location=torch.device("cpu"))
        except Exception as e:
            logging.error("Invalid Pytorch model:" + str(e))

    def initialize(self) -> None:
        """
        Initialize the model command
        """
        output_path = super().out_path()

        input_dim = self.config.get("input_dim")
        dimensions = ""
        for key, value in input_dim.items():
            dimensions += " -d " + key + " " + value

        self.command = "snpe-pytorch-to-dlc -i " + self.path + dimensions + " -o " + output_path
