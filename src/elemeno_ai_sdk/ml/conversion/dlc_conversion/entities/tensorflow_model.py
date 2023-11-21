import logging
from typing import Dict, Union

import tensorflow as tf

from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class TensorflowModel(Model):
    """
    Class for Tensorflow model
    """

    command: str
    path: str
    config: Dict[str, str]

    def __init__(self, path: str, config: Dict[str, Union[str, Dict[str, str]]]) -> None:
        """
        Initialize the Tensorflow model

        Args:
            path (str): path of the model
            config (Dict[str, Union[str, Dict[str, str]]]): model config and options
        """
        super().__init__("tensorflow", path, config)

    def validate(self) -> None:
        """
        Validate the model

        Raises:
            Exception: if validation fails
        """
        try:
            tf.keras.models.load_model(self.path)
        except Exception as e:
            logging.error("Invalid Tensorflow model: " + str(e))

    def initialize(self) -> None:
        """
        Initialize the model command
        """

        output_path = super().out_path()

        input_dim = self.config.get("input_dim")
        dimensions = ""
        for key, value in input_dim.items():
            dimensions += " -d " + key + " " + value

        out_nodes = self.config.get("out_nodes")
        nodes = ""
        for node in out_nodes:
            nodes += " --out_node " + node

        self.command = "snpe-tensorflow-to-dlc -i " + self.path + dimensions + " -o " + output_path + nodes
