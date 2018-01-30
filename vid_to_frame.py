#!/usr/bin/env python

import os
import argparse
import skvideo.io as io

if __name__ == '__main__':
    '''
    Takes an .mp4 file and splits it into constituent frames.

    By default, will create a new folder with the same name as the parent (can be overwritten with the '-O' / '--out' flag)

    E.x.
        python vid_to_frame.py small.mp4

        python vid_to_frame.py ./small.mp4 --out new_output_dir
    '''

    parser = argparse.ArgumentParser(description='Splits a video to images')

    parser.add_argument('file', metavar='f', type=str, help='the video file to split')
    parser.add_argument('-O', '--out', dest='output_dir', action='store', default=None, 
            help='desired output directory (default: creates one with same name as input file')
    args = parser.parse_args()

    filepath = os.path.abspath(args.file)
    dir_name, _ = os.path.splitext(filepath)
    filename_base , _ = os.path.splitext(os.path.basename(filepath))

    if args.output_dir is not None:
        # If the output director is specified, use that
        output_dir = os.path.abspath(args.output_dir)
    else:
        # The output directory is not specified and is the file name
        output_dir = os.path.abspath(dir_name)

    if not os.path.exists(output_dir) or not os.path.isdir(output_dir):
        # If the directory needs to be created, make it
        os.makedirs(output_dir)

    video = io.vread(filepath)

    for i, frame in enumerate(video):
        # Go frame by frame and write to file
        output_filename = os.path.join(output_dir, '{}_{}.png'.format(filename_base, i))
        io.vwrite(output_filename, frame)

