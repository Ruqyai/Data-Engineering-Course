# Tuwaiq_Academy
 
<table class="tg">
    <tr>
        <th class="tg-yw4l"><b>Day</b></th>
        <th class="tg-yw4l"><b>Slides</b></th>
        <th class="tg-yw4l"><b> Examples </b></th>
    </tr>
    <tr>
        <td class="tg-yw4l"> Day#1 </td>
        <td class="tg-yw4l"> <a href="https://bit.ly/DE_Slide1">Slides</a> </td>
        <td class="tg-yw4l">
            <a href="https://github.com/Ruqyai/Tuwaiq_Academy/blob/main/Jupyter/Colab/PySpark_On_Colab.ipynb">
                <img src="https://colab.research.google.com/assets/colab-badge.svg">
            </a>
        </td>
    </tr>
    <tr>
        <td class="tg-yw4l"> Day#2 </td>
        <td class="tg-yw4l"><a href="https://bit.ly/3M6etal">Slides </a></td>
        <td class="tg-yw4l">
            <a href="https://github.com/Ruqyai/Tuwaiq_Academy/blob/main/Jupyter/Colab/Kafka_on_Colab.ipynb">
                <img src="https://colab.research.google.com/assets/colab-badge.svg">
            </a>
            <a href="https://github.com/Ruqyai/Tuwaiq_Academy/blob/main/Jupyter/Colab/MongoDB_on_Colab.ipynb">
                <img src="https://colab.research.google.com/assets/colab-badge.svg">
                <a href="https://github.com/Ruqyai/Tuwaiq_Academy/blob/main/Jupyter/Colab/Dash_on_colab.ipynb">
                    <img src="https://colab.research.google.com/assets/colab-badge.svg">
                </a>
            </a>
        </td>
    </tr>
    <tr>
        <td class="tg-yw4l"> Day#3 </td>
        <td class="tg-yw4l"><a href="https://bit.ly/3CdN6GL"> Slides </a></td>
        <td class="tg-yw4l"><a href="https://github.com/Ruqyai/Tuwaiq_Academy/blob/main/Docker-compose.yml"> Project on Docker</a> or 
        <a href="https://github.com/Ruqyai/Tuwaiq_Academy/blob/main/Jupyter/Colab/Final_Project_on_Colab.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg"></a>
        </td>
    </tr>
</table>

![Dashbord](https://raw.githubusercontent.com/Ruqyai/publish/master/screenshots/dash/9.gif)

## First Day

#### Reivew the [Slides](https://bit.ly/DE_Slide1)   

#### Command to run Just jupyter docker image  

```bash
docker compose up jupyter   
```  

* Copy the token value in the terminal   
* Open the browser    
[http://localhost:10100 ](http://localhost:10100/)  
* Paste it in login field
![Dashbord](https://raw.githubusercontent.com/Ruqyai/publish/master/screenshots/dash/1.jpg)
## Second Day 


#### Reivew the [Slides](https://bit.ly/3M6etal)   

## Third day

#### Reivew the [Slides](https://bit.ly/3CdN6GL)  
![Dashbord](https://raw.githubusercontent.com/Ruqyai/publish/master/screenshots/dash/2.jpg)

#### Commands of docker compose

* build the docker image
```bash
docker compose build  
```  
* run all 

```bash
docker compose up  
```  
* stop and remove all 

```bash
docker compose down 
```  
* clean 
```bash
docker volume rm $(docker volume ls -q)
docker image rm $(docker image ls -q)
docker system prune
```  
