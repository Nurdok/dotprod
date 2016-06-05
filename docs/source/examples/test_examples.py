import json
import pytest
import pathlib
import jsonschema

this_dir = pathlib.Path(__file__).parent
positive_examples = this_dir / 'positive'
negative_examples = this_dir / 'negative'
schema_path = this_dir / '..' / '..' / '..' / 'prod.json'


@pytest.mark.parametrize("example_path", positive_examples.rglob('*.prod'))
def test_positive_examples(example_path):
    with schema_path.open('rt') as schema_file:
        schema = json.load(schema_file)

    with example_path.open('rt') as example_file:
        example = json.load(example_file)

    jsonschema.validate(example, schema)


@pytest.mark.parametrize("example_path", negative_examples.rglob('*.prod'))
def test_negative_examples(example_path):
    with schema_path.open('rt') as schema_file:
        schema = json.load(schema_file)

    with example_path.open('rt') as example_file:
        example = json.load(example_file)

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(example, schema)
