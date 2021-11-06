def flex_message_attractions(location,title,description,image):
    content = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": f"{image}",
                    "size": "5xl",
                    "aspectMode": "cover",
                    "aspectRatio": "2:3",
                    "gravity": "top"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": f"{title}",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": f"{description}",
                                    "color": "#ebebeb",
                                    "size": "sm",
                                    "flex": 0,
                                    "wrap": True
                                }
                            ],
                            "spacing": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "text",
                                            "text": "查看更多",
                                            "color": "#ffffff",
                                            "flex": 0,
                                            "offsetTop": "-2px",
                                            "action": {
                                                "type": "uri",
                                                "label": "景點導址",
                                                "uri": f"https://liff.line.me/1656487192-GDz8ZxYQ?redirect=attractions&location={location}"
                                            }
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "spacing": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "景點導址",
                                        "uri": f"https://liff.line.me/1656487192-GDz8ZxYQ?redirect=attractions&location={location}"
                                    }
                                },
                                {
                                    "type": "filler"
                                }
                            ],
                            "borderWidth": "1px",
                            "cornerRadius": "4px",
                            "spacing": "sm",
                            "borderColor": "#ffffff",
                            "margin": "xxl",
                            "height": "40px"
                        }
                    ],
                    "position": "absolute",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#03303Acc",
                    "paddingAll": "20px",
                    "paddingTop": "18px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "虎尾商圈",
                            "color": "#ffffff",
                            "align": "center",
                            "size": "xs",
                            "offsetTop": "3px",
                            "wrap": True
                        }
                    ],
                    "position": "absolute",
                    "cornerRadius": "20px",
                    "offsetTop": "18px",
                    "backgroundColor": "#0072E3",
                    "offsetStart": "18px",
                    "height": "25px",
                    "width": "100px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "＃點我分享到社群",
                            "align": "center",
                            "size": "xs",
                            "offsetTop": "3px",
                            "wrap": True
                        }
                    ],
                    "position": "absolute",
                    "cornerRadius": "20px",
                    "offsetTop": "18px",
                    "backgroundColor": "#a6ed8e",
                    "height": "25px",
                    "width": "120px",
                    "offsetEnd": "18px",
                    "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": "https://developers.line.biz/en/news/2021/"
                    }
                }
            ],
            "paddingAll": "0px"
        }
    }
    return content
