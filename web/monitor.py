#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint, redirect
from jinja2 import Environment, FileSystemLoader
import os
import commands

monitor = Blueprint('monitor', __name__,
                        template_folder='templates')

@monitor.route('/status')
def check_status():
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(THIS_DIR))
    template = env.get_template('templates/status.tpl')
    items = []
    
    result= commands.getstatusoutput('supervisorctl status wxpub')
    print result
    up = True if 'RUNNING' in result[1] else False
    it = {'service': u'公众号服务', 'up': up}
    items.append(it)
    result= commands.getstatusoutput('supervisorctl status wxschtask')
    print result
    up = True if 'RUNNING' in result[1] else False
    it = {'service': u'公众号定时推送', 'up': up}
    items.append(it)

    result= commands.getstatusoutput('curl -L --socks5 127.0.0.1:1080 --connect-timeout 10 -s -o /dev/null -I -w %{http_code} https://www.twitter.com')
    print result
    up = True if '200' in result[1] else False
    it = {'service': u'虚拟网服务', 'up': up}
    items.append(it)
    return template.render(items=items)


@monitor.route('/rebootvpn/<idx>')
def reboot_vpn(idx):
    os.system('/home/pi/www/iss/go.py %s' % idx)
    return 'ok'
