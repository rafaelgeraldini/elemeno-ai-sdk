from elemeno_ai_sdk.ml.conversion.dlc_conversion.commands.interface.command import Command
from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model
from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.onnx_model import ONNXModel
from elemeno_ai_sdk.ml.conversion.dlc_conversion.service.model_domain_service import (
    ModelDomainService,
)


FLAVOURS = {
    "onnx": ONNXModel,
}


class ModelApplicationService:
    """
    Application service for model related operations
    """

    def __init__(self, model_domain_service: ModelDomainService) -> None:
        """
        Initialize the model domain service

        Args:
            model_domain_service (ModelDomainService): Model Domain Service
        """
        self.model_domain_service = model_domain_service

    def convert(self, flavour: str, path: str, config: dict) -> Command:
        """
        Convert the model to DLC

        Args:
            flavour (str): model flavour
            path (str): model path
            config (dict): model config and options
        Returns:
            Command: Command object
        """
        model = FLAVOURS[flavour](path, config)
        command = self.model_domain_service.convert_to_dlc(model)
        command.execute()
        return command

    def quantize(self, model: Model) -> Command:
        """
        Quantize the model

        Args:
            model (Model): model object

        Returns:
            Command: Command object
        """
        command = self.model_domain_service.quantize_dlc(model)
        command.execute()
        return command
