import logging
import os
import subprocess

from elemeno_ai_sdk.ml.conversion.dlc_conversion.commands.interface.command import Command
from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class QuantizeDLCCommand(Command):
    """
    Quantize the DLC model
    """

    quantizing_process: subprocess.CompletedProcess

    def __init__(self, model: Model) -> None:
        """
        Initialize the command

        Args:
            model (Model): model object
        """
        super().__init__(model)

    def execute(self) -> None:
        """
        Execute the command
        """
        model_path = self.model.out_path()

        quantized_path = ".".join(model_path.split(".")[:-1]) + "quantized.dlc"

        shell_command = (
            "snpe-dlc-quantize --input_dlc "
            + model_path
            + " --input_list "
            + str(self.model.config.get("input_list"))
            + " --output_dlc "
            + quantized_path
        )
        self.completed_process = subprocess.run(
            shell_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True
        )

        if self.completed_process.returncode != 0:
            logging.error(self.completed_process.stdout)
        else:
            logging.info(self.completed_process.stdout)
