from clodsa.augmentors.augmentorFactory import createAugmentor
from clodsa.transformers.transformerFactory import transformerGenerator
from clodsa.techniques.techniqueFactory import createTechnique

PROBLEM = "instance_segmentation"

ANNOTATION_MODE = "coco"
INPUT_PATH = "cleaned_dataset"
GENERATION_MODE = "linear"
OUTPUT_MODE = "coco"
OUTPUT_PATH = "flip_augmented/"

augmentor = createAugmentor(PROBLEM, ANNOTATION_MODE, OUTPUT_MODE, GENERATION_MODE,
                            INPUT_PATH, {"outputPath": OUTPUT_PATH})

transformer = transformerGenerator(PROBLEM)

none = createTechnique("none", {})
augmentor.addTransformer(transformer(none))

flip = createTechnique("flip", {"flip": 1})
augmentor.addTransformer(transformer(flip))

augmentor.applyAugmentation()
