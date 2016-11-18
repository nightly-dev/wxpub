#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint,request,url_for,render_template, make_response
from pymongo import *
import datetime
import random
import time

jsmm = Blueprint('jsmm', __name__,
                        template_folder='templates')

@jsmm.route('/jsmm')
def get_mm_images():
    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc

    images = mmc.find(sort=[('_id', DESCENDING)], limit=15)
    imgs = list(images)
    covers = [random.sample(img['alias'], 1)[0] for img in imgs]
    dts = [time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(img['record'])) for img in imgs]
    sources = [img['source'] for img in imgs]
    resp =make_response(render_template('jsmm.tpl', images=imgs, covers=covers, dts=dts, sources=sources))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

@jsmm.route('/immall')
def get_mm_all_images():
    key = request.args.get('key')

    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc

    images = mmc.find({'img':key}, limit=1)
    
    if not images.count():
        return 'not found'
    aliaslist = images[0]['alias']
    alt = images[0]['alt']
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(images[0]['record']))
    source = images[0]['source'] if 'source' in images[0].keys() else '99mm'

    resp = make_response(render_template('mmlist.tpl', aliaslist=aliaslist, dt=dt, alt=alt, source=source))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

