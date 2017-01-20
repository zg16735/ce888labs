from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
global ave
ave = 0

@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    global ave
    a = 0.01
    ave = ave + a* (emo.detect_emotion_in_raw_np(str(trigger)) - ave)
    bot.say('Hi, ' + trigger.nick)
    print(ave)
