# QQAutoDM

> This program focuses on automatically sending DMs through TIM and QQ at certain time to certain user.



## Requirements

- python3
- import win32gui
- import win32api
- import win32con
- import win32clipboard
- pause



## Instructions

First edit  `config` in *if ____name____ == ____main____*:

```
    config = {
    "user": "the name of window to whom you want to send DMs to",
    "msg": "any message",
    "clock": "2033-05-30 18~00"
    }
```

***Very important step***. **Double click** to the account you want to send DMs, and make sure **an independent window** for chats is opened. And the name for that window is just how you should fill in the `config`. Then adjust the window’s size, make sure the input text part is bigger, better 3 times taller than the button for `sending`. And check if you have set `ENTER` as the default hotkey for sending messages.

Finally, **run auto_dm.py**.

If you have set the hour and minute, program will run at set time.

```
Sent :  2023-05-30 15:47:26.045654
```

However, if you just set date, it is for first run test, the program will automatically send messages after 10 seconds once the messages arrive at text area of the DM webpage.



## Arguments

All arguments are set in `config` in __main__.

```
{
    "user": "test",
    "msg": "你好",
    "clock": "2023-05-30 1800"
}
```

### user

The window name for searching for its handle to whom you want to send DMs. TIM and QQ now allow users to edit **NOTE NAME** for each account and group.  Note name is better as it will not change. Note name will be the window name, or by default another person’s account name will be shown. In order to avoid TypeError as nowadays many would add emoji in ID, it is highly recommend to use note name. Also, it could be used to send to **group** messages.

### msg

Any string. Encode in UTF-8.

### clock

format as

`YYYY-MM-DD HH~mm`

or

`YYYY-MM-DD`

`YYYY-MM-DD HH~mm` this format will let program run at the set time to automatically send messages, consider better to use when you debug this program is OK on your PC.

`YYYY-MM-DD` this format is used only for **debug**. Automatically sending messages **10 seconds** after program starts.



## WARNING

1. Users should **NOT** run this program less than **1 minute** before the set time.
2. Users should **NOT** click or move any window on computer, better stay away during the program.



## Further

1. For now, text area in Weibo only support inputs messages without `ENTER`, but it could be done with `CTRL+ENTER` to input texts with `ENTER`
2. This program **only support 1 receiver at 1 set time**. If you want to send to multiple user at the same time, it is better to run in multiple terminal to make sure the timeliness.
3. About timeliness. After multiple tests on program, for now without the interruption of bad network, the delay is less than **0.02** second. Will continue to improve and concentrate more on this feature.
4. The origin of this program is to send to someone at certain minute, so the second is ignored. Also, TIM/QQ doesn’t show the second of sent messages, so initially all set time will be changed to `%H%M:00` to make sure the timeliness.