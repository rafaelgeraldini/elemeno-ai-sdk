
DLC Model Conversion Tool
===========

Installation
------------

1 Obtaining the SNPE SDK
^^^^^^^^^^^^^^^^^^^^^^^

Before any preparation, it is necessary to obtain the Qualcomm Neural Processing SDk from `Qualcomm Neural Processing SDK <https://developer.qualcomm.com/software/qualcomm-neural-processing-sdk>`_. Users should register on the Qualcomm platform and download the version necessary for the used OS following the correct instructions.

2 Preparing Environment
^^^^^^^^^^^^^^^^^^^^^^^

For correct execution of the system, an environment with Python 3.8.* must be installed. For validating all Linux dependencies are available the script provided by the SDK can be used:

.. code-block:: shell

   sudo /path/to/sdk/bin/check-linux-dependency.sh

Some python libraries are also necessary, a script is also provided, and can be executed by:

.. code-block:: shell

   python /path/to/sdk/bin/check-python-dependency

Using the Conversion Tool
---------------------

Import modules
^^^^^^^^^^^^^^

For using the Conversion Tool the user must import the class "DLCConverter":

.. code-block:: python

   from elemeno_ai_sdk.ml.conversion.dlc_converter import DLCConverter

Initialize the converter
^^^^^^^^^^^^^^^^^^^^^^^^

The converter requires the path for the SNPE SDK, path of the model to be converted and a options dictionary to be passed to it constructor and can be initialized by:

.. code-block:: python

   converter = DLCConverter("/path/to/sdk","/path/to/model", config_dict)

User can also pass the argument "quantize" to the constructor, if the model should be quantized. The default value is False."

Model Options and Specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The converter has some options that can be set by the user, some are equal for all flavours and some are specific. The options should be set on a single dictionary and passed to the converter.

Common Options
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - **Key**
     - **Value**
     - **Required**
   * - output_path
     - String - Path to output directory
     - True
   * - input_list
     - String - Path to txt with input data formated to SDK
     - If Quantize And/Or Run Validator


Onnx Options
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - **Key**
     - **Value**
     - **Required**
   * - input_dim
     - Dict(string:String) - Name and dimension of input layers
     - If model with Dynamic Batch Size


Pytorch Options
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - **Key**
     - **Value**
     - **Required**
   * - input_dim
     - Dict(string:String) - Name and dimension of input layers
     - True


Tensorflow Options
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - **Key**
     - **Value**
     - **Required**
   * - input_dim
     - Dict(string:String) - Name and dimension of input layers
     - True
   * - out_nodes
     - Tuple(String) - Name of output nodes
     - True


Tflite Options
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - **Key**
     - **Value**
     - **Required**
   * - input_dim
     - Dict(string:String) - Name and dimension of input layers
     - True


Convert Model
^^^^^^^^^^^^^

For converting the model, the user must call the method "apply_conversion":

The method returns None. The output files will be saved on the same directory as the model.

.. code-block:: python

   converter.apply_conversion()

End-to-End Example
------------------

.. code-block:: python


   from elemeno_ai_sdk.ml.conversion.dlc_converter import DLCConverter

   config = {
    "input_dim": {
        "images": "1,3,640,640"
        }
    }

    converter =  DLCConverter("/path/to/sdk","/path/to/model", config)
    converter.apply_conversion()
