# Pre train vgg16 model #

the pretrain vgg16 model is from Davi Frossard in his [page](1).
What I do is just wrapping it to call it more easy, and I also give relu1\_1 to relu5\_1 for transfer learning or style transfer.

## Usage ##

First, download the vgg16_weights.npz in [here](2).

    >> from vgg16 import vgg16
    >> vgg16.predict('.vgg16/Greater-Swiss-Mountain-dog.jpg')
    Greater Swiss Mountain dog 0.699447
    EntleBucher 0.176884
    Appenzeller 0.0887003
    black-and-tan coonhound 0.0218748
    Doberman, Doberman pinscher 0.00687326

[1]: http://www.cs.toronto.edu/~frossard/post/vgg16/
[2]: https://www.cs.toronto.edu/~frossard/vgg16/vgg16_weights.npz
