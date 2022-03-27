from datetime import datetime, date, time
from pathlib import Path
from os.path import exists
from aiogram.types import CallbackQuery, Message
import urllib.parse
import urllib.request
import ssl
import time
import ftplib

host = 'ruvip37.hostiman.ru'
ftp_user = 's220697'
ftp_password = 'Tramadol1989!'
ftp = ftplib.FTP(host, ftp_user, ftp_password)
ftp.cwd("www/pzhtop.ru")
ftp_file = 'index.html'
local_file = r'index.html'
file = "index.html"

oper = open("system/oper.txt", "r", encoding="utf-8").read()
texx = open("system/texx.txt", "r", encoding="utf-8").read()
bbot = open("system/bbot.txt", "r", encoding="utf-8").read()
hyd = open("system/hyd.txt", "r", encoding="utf-8").read()
rab = open("system/rab.txt", "r", encoding="utf-8").read()
rabw = open("system/rabw.txt", "r", encoding="utf-8").read()
legal = open("system/legal.txt", "r", encoding="utf-8").read()
otz = open("system/otz.txt", "r", encoding="utf-8").read()

logo = f"""
        Сейчас Установленны Такие Контакты
        ----------------------------------


        1)  Оператор:        {oper}

        2)  Техподержка:     {texx}

        3)  Бот:             {bbot}

        4)  Hydra:           {hyd}

        5)  Работа:          {rab}

        6)  Работа WatsApp:  {rabw}

        7)  Legal:           {legal}

        8)  Отзывы:          {otz}
        """
def main():
    oper = open("system/oper.txt", "r", encoding="utf-8").read()
    texx = open("system/texx.txt", "r", encoding="utf-8").read()
    bbot = open("system/bbot.txt", "r", encoding="utf-8").read()
    hyd = open("system/hyd.txt", "r", encoding="utf-8").read()
    rab = open("system/rab.txt", "r", encoding="utf-8").read()
    rabw = open("system/rabw.txt", "r", encoding="utf-8").read()
    legal = open("system/legal.txt", "r", encoding="utf-8").read()
    otz = open("system/otz.txt", "r", encoding="utf-8").read()
    print(" \nОбновление Сайта Ожидай......")
    site = ('''
        <!-- saved from url=(0069)file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/index%20(3).html -->
        <html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
        <title>PZH</title>
        <meta name="og:title" content="AMAZON">
        <meta name="twitter:title" content="AMAZON">
        <meta name="og:site_name" content="AMAZON">
        <meta name="og:image" content="https://airsite.nyc3.cdn.digitaloceanspaces.com/brand/icon-256.png">
        <meta name="twitter:image" content="https://airsite.nyc3.cdn.digitaloceanspaces.com/brand/icon-256.png">
        <meta name="og:type" content="website">
        <meta name="twitter:card" content="summary">
        <link rel="shortcut icon" href="http://pzhtop.ru/null">
        <link rel="canonical" href="http://pzhtop.ru/">
        <meta name="next-head-count" content="12">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/index.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/_app.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/webpack-5247482ebcd811c9f929.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/framework.1da4ef788d111291b4b6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/commons.4cf1157854d94d82078f.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/d22e4f5c724d666750fe44516895f703072ed09f.7b1b72c2c4e99b5a67d6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/main-cb29ba5623faf6e6dfd1.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/151566a4651e83b50223f84eab66dbab6954d29f.7d68887e701c477e5f78.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <link rel="preload" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/be4ce260d173322dd4ddf7dc70532fb96bd360d4.0efdea021efae6576dac.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" as="script">
        <style>

            html,
            body,
            #__next {
            width: 100%;
            /* To smooth any scrolling behavior */
            -webkit-overflow-scrolling: touch;
            margin: 0px;
            padding: 0px;
            /* Allows content to fill the viewport and go beyond the bottom */
            min-height: 100%;
            }

            #__next {
            flex-shrink: 0;
            flex-basis: auto;
            flex-direction: column;
            flex-grow: 1;
            display: flex;
            flex: 1;
            }

            html {
            scroll-behavior: smooth;
            /* Prevent text size change on orientation change https://gist.github.com/tfausak/2222823#file-ios-8-web-app-html-L138 */
            -webkit-text-size-adjust: 100%;
            height: 100%;
            }

            body {
            display: flex;
            /* Allows you to scroll below the viewport; default value is visible */
            overflow-y: auto;
            overscroll-behavior-y: none;
            text-rendering: optimizeLegibility;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            -ms-overflow-style: scrollbar;
            }
        </style>
        <style id="react-native-stylesheet">
            [stylesheet-group="0"] {}

            html {
            -ms-text-size-adjust: 100%;
            -webkit-text-size-adjust: 100%;
            -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
            }

            body {
            margin: 0;
            }

            button::-moz-focus-inner,
            input::-moz-focus-inner {
            border: 0;
            padding: 0;
            }

            input::-webkit-inner-spin-button,
            input::-webkit-outer-spin-button,
            input::-webkit-search-cancel-button,
            input::-webkit-search-decoration,
            input::-webkit-search-results-button,
            input::-webkit-search-results-decoration {
            display: none;
            }

            [stylesheet-group="0.1"] {}

            :focus:not([data-focusvisible-polyfill]) {
            outline: none;
            }

            [stylesheet-group="0.5"] {}

            .css-4rbku5 {
            background-color: rgba(0, 0, 0, 0.00);
            color: inherit;
            font: inherit;
            list-style: none;
            margin-bottom: 0px;
            margin-left: 0px;
            margin-right: 0px;
            margin-top: 0px;
            text-align: inherit;
            text-decoration: none;
            }

            .css-18t94o4 {
            cursor: pointer;
            }

            [stylesheet-group="1"] {}

            .css-1dbjc4n {
            -ms-flex-align: stretch;
            -ms-flex-direction: column;
            -ms-flex-negative: 0;
            -ms-flex-preferred-size: auto;
            -webkit-align-items: stretch;
            -webkit-box-align: stretch;
            -webkit-box-direction: normal;
            -webkit-box-orient: vertical;
            -webkit-flex-basis: auto;
            -webkit-flex-direction: column;
            -webkit-flex-shrink: 0;
            align-items: stretch;
            border: 0 solid black;
            box-sizing: border-box;
            display: -webkit-box;
            display: -moz-box;
            display: -ms-flexbox;
            display: -webkit-flex;
            display: flex;
            flex-basis: auto;
            flex-direction: column;
            flex-shrink: 0;
            margin-bottom: 0px;
            margin-left: 0px;
            margin-right: 0px;
            margin-top: 0px;
            min-height: 0px;
            min-width: 0px;
            padding-bottom: 0px;
            padding-left: 0px;
            padding-right: 0px;
            padding-top: 0px;
            position: relative;
            z-index: 0;
            }

            .css-901oao {
            border: 0 solid black;
            box-sizing: border-box;
            color: rgba(0, 0, 0, 1.00);
            display: inline;
            font: 14px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, "Helvetica Neue", sans-serif;
            margin-bottom: 0px;
            margin-left: 0px;
            margin-right: 0px;
            margin-top: 0px;
            padding-bottom: 0px;
            padding-left: 0px;
            padding-right: 0px;
            padding-top: 0px;
            white-space: pre-wrap;
            word-wrap: break-word;
            }

            .css-9pa8cd {
            bottom: 0px;
            height: 100%;
            left: 0px;
            opacity: 0;
            position: absolute;
            right: 0px;
            top: 0px;
            width: 100%;
            z-index: -1;
            }

            [stylesheet-group="2"] {}

            .r-1udh08x {
            overflow-x: hidden;
            overflow-y: hidden;
            }

            .r-10vs3n6 {
            border-bottom-color: rgba(199, 206, 211, 1.00);
            border-left-color: rgba(199, 206, 211, 1.00);
            border-right-color: rgba(199, 206, 211, 1.00);
            border-top-color: rgba(199, 206, 211, 1.00);
            }

            .r-z2wwpe {
            border-bottom-left-radius: 4px;
            border-bottom-right-radius: 4px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            }

            .r-1phboty {
            border-bottom-style: solid;
            border-left-style: solid;
            border-right-style: solid;
            border-top-style: solid;
            }

            .r-rs99b7 {
            border-bottom-width: 1px;
            border-left-width: 1px;
            border-right-width: 1px;
            border-top-width: 1px;
            }

            [stylesheet-group="2.1"] {}

            .r-1pn2ns4 {
            padding-left: 8px;
            padding-right: 8px;
            }

            .r-oyd9sg {
            padding-bottom: 4px;
            padding-top: 4px;
            }

            [stylesheet-group="2.2"] {}

            .r-1awozwy {
            -ms-flex-align: center;
            -webkit-align-items: center;
            -webkit-box-align: center;
            align-items: center;
            }

            .r-1777fci {
            -ms-flex-pack: center;
            -webkit-box-pack: center;
            -webkit-justify-content: center;
            justify-content: center;
            }

            .r-z80fyv {
            height: 20px;
            }

            .r-19wmn03 {
            width: 20px;
            }

            .r-17bb2tj {
            -webkit-animation-duration: 0.75s;
            animation-duration: 0.75s;
            }

            .r-1muvv40 {
            -webkit-animation-iteration-count: infinite;
            animation-iteration-count: infinite;
            }

            .r-127358a {
            -webkit-animation-name: r-9p3sdl;
            animation-name: r-9p3sdl;
            }

            @-webkit-keyframes r-9p3sdl {
            0% {
                -webkit-transform: rotate(0deg);
                transform: rotate(0deg);
            }

            100% {
                -webkit-transform: rotate(360deg);
                transform: rotate(360deg);
            }
            }

            @keyframes r-9p3sdl {
            0% {
                -webkit-transform: rotate(0deg);
                transform: rotate(0deg);
            }

            100% {
                -webkit-transform: rotate(360deg);
                transform: rotate(360deg);
            }
            }

            .r-1ldzwu0 {
            -webkit-animation-timing-function: linear;
            animation-timing-function: linear;
            }

            .r-1pi2tsx {
            height: 100%;
            }

            .r-13qz1uu {
            width: 100%;
            }

            .r-2llsf {
            min-height: 100%;
            }

            .r-g6jmlv {
            width: 100vw;
            }

            .r-1mlwlqe {
            -ms-flex-preferred-size: auto;
            -webkit-flex-basis: auto;
            flex-basis: auto;
            }

            .r-417010 {
            z-index: 0;
            }

            .r-1niwhzg {
            background-color: rgba(0, 0, 0, 0.00);
            }

            .r-vvn4in {
            background-position: center;
            }

            .r-u6sd8q {
            background-repeat: no-repeat;
            }

            .r-4gszlv {
            background-size: cover;
            }

            .r-1p0dtai {
            bottom: 0px;
            }

            .r-1d2f490 {
            left: 0px;
            }

            .r-u8s1d {
            position: absolute;
            }

            .r-zchlnj {
            right: 0px;
            }

            .r-ipm5af {
            top: 0px;
            }

            .r-1wyyakw {
            z-index: -1;
            }

            .r-1loqt21 {
            cursor: pointer;
            }

            .r-1otgn73 {
            -ms-touch-action: manipulation;
            touch-action: manipulation;
            }

            .r-14lw9ot {
            background-color: rgba(255, 255, 255, 1.00);
            }

            .r-1ebgqk7 {
            bottom: 10px;
            }

            .r-14vhaug {
            box-shadow: 1px 1px 4px rgba(68, 78, 87, 0.30);
            }

            .r-18u37iz {
            -ms-flex-direction: row;
            -webkit-box-direction: normal;
            -webkit-box-orient: horizontal;
            -webkit-flex-direction: row;
            flex-direction: row;
            }

            .r-1xcajam {
            position: fixed;
            }
            ''')




    site2 = f'''
        </style>
        <script async="" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/analytics.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script>
        <script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script>
        <script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script>
        </head>
        <body style="height:100%;overflow:scroll">
            <div id="__next">
            <div class="css-1dbjc4n r-1pi2tsx r-13qz1uu">
                <div class="css-1dbjc4n r-1777fci r-2llsf r-g6jmlv">
                <div class="css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af" style="background-color:rgba(0,0,0,0.60)">
                    <div class="css-1dbjc4n r-1p0dtai r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-zchlnj r-ipm5af r-1wyyakw">
                    <div class="css-1dbjc4n r-1niwhzg r-vvn4in r-u6sd8q r-4gszlv r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw" style="background-image: url(&quot;https://numhub.ams3.digitaloceanspaces.com/airsite/images/4c2b7f56-0855-4909-b76f-595e3ae6afdb.jpg&quot;);">
                    </div><img alt="" draggable="false" src="./PZH_files/4c2b7f56-0855-4909-b76f-595e3ae6afdb.jpg" class="css-9pa8cd">
                    </div>
                    <div class="css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af" style="background-color:rgba(0,0,0,0.60)"></div>
                </div>
                <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                    <div class="css-1dbjc4n r-1777fci r-2llsf r-13qz1uu">
                    <div class="css-1dbjc4n r-1777fci r-13qz1uu" style="-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-right:13.333333333333334px;padding-left:13.333333333333334px;padding-top:40px;padding-bottom:40px;-webkit-box-orient:vertical;-webkit-box-direction:normal" data-testid="viewBlock-undefined">
                        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 288px;">
                        <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                            <div class="css-1dbjc4n r-1777fci r-2llsf r-13qz1uu">
                            <div class="css-1dbjc4n r-1777fci r-13qz1uu" style="-webkit-align-self:center;align-self:center;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-right:13.333333333333334px;padding-left:13.333333333333334px;padding-top:40px;padding-bottom:40px;-ms-flex-item-align:center;-webkit-box-orient:vertical;-webkit-box-direction:normal" data-testid="viewBlock-undefined">
                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 288px;">
                                <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                                    <div class="css-1dbjc4n r-1777fci r-13qz1uu" style="background-image: linear-gradient(0deg, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));">
                                    <div class="css-1dbjc4n r-1awozwy r-1777fci r-13qz1uu" style="align-self: center; flex-direction: column; padding: 33.3333px 0px; -webkit-box-orient: vertical; -webkit-box-direction: normal; max-width: 411.333px;" data-testid="viewBlock-undefined">
                                        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 309.333px;">
                                        <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined">
                                            <div class="css-1dbjc4n" style="align-self: center; margin-right: 10.6667px; margin-left: 10.6667px; width: 288px; max-width: 309.333px;">
                                            <div data-focusable="true" tabindex="0" class="css-1dbjc4n r-1loqt21 r-1otgn73">
                                                <div class="css-1dbjc4n r-1mlwlqe r-1udh08x r-13qz1uu r-417010" style="align-self: center; border-radius: 26.6667px; height: 304px; margin-top: 10.6667px; margin-bottom: 10.6667px; max-width: 309.333px;" data-testid="imageBlock-undefined">
                                                <div class="css-1dbjc4n r-1niwhzg r-vvn4in r-u6sd8q r-4gszlv r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw" style="background-image: url(&quot;https://numhub.ams3.digitaloceanspaces.com/airsite/images/a6848ddf-5db2-4291-b8c6-3529723ac1c6.png&quot;);">
                                                </div><img alt="" draggable="false" src="./PZH_files/a6848ddf-5db2-4291-b8c6-3529723ac1c6.png" class="css-9pa8cd">
                                                </div>
                                            </div>
                                            </div>
                                        </div>
                                        </div>
                                        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
                                        <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                                            <div class="css-1dbjc4n r-1777fci r-13qz1uu">
                                            <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" style="padding: 16px 0px; max-width: 411.333px;" data-testid="viewBlock-undefined">
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="{oper}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">ОПЕРАТОР</div></div>
                                                    </div>
                                                    </a></div>
                                                </div>
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="{texx}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <a href="https://t.me/Fsup_24" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer"><div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">ТЕХПОДДЕРЖКА </div></div></a>
                                                    </div>
                                                    </a></div>
                                                </div>
                                            </div>
                                            </div>
                                        </div>
                                        </div>
                                        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
                                        <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                                            <div class="css-1dbjc4n r-1777fci r-13qz1uu">
                                            <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" style="padding: 16px 0px; max-width: 411.333px;" data-testid="viewBlock-undefined">
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="{bbot}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">БОТ</div></div>
                                                    </div>
                                                    </a></div>
                                                </div>
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="http://hydraruzxpnew4af.onion/market/16673" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <a href="{hyd}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer"><div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">HYDRA </div></div></a>
                                                    </div>
                                                    </a></div>
                                                </div>
                                            </div>
                                            </div>
                                        </div>
                                        </div>
                                        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
                                        <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                                            <div class="css-1dbjc4n r-1777fci r-13qz1uu">
                                            <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" style="padding: 16px 0px; max-width: 411.333px;" data-testid="viewBlock-undefined">
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="{rab}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">РАБОТА</div></div>
                                                    </div>
                                                    </a></div>
                                                </div>
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="{rabw}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">Работа watsapp </div></div>
                                                    </div>
                                                    </a></div>
                                                </div>
                                            </div>
                                            </div>
                                        </div>
                                        </div>
                                        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
                                        <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                                            <div class="css-1dbjc4n r-1777fci r-13qz1uu">
                                            <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" style="padding: 16px 0px; max-width: 411.333px;" data-testid="viewBlock-undefined">
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined">
                                                    <div href="" class="css-1dbjc4n" style="max-width:100%">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">РЕЗЕРВ</div></div>
                                                    </div>
                                                    </div>
                                                </div>
                                                </div>
                                                <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="{legal}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                    <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                        <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">LEGAL </div></div>
                                                    </div>
                                                    </a></div>
                                                </div>
                                            </div>
                                            </div>
                                            <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
                                            <div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined">
                                                <div class="css-1dbjc4n r-1777fci r-13qz1uu">
                                                <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" style="padding: 16px 0px; max-width: 411.333px;" data-testid="viewBlock-undefined">
                                                    <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
                                                    <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="{otz}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer">
                                                        <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined">
                                                            <div class="css-1dbjc4n r-rs99b7 r-1777fci" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">ОТЗЫВЫ </div></div>
                                                        </div>
                                                    </div>
                                                </div>
                                                </div>
                                            </div>
                                            </div>
    '''
    site3 = '''
                                            <iframe id="tgw_6228d60dcd821b3ca4054403" frameborder="0" scrolling="no" horizontalscrolling="no" verticalscrolling="no" width="100%" height="540px" async></iframe><script>document.addEventListener("DOMContentLoaded",function(){document.getElementById("tgw_6228d60dcd821b3ca4054403").setAttribute("src","https://tgwidget.com/channel/v2.0/?id=6228d60dcd821b3ca4054403")})</script>
                                        </div>
                                        </div>
                                        <div class="css-1dbjc4n r-1777fci r-417010" style="-webkit-flex-shrink:1;flex-shrink:1;max-width:100%;-ms-flex-negative:1">
                                        <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined">
                                            <div dir="auto" class="css-901oao" style="align-self: center; color: rgb(41, 128, 185); font-size: 57.3333px; font-weight: 900; line-height: 74.5333px; margin: 0px 37.3333px; text-align: center; max-width: 411.333px;" data-testid="textBlock-undefined"></div>
                                        </div>
                                        </div>
                                        <div class="css-1dbjc4n r-1777fci r-417010" style="-webkit-flex-shrink:1;flex-shrink:1;max-width:100%;-ms-flex-negative:1">
                                        <div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined">
                                            <div dir="auto" class="css-901oao" style="align-self: center; color: rgb(255, 255, 255); font-size: 21.3333px; line-height: 27.7333px; margin-top: 26.6667px; margin-bottom: 26.6667px; text-align: center; max-width: 411.333px;" data-testid="textBlock-undefined"></div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
                <script async="" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/analytics.js(1).%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script>
                <script nomodule="" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/polyfills-81ae63683d9078fdea77.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script>
                <script async="" data-next-page="/" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/index.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script>
                <script async="" data-next-page="/_app" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/_app.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/webpack-5247482ebcd811c9f929.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/framework.1da4ef788d111291b4b6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/commons.4cf1157854d94d82078f.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/d22e4f5c724d666750fe44516895f703072ed09f.7b1b72c2c4e99b5a67d6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/main-cb29ba5623faf6e6dfd1.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/151566a4651e83b50223f84eab66dbab6954d29f.7d68887e701c477e5f78.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/be4ce260d173322dd4ddf7dc70532fb96bd360d4.0efdea021efae6576dac.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/_buildManifest.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script>
                <xpather id="xpather">
        
                    <xpather id="xpather-result"></xpather>
                    <xpather id="xpather-sidebar-toggler"></xpather>
                </xpather>
                <xpather id="xpather-sidebar">
                    <xpather id="xpather-sidebar-spacer"></xpather>
                    <xpather id="xpather-sidebar-entries"></xpather>
                </xpather>
                </div>
            </div>
            </div>
        
        <xpather id="xpather">

            <xpather id="xpather-result"></xpather>
            <xpather id="xpather-sidebar-toggler"></xpather>
        </xpather>
        <xpather id="xpather-sidebar">
            <xpather id="xpather-sidebar-spacer"></xpather>
            <xpather id="xpather-sidebar-entries"></xpather>
        </xpather>
        
        </body></html>
    '''
    sss = (site + site2 + site3)
    with  open("index.html", "w", encoding="utf-8") as f:
        f.write(sss)


logo2 = """

            ____ ______   _
            |  _ \__  / | | |
            | |_) |/ /| |_| |
            |  __// /_|  _  |
            |_|  /____|_| |_|
"""
print(logo2)
print(logo)
while True:
    vib = input("\n     Какую кнопку нужно изменить ?:     ")

    if vib == '1':
        oper = input("\n    Оператор: ")
        with open("system/oper.txt", "w", encoding="utf-8") as f:
            f.write(oper)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    if vib == '2':
        texx = input("\n    Техподержка:  ")
        with open("system/texx.txt", "w", encoding="utf-8") as f:
            f.write(texx)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    if vib == '3':
        bbot = input("\n    Бот:  ")
        with open("system/bbot.txt", "w", encoding="utf-8") as f:
            f.write(bbot)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    if vib == '4':
        hyd = input("\n     Hydra: ")
        with open("system/hyd.txt", "w", encoding="utf-8") as f:
            f.write(hyd)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    if vib == '5':
        rab = input("\n     Работа:   ")
        with open("system/rab.txt", "w", encoding="utf-8") as f:
            f.write(rab)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    if vib == '6':
        rabw = input("\n    Работа WatsApp:    ")
        with open("system/rabw.txt", "w", encoding="utf-8") as f:
            f.write(rabw)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    if vib == '7':
        legal = input("\n   legal:   ")
        with open("system/legal.txt", "w", encoding="utf-8") as f:
            f.write(legal)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    if vib == '8':
        otz = input("\n     Отзывы:    ")
        with open("system/otz.txt", "w", encoding="utf-8") as f:
            f.write(otz)
        print("     \nКонтакт Изменен")
        main()
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        print("\n   Сайт обновлен !")
        break
    else:
        print("\n       Неверный Выбор")
    

