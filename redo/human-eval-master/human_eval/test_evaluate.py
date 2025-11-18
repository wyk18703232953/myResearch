from data import write_jsonl, read_problems
from openai import OpenAI
from execution import evaluate_functional_correctness
import os

problems = read_problems()
  

evaluate_functional_correctness()