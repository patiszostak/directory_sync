import logging

# sources:
# https://stackoverflow.com/questions/7621897/python-logging-module-globally

def setup_logger():
    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)

    formating = "%(asctime)s | %(levelname)7s | %(module)10s - LINE:%(lineno)3d | %(message)s"

    logging.basicConfig(level=logging.DEBUG,
                        format=formating,
                        datefmt='%Y-%m-%d %H:%M:%S')

    logging.getLogger('').addHandler(console)
    global LOG
    LOG = logging.getLogger(__name__)