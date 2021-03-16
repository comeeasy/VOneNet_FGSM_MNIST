# FGSM_MNIST

We're trying to make model better which is robust against to adversarial images, especially made by FGSM.
Yann LeCun's MNIST datasets are used.

We're inspired by this [tutorial](https://www.pyimagesearch.com/2021/03/08/defending-against-adversarial-image-attacks-with-keras-and-tensorflow/).

A function named
  generate_image_adversarial(args) is just interpretation of tensorflow code of above tutorial

## Results
1. 1-layer-linear-classifier model
<br><img src="https://github.com/comeeasy/FGSM_MNIST/blob/main/report/1-layer-MNIST-epochs-100.png" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br>


## Requirements

- python 3.8+
- pytorch 0.4.1+
- numpy
- tqdm

## License

MIT License

## trained model

| Name     | Description                                                              |
| -------- | ------------------------------------------------------------------------ |
| 1-layer-linear-classifier | really simple model                                     |
| 3-layer-linear-classifier | add two layer to 1-layer simple model                   |
| Convnet                   | simple convolutional model                              |

## Longer Motivation

1. VOneNet maybe boosts performance. So we're considering how apply this model
[VOneNet](https://github.com/dicarlolab/vonenet)
