import argparse
import logging

from test_class import Test


def main(backup_dir, source_dir, dest_dir, log):
    logging.basicConfig(
        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S',
        level=logging.DEBUG)

    # this is for turning off the logging
    if log == "on":
        logging.getLogger().disabled = False
    elif log == "off":
        logging.getLogger().disabled = True
    else:
        print(log)
        raise ValueError("log option is not valid. on or off")

    logging.info('backup-dir')
    print(backup_dir)

    logging.info('source-dir')
    print(source_dir)

    logging.info('dest-dir')
    print(dest_dir)

    start = Test(backup_dir, source_dir, dest_dir)
    out = start.print_out()
    print(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Python scripts for doing the rsync link-dest job")

    parser.add_argument('-b',
                        '--backup_dir',
                        action='store',
                        type=str,
                        required=True,
                        help="backup-dir",
                        )

    parser.add_argument('-s',
                        '--source_dir',
                        action='store',
                        type=str,
                        required=True,
                        help='source-dir',
                        )
    parser.add_argument('-d',
                        '--dest_dir',
                        action='store',
                        type=str,
                        required=True,
                        help='dest-dir',
                        )

    parser.add_argument('-l',
                        '--log',
                        action='store',
                        type=str,
                        default="on",
                        help='boolean for logging',
                        )

    args = parser.parse_args()
    main(args.backup_dir, args.source_dir, args.dest_dir, args.log)
