﻿# Tuwaiq_Academy

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

## Second Day 


#### Reivew the [Slides](https://bit.ly/3M6etal)   


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
