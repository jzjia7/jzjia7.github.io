# jzjia7.github.io

Jeremy “Jez” Jia 的个人联系页。线上地址：<https://jzjia7.github.io>

## 文件结构

| 路径 | 用途 |
| --- | --- |
| `index.html` | 网站首页。目前就是联系页；以后扩充成完整个人主页时，改的是这个文件。 |
| `contact/index.html` | 联系页的永久版本，地址 <https://jzjia7.github.io/contact/>。首页以后怎么改都不影响它。 |
| `wechat-card/wechat-card.png` | 朋友圈用的二维码卡片（1080×1440），二维码指向首页。 |
| `wechat-card/card.template.html`、`build.py` | 生成卡片的模板和脚本，改了地址或文案后重新生成用。 |
| `_config.yml` | 让 GitHub Pages 不发布本说明和卡片源文件。 |

整个页面是一个独立的 HTML 文件，不依赖外部字体、库或图片，国内打开也快。

## 版本存档

- `contact-v1`：第一版联系页（2026-10-26），含微信适配。
- `old-site`：之前的测试版主页，已被替换。

任何时候都可以在 GitHub 上按标签找回当时的完整文件：<https://github.com/jzjia7/jzjia7.github.io/tags>

## 最初的需求

- 公开名字：Jeremy "Jez" Jia。
- 页面只讲三件事：我是谁、我的身份标签、我的联系方式。
- 联系方式是 jzjia7@qq.com，它同时是邮箱和 Apple ID，所以对方可以发邮件、发 iMessage，或者用 FaceTime 联系我。
- 身份标签是 “Student-Athlete”，用特殊字体放在页面某个位置，不必强调。
- 点击邮箱后给出选项：发邮件、发 iMessage、FaceTime。
- 排版要有品位。欣赏 Jony Ive、Alessi 那种设计感，但不是照抄苹果。
- 颜色素一些。
- 要适配 iPhone、安卓手机、iPad 和电脑网页，以手机为主。
- 流程：先做静态页面在本地预览，审核调整后再部署上线。

## 设计决定

- **配色**：暖白底 `#F4F2EE`，近黑字 `#1A1A1A`，灰 `#8B8881`。跟随系统自动切换深色模式。
- **字体**：正文用系统无衬线字体（苹果设备上是 SF Pro）；身份标签用系统衬线斜体（苹果设备上是 New York），和正文形成对比。
- **布局**：右上角放身份标签；名字做成大字，“Jez” 用灰色；邮箱放在下方，靠近拇指能点到的位置。
- **联系菜单**：手机上从底部弹出，电脑上在屏幕中间弹出。选项有邮件、iMessage、FaceTime 视频、FaceTime 语音和复制地址。在 Mac 上，iMessage 用 `imessage:` 链接；非苹果设备上会提示 iMessage 和 FaceTime 需要苹果设备。
- **微信内打开**：微信会拦截邮件、iMessage 和 FaceTime 的跳转，所以在微信里只显示放大的邮箱和“复制邮箱地址”，并提示点右上角 ··· 在浏览器打开。

## 在微信里使用（实测）

- 微信签名里的文字不能点也不能复制，不适合放网址。
- 把 `wechat-card.png` 发一条朋友圈并置顶，别人从你的资料页就能看到。
- 用“扫一扫”扫码会直接打开页面；长按图片识别时，微信会先提示这是外部网页、需要跳转。
- 聊天里直接发网址文字是可以点开的。

## 以后扩充成完整个人主页

1. 直接改 `index.html`，或者换成新的首页；`contact/` 保持不动。
2. 新首页里放一个指向 `/contact/` 的入口。
3. 如果希望朋友圈二维码以后也一直打开联系页，就把 `build.py` 里的 `URL` 改成 `https://jzjia7.github.io/contact/`，再重新生成卡片。

重新生成卡片需要 `qrcode` 这个 Python 库和 Google Chrome：

```sh
cd wechat-card
python3 build.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=540,720 \
  --screenshot="$PWD/wechat-card.png" "file://$PWD/card.html"
```
