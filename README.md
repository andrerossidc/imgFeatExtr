# Image Feature Extraction Methods

This is repository of Image Feature Extraction Methods written in Python. 

This is intended to support many projects of UNESP - Itapeva.

## Usage

The following parameters have to be informed:

-p : parameters of the feature extraction method, as showed in the example section.

-i : directory of the images

-o : directory of the output. This script saves files related to the process, as described in the Additional Information section.

Thus:

python main.py -p file_of_parameters.txt -i images_directory -o output_dir

## Images format 

The images must be in the .xxx format. 

## Example of parameters file

In this example, we have three groups of features: LBP_GLCM, LBP, and GLCM, which are delimited by {}. The first one will combine features from LBP and GLCM in the same feature vector, while the others will extract only LBP and GLCM, respectively. Please, see that into each block we have the name of the respective methods (lbp and glcm). Currently, other supported methods are hog (Histogram of Oriented  Gradients).

LBP_GLCM{
lbp:
numPoints=4
radius=8
method="uniform"

glcm:
axis=[0, 0.785398]
}

LBP{
lbp:
numPoints=24
radius=8
method="uniform"
}

GLCM{
glcm:
axis=[0, 0.785398]
}

## Additional Information

This script saves the following files in the output directory:

- A .csv file, which contains the features and the class of the images;
- A .obj file, which contains the objected created for feature extraction;
- A .info file, which is a list of the images processed. 
