from clodsa.augmentors.augmentorFactory import createAugmentor
from clodsa.transformers.transformerFactory import transformerGenerator
from clodsa.techniques.techniqueFactory import createTechnique

PROBLEM = "instance_segmentation"

ANNOTATION_MODE = "coco"
INPUT_PATH = "rotation_augmented"
GENERATION_MODE = "linear"
OUTPUT_MODE = "coco"
OUTPUT_PATH = "effects_augmented/"

augmentor = createAugmentor(PROBLEM, ANNOTATION_MODE, OUTPUT_MODE, GENERATION_MODE,
                            INPUT_PATH, {"outputPath": OUTPUT_PATH})

transformer = transformerGenerator(PROBLEM)

none = createTechnique("none", {})
augmentor.addTransformer(transformer(none))

dropout = createTechnique("dropout", {"percentage": 0.1})
augmentor.addTransformer(transformer(dropout))

histogram = createTechnique("equalize_histogram", {})
augmentor.addTransformer(transformer(histogram))

gamma = createTechnique("gamma", {"gamma": 2.0})
augmentor.addTransformer(transformer(gamma))

shearing = createTechnique("shearing", {"a": 0.4})
augmentor.addTransformer(transformer(shearing))

saturation = createTechnique("raise_saturation", {"power": 2.0})
augmentor.addTransformer(transformer(saturation))

hue = createTechnique("raise_hue", {"power": 1.5})
augmentor.addTransformer(transformer(hue))

gamma_dark = createTechnique("gamma", {"gamma": 0.3})
augmentor.addTransformer(transformer(gamma_dark))

blur = createTechnique("blurring", {"ksize": 5})
augmentor.addTransformer(transformer(blur))

augmentor.applyAugmentation()
