import logging


class Test(object):
    def __init__(self, backup_dir, source_dir, dest_dir):
        logging.basicConfig(
            format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d:%H:%M:%S',
            level=logging.DEBUG)
        self.bak_dir = backup_dir
        self.src_dir = source_dir
        self.dest_dir = dest_dir

    def print_out(self):
        logging.info('self thing')
        return self.bak_dir + "->" + self.dest_dir
