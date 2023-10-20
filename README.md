## Installation

### Create a Virtual Environment

To create a virtual environment, run the following command:

```bash
python -m venv venv
```
### Install Required Packages

Install the necessary packages listed in the requirements.txt file using the following command:
```bash
pip install -r requirements.txt
```


## Usage

To run the project, execute crc.py as follows:
```bash
python crc.py
```

## Functions

The project features eight functions, each of which shares common arguments: similarity_threshold, width, height, empty_ratio, n_iterations, and races.

- similaritycomparethreshold: Generates a graph comparing the percentage of similarity with the similarity threshold for different numbers of races while keeping the empty space constant.

- multipleraces_same_threshold: Produces images showing the initial and final states of simulations for various races, all with the same similarity threshold and empty space.

- same_threshold_different_empty: Creates a graph comparing the percentage of similarity with the percentage of empty space for different numbers of races, while maintaining the same similarity threshold.

- multipleraces_dif_threshold_cal_happiness: Generates a graph comparing the percentage of happiness with the similarity threshold for different numbers of races.

- same_threshold_different_empty_happiness: Creates a graph comparing the percentage of happiness with the percentage of empty space for different numbers of races, while keeping the similarity threshold constant.

- diff_grid_size_happiness: Generates a graph comparing grid size with the percentage of happiness for different numbers of races.

- diff_grid_size_similarity: Produces a graph comparing grid size with the percentage of similarity for different numbers of races.

- change_threshold_in_middle_fase: Generates a graph that evaluates the evolution of similarity between neighbors over the course of iterations, starting with a grid that already has segregation.