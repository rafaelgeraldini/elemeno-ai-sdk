from elemeno_ai_sdk.ml.conversion.dlc_conversion.entities.interface.model import Model


class Command:
    def __init__(self, model: Model) -> None:
        self.model = model

    def execute(self) -> None:
        pass
