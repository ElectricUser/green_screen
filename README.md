Simple python script for green screening (Chroma keying)

Input can be a video, or a camera (if you want a camera pass 0 to VideoCapture); 
Outputs a video where every green pixel is substituted by another media (in this case an image but can be a video aswell for example);
Uses HSV color space to deal with ilumination problems;
