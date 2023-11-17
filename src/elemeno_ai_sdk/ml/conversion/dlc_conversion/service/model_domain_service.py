from elemeno_ai_sdk.ml.conversion.dlc_conversion.commands.convert_to_dlc_command import (
    ConvertToDLCCommand,
)
from elemeno_ai_sdk.ml.conversion.dlc_conversion.commands.interface.command import Command
from elemeno_ai_sdk.ml.conversion.dlc_conversion.commands.quantize_dlc_command import (
    QuantizeDLCCommand,
)
from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class ModelDomainService:
    """
    Domain service for model related operations
    """

    def convert_to_dlc(self, model: Model) -> Command:
        """
        Convert the model to DLC, after validating and initializing it.

        Args:
            model (Model): Model Object

        Returns:
            Command: Command object
        """
        model.validate()
        model.initialize()
        return ConvertToDLCCommand(model)

    def quantize_dlc(self, model: Model) -> Command:
        """
        Quantize the DLC model

        Args:
            model (Model): Model Object

        Returns:
            Command: Command object
        """
        return QuantizeDLCCommand(model)
