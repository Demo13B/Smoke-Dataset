from clodsa.augmentors.augmentorFactory import createAugmentor
from clodsa.transformers.transformerFactory import transformerGenerator
from clodsa.techniques.techniqueFactory import createTechnique

PROBLEM = "instance_segmentation"

ANNOTATION_MODE = "coco"
INPUT_PATH = "flip_augmented"
GENERATION_MODE = "linear"
OUTPUT_MODE = "coco"
OUTPUT_PATH = "rotation_augmented/"

augmentor = createAugmentor(PROBLEM, ANNOTATION_MODE, OUTPUT_MODE, GENERATION_MODE,
                            INPUT_PATH, {"outputPath": OUTPUT_PATH})

transformer = transformerGenerator(PROBLEM)

none = createTechnique("none", {})
augmentor.addTransformer(transformer(none))

rotation = createTechnique("rotate", {"angle": 90})
augmentor.addTransformer(transformer(rotation))
rotation = createTechnique("rotate", {"angle": 180})
augmentor.addTransformer(transformer(rotation))
rotation = createTechnique("rotate", {"angle": 270})
augmentor.addTransformer(transformer(rotation))

augmentor.applyAugmentation()