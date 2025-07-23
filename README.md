# Compare-Faces

 This project has three uploaded models: 
1. `face_noface`
2. `humanfaces`
3. `comparenet`

## Face_NoFace

### Desciption

This is **classification network**, so it can tell if there is a face or something else (not face). It is trained and validated on about 200k images of human faces from [VGGFace2](https://www.kaggle.com/datasets/hearfool/vggface2) and [WIDER FACE](https://shuoyang1213.me/WIDERFACE/).

### Examples

<div style="display:flex; flex-direction:row;align-items:flex-start;">
    <img alt="77%example" src="./images/randguy.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
    <img alt="99%example" src="./images/me31.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
    <img alt="faceimage3" src="./images/RONALDOTHEGOAT.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
</div>

### Installation & Usage

I will use [Nvidia Jetson Orin Nano](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/) for running Face_NoFace model.

1. Download Face_NoFace from [here](https://github.com/IskDava/Compare-Faces/releases/tag/Face_NoFace_v1.0.0)
2. Move to your classification folder:
```Bash
cd ~/jetson-inference/python/training/classification
```
3. Put them in folder one folder (e.g. face_noface)<br>
You should have something like this:
```
classification/
...
├── face_noface (or any other name)/
│   ├── labels.txt
│   └── model.onnx
├── image.jpg
...
```
4. Now we will start our model. You should write this into terminal:
```Bash 
imagenet.py \ 
  --model=face_noface/model.onnx \ # showing where is face_noface model
  --labels=face_noface/labels.txt \ # showing where are labels
  --input_blob=input_0 \ 
  --output_blob=output_0 \ 
  image.jpg \ # or any other name where are your image 
  output.jpg # where you want to put new image
```
5. Congrats! Your new image is `output.jpg`.

### Possible issues

Network is trained for cropped faces, so if they are far away or there are some other items, it may mistake. Also it can't work with some types of images like .webp

## HumanFaces

### Description

This is **detection network** that can see faces, so it will highlight all of them. It is trained on about 20k photos from [Open Images (Human faces class)](https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=detection&c=%2Fm%2F0dzct) 

### Examples

<div style="display:flex; flex-direction:row;align-items:flex-start;">
    <img alt="77%example" src="./images/grandpaout.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
    <img alt="99%example" src="./images/ron1.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
    <img alt="faceimage3" src="./images/ron2.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
</div>


### Installation & Usage

This guide be a bit simillar to `Face_NoFace`'s one.

1. Download HumanFace from [here](https://github.com/IskDava/Compare-Faces/releases/tag/HumanFacesv1.0.0)

2. Move to your classification folder:
```Bash
cd ~/jetson-inference/python/training/detection/ssd
```
3. Put them in folder one folder (e.g. face_noface)<br>
You should have something like this:
```
ssd/
...
├── HumanFaces/
│   ├── labels.txt
│   └── model.onnx
├── image.jpg
...
```
4. Now we will start our model. You should write this into terminal:
```Bash 
detectnet \ 
  --model=models/humanfaces/ssd-mobilenet.onnx \ # showing where is the model         
  --labels=models/humanfaces/labels.txt  \ # showing labels
  --input-blob=input_0  \ # telling input type
  --output-cvg=scores  \ 
  --output-bbox=boxes \ # telling output type
  input.jpg \ # input (can be video as well)
  output.jpg # output
```
5. Congrats! Your new image is `output.jpg`.

### Possible issues

Like other models this model can't work with some types of images like .webp


## CompareNet

This isn't my own network, I did it with [`face_recognition`](https://github.com/ageitgey/face_recognition) python's library. Here you can compare images with faces and programm will return if they are same or not and its confidence.

## Examples

<div style="display:flex; flex-direction:row;align-items:flex-start;">
    <img alt="77%example" src="./images/dos.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
    <img alt="99%example" src="./images/me31.jpg" style="flex: 1 1 200px; width: auto; height: 200px; object-fit: contain;">
</div>

<div style="text-align:center; margin-top: 10px;">
    <img alt="result: 98%" src="./images/comparenet_results.png">
</div>

## Installation & Usage

This quide is much easier and prettier than others.

1. Install CompareNet from [here](https://github.com/IskDava/Compare-Faces/releases/tag/CompareNetv1.0.0)

2. Install all essential libraries:
```Bash
pip install -r requirements.txt # installing everything that is writen in requirements (pip will understnd it by him self)
```

3. Now run the CompareNet like that:
```Bash
python comparenet.py face1.jpg face2.jpg # face1 and face2 are your own images
```

## Possible issues

`face_recognition`'s network is trained on faces in good quality. Also it can work worse with faces that are far away.

---
### Resources

- Cao, Qiong, Li Shen, Weidi Xie, Omkar M. Parkhi, и Andrew Zisserman. 2017. “VGGFace2: A Dataset for Recognising Faces across Pose and Age.” arXiv, October 23. https://arxiv.org/abs/1710.08092 
arXiv

- Yang, Shuo, Ping Luo, Chen Change Loy, и Xiaoou Tang. 2015. “WIDER FACE: A Face Detection Benchmark.” arXiv, November 20. https://arxiv.org/abs/1511.06523 
arXiv

- Kuznetsova, Alina, Hassan Rom, Neil Alldrin, Jasper Uijlings, Ivan Krasin, Jordi Pont‑Tuset, Shahab Kamali, Stefan Popov, Matteo Malloci, Alexander Kolesnikov, Tom Duerig, и Vittorio Ferrari. 2020. “The Open Images Dataset V4: Unified Image Classification, Object Detection, and Visual Relationship Detection at Scale.” International Journal of Computer Vision 128, no. 7 (март): 1956–81. https://doi.org/10.1007/s11263-020-01316-z

- Geitgey, Adam. 2020. «face-recognition.» Python package version 1.3.0. https://pypi.org/project/face-recognition/