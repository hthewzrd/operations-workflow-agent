import os
from google.genai import types


def write_file(working_directory, file_path, content):
    # Public-safe stub: disable writing entirely
    return (
        'Error: write_file is disabled in this public version and cannot modify files.'
    )


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=(
        "DISABLED in the public version. Present only as a stub; "
        "does not actually write any files."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="(Ignored in public version) Path to the file to write.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="(Ignored in public version) Text content to write.",
            ),
        },
        required=["file_path", "content"],
    ),
)