from .data import split_to_folders, prepare_single_client
from .config import load_config
from examples.utils.plot import display_statistics, plot_results, plot_votes
from keras_learner import KerasLearner


class Mnist:
    split_to_folders = split_to_folders
    prepare_single_client = prepare_single_client
    load_config = load_config
    display_statistics = display_statistics
    plot_results = plot_results
    plot_votes = plot_votes
    Model = KerasLearner