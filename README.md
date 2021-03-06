# build-simple-docker-container

## demo
[![](http://img.youtube.com/vi/bp8AXeAzQls/0.jpg)](https://youtu.be/bp8AXeAzQls "Build Docker Container Project")

## build the image
```
docker build -t nlp .
```

## rename the image to be pushed to docker hub
```
docker image tag nlp:latest yichenghuang980/container-ids-721:final
```

## push the image to dockerhub
```
docker image push yichenghuang980/container-ids-721:final
```

## login into docker hub
```
docker login --username=yourhubusername --email=youremail@company.com
```

## pull the image down
```
docker pull yichenghuang980/container-ids-721:final
```

## run the image
```
docker run -it
```

And in the prompted panel, type in whatever sentences you want to analyze and scores will be returned
