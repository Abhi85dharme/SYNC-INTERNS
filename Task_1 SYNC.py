from plyer import notification

title = 'buenas noches sync interns!'

message= 'HAVE AN AMAZING DAY ALL!'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)