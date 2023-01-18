import imageio
import os

def make_gif(input, output_path=None, total_duration=5, first_frame_duration=None, last_frame_duration=None):
    """
    Make an animation from set of images.
    You can pass a folder containing images, which will be sorted in alphabetical order. 
    To make a gif from a set of images in a custom order, pass a list of paths to the input argument.
    """
    images = []
    if output_path is None:
        output_path = "./animation.gif"
    if isinstance(input, str):
        paths = list(sorted(os.listdir(input)))
    elif isinstance(input, list):
        paths = input
    else:
        raise TypeError("input must be a directory or a list of paths")
    assert len(paths), "No images found in input directory, aborting"
    frame_duration = total_duration / len(paths)
    durations = [frame_duration] * len(paths)
    if first_frame_duration:
        durations[0] = first_frame_duration
    if last_frame_duration:
        durations[-1] = last_frame_duration
    for file_name in paths:
        if os.path.isfile(file_name):
            images.append(imageio.imread(file_name))
    imageio.mimsave(output_path, images, duration=durations)