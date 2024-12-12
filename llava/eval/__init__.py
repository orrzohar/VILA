import os

from llava.utils import io

__all__ = ["EVAL_ROOT", "TASKS"]


EVAL_ROOT = "scripts/v1_5/eval"
TASKS = io.load(os.path.join(os.path.dirname(__file__), "registry.yaml"))