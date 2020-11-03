import json
from pathlib import Path
import sys

from nni.retiarii import *


json_files = [
    'mnist-tensorflow.json'
]


def test_model_load_dump():
    for json_file in json_files:
        path = Path(__file__).parent / json_file
        _test_file(path)


def _test_file(json_path):
    orig_ir = json.load(json_path.open())
    model = Model._load(orig_ir)
    dump_ir = model._dump()

    # add default values to JSON, so we can compare with `==`
    for graph_name, graph in orig_ir.items():
        if 'inputs' not in graph:
            graph['inputs'] = None
        if 'outputs' not in graph:
            graph['outputs'] = None
        for node_name, node in graph['nodes'].items():
            if 'type' not in node and 'cell' in node:
                node['type'] = '_cell'

    assert orig_ir == dump_ir


if __name__ == '__main__':
    test_model_load_dump()
