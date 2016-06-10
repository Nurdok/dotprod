import json
import pathlib
import textwrap

this_dir = pathlib.Path(__file__).parent

example_file_content = textwrap.dedent("""
    {example[title]}
    =====================

    {example[description]}

    .. literalinclude:: {path}
       :language: json
""")


def generate_docs(example_path):
    with example_path.open('rt') as example_file:
        example_json = json.load(example_file)

    content = example_file_content.format(example=example_json,
                                          path=example_path)
    dest_rst = example_path.parent / '{}.rst'.format(example_path.stem)

    with dest_rst.open('wt') as rst_file:
        rst_file.write(content)


def generate_docs_for_dir(directory):
    for path in directory.glob('*.prod'):
        generate_docs(path)

