import logging
import os

from elemeno_ai_sdk.ml.conversion.dlc_conversion.DLC_model_converter import DLCModelConverter


CONVERTERS = {
    "h5": "tensorflow",
    "onnx": "onnx",
    "tflite": "tflite",
    "pt": "pytorch",
    "pth": "pytorch",
}

logging.basicConfig(level=logging.INFO)


class DLCConverter:
    """
    DLCConverter class is used to convert a model to DLC format.

    Attributes:
        snpe_sdk_path (str): Path to the SNPE SDK.
        model_path (str): Path to the model.
        config (dict): Model configuration.
        quantize (bool): Flag to quantize the model.
    """

    def __init__(self, snpe_sdk_path: str, model_path: str, config: dict, quantize: bool = False) -> None:
        self.model_path = model_path
        self.config = config
        self.quantize = quantize
        self.snpe_sdk_path = snpe_sdk_path

    def apply_conversion(self) -> None:
        """
        Converts a given deep learning model to the Deep Learning Container (DLC) format
        using the specified SDK path and configuration settings.

        :return: None
        """

        dlc_model_converter = DLCModelConverter(self.snpe_sdk_path)
        if os.path.isdir(self.model_path):
            file_extension = "h5"
        else:
            file_extension = self.model_path.split(".")[-1]

        dlc_model_converter.run_convert(CONVERTERS[file_extension], self.model_path, self.config, self.quantize)

        return
