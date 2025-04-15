from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("菜单")
    async def helloworld(self, event: AstrMessageEvent):
        yield event.plain_result("
蔡徐坤、来点坤图	获取蔡徐坤相关随机图片	随机明星图片
丁真、来点丁真图	获取丁真相关随机图片	随机人物摄影
原神黄历、来点骚的	获取原神主题黄历图文	二次元图文结合
热榜	获取60秒热点资讯图片	新闻资讯图片
小动物	获取动漫风格动物插画	二次元风格动物图片
三坑少女	获取三坑服饰风格美女图片	时尚穿搭摄影
看看妞、看看腿	获取人物美拍/腿部特写图片	人物摄影图片
猫猫	获取萌宠猫咪主题图片	治愈系萌宠图片
风景、景色	获取二次元风格风景CG图片	二次元场景插画
随便来点	随机获取各类风格图片	综合类型图片
龙图	获取东方幻想风格龙主题图片	奇幻风格插画
cosplay、来点cos	获取角色扮演Cosplay图片	三次元Cosplay摄影
全国阵雨（存在问题无法使用）	获取天气主题阵雨场景图片	天气相关插画
来点二次元	获取动漫风格美女插画	二次元美少女插画
海贼王、蜡笔小新	获取对应动漫角色官方/同人图	动漫IP角色图片
doro结局	获取Doro游戏剧情结局图片	游戏CG剧情图片
早安、晚安	获取早晚问候主题温馨图片	治愈系问候插画
历史上的今天	获取历史事件回顾资讯图片	历史资讯图文
腹肌	获取健身腹肌主题摄影图片	运动健身图片
来点原神	获取原神角色/场景官方插画	游戏IP插画
弔图 （存在问题）	获取网络热门搞笑趣味图片	梗图/搞笑图片")# 发送一条纯文本消息

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`

    

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
