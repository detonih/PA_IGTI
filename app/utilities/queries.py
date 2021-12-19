import subprocess

def execute_query(query):
  result = subprocess.call(["hive", "-e", f"{query}"])
  return result