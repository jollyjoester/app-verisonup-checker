#! /usr/bin/env python
# -*- coding: utf-8

import urllib.request
from bs4 import BeautifulSoup


def get_ios_app_verison():

    itunes_url = 'https://itunes.apple.com/jp/app/plantsnote-zai-peiroguwo-cansutamenoapuridesu/id604626920?mt=8'

    html = urllib.request.urlopen(itunes_url)
    soup = BeautifulSoup(html, 'lxml')

    app_version = soup.find('span', itemprop='softwareVersion')
    print(app_version.string.strip())


def get_android_app_verison():

    google_play_url = 'https://play.google.com/store/apps/details?id=jp.plantsnote.plantsnote&hl=ja'

    html = urllib.request.urlopen(google_play_url)
    soup = BeautifulSoup(html, 'lxml')

    app_version = soup.find('div', itemprop='softwareVersion')
    print(app_version.string.strip())


def main():

    get_ios_app_verison()
    get_android_app_verison()


if __name__ == '__main__':
    main()
