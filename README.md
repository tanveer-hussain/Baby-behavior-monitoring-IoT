## Baby-behavior-monitoring-IoT

There are three sections in this report: <br />
I)	Development environment and pre-requisites <br />
II)	Source code  <br />
III)	Details about implemented methods and working mechanism <br />

##### I)	Development environment and pre-requisites

Python (v3.5) is used to develop the baby monitoring system. The system is developed in Spyder Integrated Development Environment (IDE). The details about libraries used in the implementation are given in <b> Table 1 </b>.  <br />

### Table 1: Description of libraries used in baby monitoring system <br />
![Table-1](https://user-images.githubusercontent.com/40714349/82876614-0957e780-9f74-11ea-932a-066b17fca0bf.JPG)

##### II)	Source code
There are total 28 files included in the package for seven implemented methods. For each method, four different type of experiments have been performed in separate scripts. Details about file names are described in <b> Table 2 </b>. <br />

### Table 2: Description of file names for each method <br />
![Source-Codes_Details](https://user-images.githubusercontent.com/40714349/82876135-466faa00-9f73-11ea-81ec-5c6ea3bf0208.JPG)

The regions of motion are encircled by one or multiple circles depending on the areas of motion in the video frames. The concept of circles (no circle, one circle, multiple circles, multiple circles with minimum overlapping) is illustrated in Fig. 1 where two consecutive frames are processed and after processing converted into binary form and then individual output is shown in the <b> Figure 1 </b>.

### Figure 1: Demonstration of concept of circles <br />
![Figure-1](https://user-images.githubusercontent.com/40714349/82877239-e37f1280-9f74-11ea-96ff-875878eb8f26.jpg)

##### a) Implementation details <br />
The working of each step along with functions used in program and its corresponding output with the name of variables are given in Table 3 which are general for all the methods. Whereas <b> Table 4 </b> demonstrates the steps distinctive for each method processing.

### Table 3: Generic steps for breathing detection of baby for all seven methods <br />
![Table-3](https://user-images.githubusercontent.com/40714349/82877842-ab2c0400-9f75-11ea-8911-2fb4ef8f2479.JPG)

### Table 4: Distinctive steps for each method <br />
![Table-4](https://user-images.githubusercontent.com/40714349/82877948-cbf45980-9f75-11ea-848b-149b258ac6ac.JPG)

##### a) How to run the program? <br />
Each script file contains a main function which includes all the programming logic defined for the baby monitoring system. Run this script and choose the input video from the file dialog box. The input parameters and description of variables are explained in <b> Table 5 </b>.

### Table 5: Description of variables of Python script <br />
![Table-5](https://user-images.githubusercontent.com/40714349/82878198-1e357a80-9f76-11ea-8f3a-6dd7ea196db1.JPG)


##### III)	Details about implemented methods and working mechanism
We have implemented seven methods for the baby monitoring system including frame difference, optical flow, background subtraction and various combination of these methods. The detailed description of all the methods is given in subsequent sections. <br />


1.	Frame difference (method 1) <br />
This method comprises of the following steps: <br />
•	Calculate pixel-wise difference between two successive frames. <br />
•	Convert the difference image into binary. <br />
•	Compute binary image to detect motion. <br />
The working mechanism of method 1 is visualized in <b> Figure 2 <\b> <br />
  
### Figure 2: Overall framework of method 1 (frame difference) <br />
![Figure-2](https://user-images.githubusercontent.com/40714349/82878539-956b0e80-9f76-11ea-9993-06267476096e.jpg)

2.	Optical flow (method 2) <br />
Optical flow motion detection technique is used to estimate the motion in two consecutive frames of video sequence as shown in <b> Figure. 3 </b>. Optical flow uses the following steps. <br />
•	Consecutive frames at time (t, t + 1) are converted into HSI color model. <br />
•	These frames are input to optical flow algorithm which detects the flow. <br />
•	Flow is converted into binary, and maximum flow regions inside binary image are selected as motion area. <br />

### Figure 3: Overall framework of method 2 (optical flow) <br />
![Figure-3](https://user-images.githubusercontent.com/40714349/82878853-09a5b200-9f77-11ea-95e4-8c9bb719ab0c.jpg)

3.	Background subtraction (method 3) <br />
Background subtraction method relies on generating a foreground mask of the object. Foreground mask is a binary image which contains those pixels that belong to the moving object or motion present in the scene. Background subtraction algorithm calculates the foreground mask by performing a subtraction between the current frame and a background model as shown in <b> Figure. 4 </b>. <br />

### Figure 4: Overall framework of method 3 (background subtraction) <br />
![Figure-4](https://user-images.githubusercontent.com/40714349/82879938-a452c080-9f78-11ea-90a4-0cabb99b20d5.jpg)


4.	Frame difference + optical flow (method 4) <br />
Method 4 is the combination of both frame difference and optical flow (method 1 and method 2). In this method, a final binary image is obtained through bitwise AND logical operation of binary images from both methods which is shown in <b> Figure. 5 </b>. <br />

### Figure 5: Overall framework of method 4 (frame difference + optical flow) <br />
![Figure-5](https://user-images.githubusercontent.com/40714349/82881968-5d19ff00-9f7b-11ea-8c71-4cbbe2977cc0.jpg)

5.	Frame difference + background subtraction (method 5) <br />
Method 5 is the combination of frame difference and background subtraction which intersects the binary image obtained from frame difference and background subtraction. Finally, it estimates the motion from the intersected binary image as visualized in <b> Figure. 6 </b>. <br />

### Figure 6: Overall framework of method 5 (frame difference + background subtraction) <br />
![Figure-6](https://user-images.githubusercontent.com/40714349/82882041-7cb12780-9f7b-11ea-947f-c6fc96c393a8.jpg)

6.	Optical flow + background subtraction (method 6) <br />
In method 6, optical flow is combined with background subtraction and estimates motion by integration of binary images obtained individually. The process flow is visualized in <b> Figure. 7 </b>.<br />

### Figure 7: Overall framework of method 6 (optical flow + background subtraction) <br />
![Figure-7](https://user-images.githubusercontent.com/40714349/82882163-acf8c600-9f7b-11ea-82c4-626c377b158c.jpg)


7.	Hybrid method (method 7) <br />
Hybrid method (method 7) is the combination of three methods i.e., frame difference, optical flow and background subtraction. The decision of “breathing” or “not breathing” of the subject is taken on the basis of all three methods. These three methods process the video independently till a binary image of estimated motion is obtained. The final binary image of each method is combined by taking logical AND of the three binary images. 
The system works as follows: It takes video as an input and reads two successive frames from the video, converts it into gray scale and apply Gaussian blur to remove noise. The noise is removed to avoid wrong decision of baby breathing because the system may detect noise as motion. Binary image of detected motion is computed by each method separately and combined by taking intersection between them. On the basis of motion present inside the combined image, breathing or not breathing of baby is decided and displayed on the corresponding video as shown in <b> Figure. 8 </b>. <br />

### Figure 8: Overall framework of method 7 (hybrid method) <br />
![Figure-8](https://user-images.githubusercontent.com/40714349/82882173-aff3b680-9f7b-11ea-8902-a1d7b057b067.jpg) <br /> <br />


# Citation
<pre>
<code>
Hussain, Tanveer, Khan Muhammad, Salman Khan, Amin Ullah, Mi Young Lee, and Sung Wook Baik. "Intelligent Baby Behavior Monitoring using Embedded Vision in IoT for Smart Healthcare Centers." Journal of Artificial Intelligence and Systems. J. Artif. Intell. Syst 1, no. 15 (2019): 2019.

</code>
</pre>

If you are interested in similar works related to Computer Vision, you may find some of my other recent papers worthy to read:

<pre>
<code>
Hussain, T., Muhammad, K., Del Ser, J., Baik, S. W., & de Albuquerque, V. H. C. (2019). Intelligent Embedded Vision for Summarization of Multi-View Videos in IIoT. IEEE Transactions on Industrial Informatics.

K. Muhammad, T. Hussain, and S. W. Baik, "Efficient CNN based summarization of surveillance videos for resource-constrained devices," Pattern Recognition Letters, 2018/08/07/ 2018

Hussain, Tanveer, Khan Muhammad, Amin Ullah, Zehong Cao, Sung Wook Baik, and Victor Hugo C. de Albuquerque. "Cloud-Assisted Multi-View Video Summarization using CNN and Bi-Directional LSTM." IEEE Transactions on Industrial Informatics (2019).

K. Muhammad, T. Hussain, M. Tanveer, G. Sannino and V. H. C. de Albuquerque, "Cost-Effective Video Summarization using Deep CNN with Hierarchical Weighted Fusion for IoT Surveillance Networks," in IEEE Internet of Things Journal.
doi: 10.1109/JIOT.2019.2950469

K. Muhammad, H. Tanveer, J. Del Ser, V. Palade and V. H. C. De Albuquerque, "DeepReS: A Deep Learning-based Video Summarization Strategy for Resource-Constrained Industrial Surveillance Scenarios," in IEEE Transactions on Industrial Informatics.
doi: 10.1109/TII.2019.2960536
keywords: {Big Data;Computer Vision;Deep Learning;Video Summarization;IIoT;Resource-Constrained Devices},
URL: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8936419&isnumber=4389054
</code>
</pre>







