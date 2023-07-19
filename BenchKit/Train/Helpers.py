import os.path
from pathlib import Path
from accelerate import Accelerator
from BenchKit.Data.Helpers import remove_all_temps


def data_loading(acc: Accelerator):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            return fun(*args, **kwargs)
        wipe_temp(acc)
        acc.free_memory()

        return wrapper

    return decorator


def wipe_temp(acc: Accelerator):
    acc.wait_for_everyone()
    remove_all_temps()
    acc.wait_for_everyone()


def write_script():
    template_path = Path(__file__).resolve().parent / "TrainScript.txt"

    if not os.path.isfile("TrainScript.py"):
        with open(template_path, "r") as read_file:

            with open("TrainScript.py", "w") as file:
                line = read_file.readline()
                while line:
                    file.write(line)
                    line = read_file.readline()
