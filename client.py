haha=123
import requests  # calling web service
import json # relational-object mapping

import uuid
import pathlib
import logging
import sys
import os
import base64

from configparser import ConfigParser

import matplotlib.pyplot as plt
import matplotlib.image as img
def add_user(data,baseurl=haha):

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

        if res.status_code == 400:  # we'll have an error message
            body = res.json()
            userid = body["userid"]
            message = body["message"]
            return([False,{'userid':userid,'messgae':message}])
        if res.status_code == 200:
            body = res.json()
            userid = body["userid"]
            message = body["message"]
            return([True,{'userid':userid,'messgae':message}])

    except Exception as e:
        logging.error("add_user() failed:")
        logging.error("url: " + url)
        logging.error(e)
        return

def login(data, baseurl):
    try:
        url = baseurl + '/login'
        res = requests.get(url, json=data)

        if res.status_code == 200:
            body = res.json()
            return [True, body]
        else:
            return [False, {"message": "Login Failed ,Wrong username or password"}]
    except Exception as e:
        logging.error("login() failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def search_film(data, baseurl):
    try:
        url = baseurl + '/search_film'
        res = requests.get(url, json=data)
        if res.status_code == 200:
            body = res.json()
            data =body["data"]
            return [True, data]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]


def add_review(data,baseurl):

    local_filename = data['filename']

    if not pathlib.Path(local_filename).is_file():
        message ="Local file '", local_filename, "' does not exist..."
        return [False,{"message":message}]

    try:
        infile = open(local_filename, "rb")
        bytes = infile.read()
        infile.close()
        image = base64.b64encode(bytes)
        image_str = image.decode()

        api = '/add_review'
        url = baseurl + api
        data_ = {'userId': data["userId"],'movieId':data['movieId'],'rate':data['rate'],'reviewContent':data['reviewContent']
                 ,'image_Uploaded':data['image_Uploaded'],'image':image_str}
        res = requests.post(url, json=data_)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]

    except Exception as e:
        logging.error("upload() failed:")
        logging.error("url: " + url)
        logging.error(e)
        return


def like_review(data, baseurl):
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
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def unlike_review(data, baseurl):
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
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]


def favorite_movie(data, baseurl):
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
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def infavorite_movie(data, baseurl):
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
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def my_favorite(data,baseurl):
    try:
        url = baseurl + '/my_favorite'
        res = requests.get(url, json=data)
        if res.status_code == 200:
            body = res.json()
            return [True, {"message": body["message"],"data":body["data"]}]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]



def checkimage_exist(userid, reviewid):
    # Construct the image file name
    imagename = f"{userid}_{reviewid}.png"

    # Define the path to the images folder relative to the current directory
    image_folder_path = os.path.join(os.getcwd(), "images")

    # Construct the full path to the image file
    image_path = os.path.join(image_folder_path, imagename)

    # Check if the image file exists and return the result
    return os.path.exists(image_path)

def movie(data,baseurl):
    try:
        url = baseurl + '/movie'
        res = requests.get(url, json=data)
        if res.status_code == 200:
            body = res.json()
            return [True, body['message']]
        else:
            body = res.json()
            return [False, {"message": body["message"]}]
    except Exception as e:
        logging.error("search_file failed:")
        logging.error("url: " + url)
        logging.error(e)
        return [False, {"message": "Request failed"}]

def my_like(data,baseurl):
    return
def my_review(data,baseurl):
    return