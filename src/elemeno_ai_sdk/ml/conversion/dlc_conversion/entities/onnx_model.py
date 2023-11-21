import logging
from typing import Dict

import onnx

from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class ONNXModel(Model):
    """
    Class for ONNX model
    """

    command: str
    path: str
    config: Dict[str, str]

    def __init__(self, path: str, config: Dict[str, str]) -> None:
        """
        Initialize the ONNX model

        Args:
            path (str): path of the model
            config (Dict[str, str]): model config and options
        """
        super().__init__("onnx", path, config)

    def validate(self) -> None:
        """
        Validate the model

        Raises:
            Exception: if validation fails
        """
        try:
            onnx_model = onnx.load(self.path)
            onnx.checker.check_model(onnx_model)
        except Exception as e:
            logging.error("Invalid ONNX model: " + str(e))

    def initialize(self) -> None:
        """
        Initialize the model command
        """

        output_path = super().out_path()

        input_dim = self.config.get("input_dim")

        if input_dim is None:
            self.command = "snpe-onnx-to-dlc -i " + self.path + " -o " + output_path
        else:
            dimensions = ""
            for key, value in input_dim.items():
                dimensions += " -d " + key + " " + value
            self.command = "snpe-onnx-to-dlc -i " + self.path + dimensions + " -o " + output_path
