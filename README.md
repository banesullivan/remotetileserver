# 📡 Remote Tile Server

[![Deploy on Heroku](https://github.com/banesullivan/remotetileserver/actions/workflows/heroku.yml/badge.svg)](https://github.com/banesullivan/remotetileserver/actions/workflows/heroku.yml)

*A template for deploying [localtileserver](https://github.com/banesullivan/localtileserver) on Heroku.*


## ℹ️ Overview

This is a template repository for deploying a localtileserver instance on
Heroku.


## 🚀 Usage

Create a new repository from this template and set the following Secrets in
your repository for your Heroku account:

- `HEROKU_API_KEY`
- `HEROKU_APP_NAME`
- `HEROKU_EMAIL`

After that, the GitHub Action should deploy localtileserver for you on your
Heroku account and you can configure the dyno to your desire.

I recommend setting up your AWS S3 credentials in the Heroku interface or at
least setting `AWS_NO_SIGN_REQUEST=YES`.


## 💭 Feedback and Contributing

For any feedback or questions, please head over to the
[Discussions forum for `localtileserver`](https://github.com/banesullivan/localtileserver/discussions)
