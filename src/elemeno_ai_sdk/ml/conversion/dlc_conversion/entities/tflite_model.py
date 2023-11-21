import logging
from typing import Dict, Union

import tensorflow as tf

from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class TFLiteModel(Model):
    """
    Class for TFLite model
    """

    command: str
    path: str
    config: Dict[str, str]

    def __init__(self, path: str, config: Dict[str, Union[str, Dict[str, str]]]) -> None:
        """
        Initialize the TFLite model

        Args:
            path (str): path of the model
            config (Dict[str, Union[str, Dict[str, str]]]): model config and options
        """
        super().__init__("tflite", path, config)

    def validate(self) -> None:
        """
        Validate the model

        Raises:
            Exception: if validation fails
        """
        try:
            interpreter = tf.lite.Interpreter(model_path=self.path)
            interpreter.allocate_tensors()
        except Exception as e:
            logging.error("Invalid TFLite model: " + str(e))

    def initialize(self) -> None:
        """
        Initialize the model command
        """

        output_path = super().out_path()

        input_dim = self.config.get("input_dim")
        dimensions = ""
        for key, value in input_dim.items():
            dimensions += " -d " + key + " " + value

        self.command = "snpe-tflite-to-dlc -i " + self.path + dimensions + " -o " + output_path
