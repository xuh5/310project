import requests  # calling web service
import json # relational-object mapping
from PyQt5.QtGui import QImage
import pathlib
import logging

import os
import base64
from configparser import ConfigParser
config_file = 'movieapp-config.ini'
configur = ConfigParser()
configur.read(config_file)
baseurl = configur.get('client', 'webservice')


def add_user(data,baseurl=baseurl):

    username = data['username']
    email = data['email']
    password = data['password']
    try:
        data = {
            "username": username,
            "email": email,
            "password": password,
        }

        api = '/add_user'
        url = baseurl + api

        res = requests.put(url, json=data)

        if res.status_code == 200:
            body = res.json()
            userid = body["userid"]
            message = body["message"]
            return([True,{'userid':userid,'message':message}])
        else:  # we'll have an error message
            body = res.json()
            userid = body["userid"]
            message = body["message"]
            return ([False, {'userid': userid, 'message': message}])

    except Exception as e:
        logging.error("add_user() failed:")
        logging.error("url: " + url)
        logging.error(e)
        return

def login(data, baseurl=baseurl):
    try:
        url = baseurl + '/login'
        res = requests.get(url, params=data)

        if res.status_code == 200:
            body = res.json()
            return [True, body]
        else:
            body = res.json()
            return [False, {"message": body['message']}]
    except Exception as e:
        logging.error("login() failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def search_film(data, baseurl=baseurl):
    try:
        url = baseurl + '/search_film'
        res = requests.get(url, params=data)
        if res.status_code == 200:
            body = res.json()
            return [True, body]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]


def add_review(data,baseurl=baseurl):
    has_image=False
    if(data['filename']):
        local_filename = data['filename']
        if not pathlib.Path(local_filename).is_file():
            message ="Local file '", local_filename, "' does not exist..."
            return [False,{"message":message}]
        has_image=True
    try:
        image_str= ""
        if(has_image):
            infile = open(local_filename, "rb")
            bytes = infile.read()
            infile.close()
            image = base64.b64encode(bytes)
            image_str = image.decode()

        api = '/add_review'
        url = baseurl + api
        data_ = {'userid': data["userid"],'movieid':data['movieid'],'rate':data['rate'],'reviewContent':data['reviewContent']
                 ,'image_Uploaded':has_image,'image':image_str}
        res = requests.post(url, json=data_)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]

    except Exception as e:
        logging.error("add_review() failed:")
        logging.error("url: " + url)
        logging.error(e)
        return


def like_review(data, baseurl=baseurl):
    try:
        url = baseurl + '/like_review'
        res = requests.post(url, json=data)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("like_review failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def unlike_review(data, baseurl=baseurl):
    try:
        url = baseurl + '/unlike_review'
        res = requests.post(url, json=data)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("unlike_review failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]


def favorite_movie(data, baseurl=baseurl):
    try:
        url = baseurl + '/favorite_movie'
        res = requests.post(url, json=data)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("favorite_movie failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def infavorite_movie(data, baseurl=baseurl):
    try:
        url = baseurl + '/infavorite_movie'
        res = requests.post(url, json=data)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("infavorite_moviesearch_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def my_favorite(data,baseurl=baseurl):
    try:
        url = baseurl + '/my_favorite'
        res = requests.get(url, params=data)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"],"data":body["data"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("my_favorite failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]


def download(reviews):
    for i in reviews:
        url = i['ImageURL']
        if url!= None and url!="":
            image = QImage()
            x= requests.get(url)
            if x.status_code!=200:
                return [False,{"message" :"download image failed"}]
            image.loadFromData(x.content)
            i['ImageURL'] = image
    return [True,{"message":"download image successfully"}]


def movie(data,baseurl=baseurl):
    try:
        url = baseurl + '/movie'
        res = requests.get(url, params=data)
        if res.status_code == 200:
            body = res.json()['data']
            result = download(body['reviews'])
            if result[0]==False:
                return [False,result[1]]
            else:
                return [True, body]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("movie failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]


def my_like(data,baseurl=baseurl):
    try:
        url = baseurl + '/my_like'
        res = requests.get(url, params=data)
        if res.status_code == 200:
            body = res.json()
            result = download(body['data'])
            if result[0] == False:
                return [False, result[1]]
            else:
                return [True, {"message": body["message"],"data":body['data']}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("my_like failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def my_review(data,baseurl=baseurl):
    try:
        url = baseurl + '/my_review'
        res = requests.get(url,params=data)
        if res.status_code == 200:
            body = res.json()
            result = download(body['data'])
            if result[0] == False:
                return [False, result[1]]
            else:
                return [True, {"message": body["message"],"data":body['data']}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("my_review failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

if __name__ == '__main__':
    #print(add_user({"username":"test1","email":"qq.com","password":"123"})) #success
    #print(login({"userid":9 ,"password":"nb666"},haha))
    #print(search_film({"genre":"","language":"English"}))
    #print(add_review({"userid": 5, "movieid": 9, "rate": 10, "reviewContent": "good","filename":""})) #success
    #print(add_review({"userid":5,"movieid":9,"rate":10,"reviewContent":"good132","filename":"C:/Users/haichen/Desktop/northwestern2023/deep learning/project-object-tracking/test.jpg"}))
    #not success
    #print(like_review({"userid":5,"reviewid":3}))
    #print(unlike_review({"userid": 5, "reviewid": 1}))
    #print(favorite_movie({"userid":5,"movieid":3}))
    #print(infavorite_movie({"userid": 5, "movieid": 9}))
    #print(my_favorite({"userid": 5}))
    print(my_like({"userid":5}))
    #print(my_review({"userid":5}))
    #print(movie({"movieid":1,"userid":5}))