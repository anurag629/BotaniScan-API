from transformers import pipeline

pipe = pipeline("image-classification", "anurag629/swin-tiny-patch4-window7-224-finetuned-eurosat")

def getPrediction(image):
    '''
    Returns the prediction of the image.
    '''
    return pipe(image)