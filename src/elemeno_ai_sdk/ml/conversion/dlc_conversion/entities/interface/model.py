class Model:
    def __init__(self, flavour: str, path: str, config: dict) -> None:
        self.flavour = flavour
        self.path = path
        self.config = config

    def validate(self) -> None:
        pass

    def initialize(self) -> None:
        pass

    def out_path(self) -> None:
        return ".".join(self.path.split(".")[:-1]) + ".dlc"
