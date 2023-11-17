import logging
import os
import subprocess

from elemeno_ai_sdk.ml.conversion.dlc_conversion.commands.interface.command import Command
from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class ConvertToDLCCommand(Command):
    """
    Convert the model to DLC
    """

    completed_process: subprocess.CompletedProcess

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

        self.completed_process = subprocess.run(
            self.model.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True
        )

        if self.completed_process.returncode != 0:
            logging.error(self.completed_process.stdout)
        else:
            logging.info(self.completed_process.stdout)
