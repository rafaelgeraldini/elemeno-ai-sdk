from typing import Literal, Tuple

from elemeno_ai_sdk.ml.conversion.dlc_conversion.commands.interface.command import Command
from elemeno_ai_sdk.ml.conversion.dlc_conversion.service.model_application_service import (
    ModelApplicationService,
)
from elemeno_ai_sdk.ml.conversion.dlc_conversion.service.model_domain_service import (
    ModelDomainService,
)
from elemeno_ai_sdk.ml.conversion.dlc_conversion.utils.snpe_sdk_initialize import SNPESDKInitializer


class DLCModelConverter:
    """
    This class is the entry point for the conversion tool.
    It initializes the SDK and provides the run method to start the conversion.
    """

    def __init__(self, snpe_sdk_path: str) -> None:
        """
        Initialize the SDK and the ModelApplicationService

        Args:
            snpe_sdk_path (str): path for the sdk
        """
        SNPESDKInitializer(snpe_sdk_path)
        self.model_application_service = ModelApplicationService(ModelDomainService())

    def run_convert(
        self,
        flavour: Literal["onnx", "tensorflow", "tflite", "pytorch"],
        path: str,
        config: dict,
        quantize: bool = False,
    ) -> Tuple[Command]:
        """
        Run the conversion tool

        Args:
            flavour (Literal["onnx"]): Flavour of the model
            path (str): path of model
            config (dict): Model Configuration and options
            quantize (bool, optional): Defaults to False.

        Returns:
            Tuple[Command]: Response
        """

        return_obj = tuple()

        conversion_step = self.model_application_service.convert(flavour, path, config)
        return_obj += (conversion_step,)

        if quantize:
            quantization_step = self.model_application_service.quantize(conversion_step.model)
            return_obj += (quantization_step,)

        return return_obj
