import logging
import os


class SNPESDKInitializer:
    """
    Initializes the SDK by setting the environment variables
    """

    def __init__(self, snpe_sdk_path: str) -> None:
        logging.info("Initializing SDK")
        os.environ["AISW_SDK_ROOT"] = snpe_sdk_path
        os.environ["SNPE_ROOT"] = snpe_sdk_path
        python_path = os.getenv("PYTHONPATH")
        if python_path is not None:
            os.environ["PYTHONPATH"] = snpe_sdk_path + "lib/python/" + ":" + python_path
        else:
            os.environ["PYTHONPATH"] = snpe_sdk_path + "lib/python/"

        path = os.getenv("PATH")
        if path is not None:
            os.environ["PATH"] = snpe_sdk_path + "bin/x86_64-linux-clang" + ":" + path
        else:
            os.environ["PATH"] = snpe_sdk_path + "bin/x86_64-linux-clang"

        ld_library = os.getenv("PATH")
        if ld_library is not None:
            os.environ["LD_LIBRARY_PATH"] = snpe_sdk_path + "lib/x86_64-linux-clang" + ":" + ld_library
        else:
            os.environ["LD_LIBRARY_PATH"] = snpe_sdk_path + "bin/x86_64-linux-clang"
