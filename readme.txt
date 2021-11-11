Triangulated Irregular Network -- TIN
    
    Step 1: Converting input into MATLAB vectors using Python

        Place your input in a file named 'input.txt' in the same folder as
        your parseInputTIN.py file.

        Run the file parseInputTIN.py and it will output MATLAB vectors in
        outputTIN.txt

    Step 2: Creating TIN MLPQ
    
        Run TINFunction.m in MATLAB and copy x, y, z from outputTIN and put them
        in the MATLAB workspace

        >>> x = [0, 5, ...]

            x =
            0
            5
            ...

        >>> y = [10, 7, ...]

            y =
            10
            7
            ...

        >>> z = [9915, 10040, ...]

            z =
            9915
            10040
            ...

        Then run TINFunction with x, y, z as inputs

        >>> TINFunction(x, y, z)

        This will output a 'result.txt' file that can be imported into MLPQ and will
        give you a TIN table.