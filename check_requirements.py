def check_and_install(modules=[]):
    from subprocess import check_call
    check_call(['pip', 'install', 'importlib'])
    import importlib

    for dependency in modules:
        try:
            try:
                importlib.util.find_spec(dependency)
            except AttributeError:
                importlib.find_loader(dependency)
            print(f'{dependency} is installed.')
        except ImportError:
            check_call(['pip', 'install', '-r', 'requirements.txt'])