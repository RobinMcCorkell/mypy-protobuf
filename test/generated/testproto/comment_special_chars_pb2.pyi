"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Test(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    A_FIELD_NUMBER: builtins.int
    B_FIELD_NUMBER: builtins.int
    C_FIELD_NUMBER: builtins.int
    D_FIELD_NUMBER: builtins.int
    E_FIELD_NUMBER: builtins.int
    F_FIELD_NUMBER: builtins.int
    G_FIELD_NUMBER: builtins.int
    H_FIELD_NUMBER: builtins.int
    I_FIELD_NUMBER: builtins.int
    J_FIELD_NUMBER: builtins.int
    K_FIELD_NUMBER: builtins.int
    a: typing.Text = ...
    """Ending with " """

    b: typing.Text = ...
    """Ending with "" """

    c: typing.Text = ...
    """Ending with \"\"\" """

    d: typing.Text = ...
    """Ending with \\ """

    e: typing.Text = ...
    """Containing bad escape: \\x"""

    f: typing.Text = ...
    """Containing \"\"\"" quadruple"""

    g: typing.Text = ...
    """Containing \"\"\""" quintuple"""

    h: typing.Text = ...
    """Containing \"\"\"\"\"\" sextuple"""

    i: typing.Text = ...
    """\"\"\" Multiple \"\"\" triples \"\"\" """

    j: typing.Text = ...
    """"quotes" can be a problem in comments.
    \"\"\"Triple quotes\"\"\" just as well
    """

    k: typing.Text = ...
    """\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"
    "                                              "
    " Super Duper comments with surrounding edges! "
    "                                              "
    "            Pay attention to me!!!!           "
    "                                              "
    \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"
    """

    def __init__(self,
        *,
        a : typing.Text = ...,
        b : typing.Text = ...,
        c : typing.Text = ...,
        d : typing.Text = ...,
        e : typing.Text = ...,
        f : typing.Text = ...,
        g : typing.Text = ...,
        h : typing.Text = ...,
        i : typing.Text = ...,
        j : typing.Text = ...,
        k : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["a",b"a","b",b"b","c",b"c","d",b"d","e",b"e","f",b"f","g",b"g","h",b"h","i",b"i","j",b"j","k",b"k"]) -> None: ...
global___Test = Test
