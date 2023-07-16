from subprocess import check_call
check_call(['pip', 'install', 'importlib'])
import importlib

def check_and_install(modules=[]):
    for dependency in modules:
        try:
            importlib.util.find_spec(dependency)
        except:
            check_call(['pip', 'install', dependency])