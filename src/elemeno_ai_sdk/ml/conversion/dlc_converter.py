from elemeno_ai_sdk.ml.conversion.converter import ModelConverter
from elemeno_ai_sdk.ml.conversion.dlc_conversion.DLC_model_converter import DLCModelConverter


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
        file_extension = self.model_path.split(".")[-1]
        if file_extension != "onnx":
            input_dim = list(self.config.get("input_dim").values())
            dimension = tuple(map(int, input_dim[0].split(",")))
            onnx_conversion = ModelConverter(self.model_path, dimension)
            onnx_conversion.apply_conversion()
            self.model_path = self.model_path + ".onnx"

        dlc_model_converter.run_convert("onnx", self.model_path, self.config, self.quantize)

        return
