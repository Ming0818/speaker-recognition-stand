# -*- coding: utf-8 -*-

# список фраз для произнесения
import numpy as np

def randomPhrase():
    phrases = [
        'С точки зрения молодости жизнь есть бесконечное будущее, с точки зрения старости — очень короткое прошлое.',
        'Жизнь состоит не в том, чтобы найти себя. Жизнь состоит в том, чтобы создать себя.',
        'Ты не научишься кататься на коньках, если боишься быть смешным. Лёд жизни скользок.',
        'Жизнь — как коробка шоколадных конфет. Никогда не знаешь, какая начинка тебе попадется.',
        'Стремление - это та энергия, которая в конце концов изменит нас.',
        'Всякая радость в этом мире проистекает из желания счастья другим. Всякое страдание в этом мире берёт начало в желании счастья самому себе.',
        'Самая чистая вода бывает в тех источниках, в которых она пробивается сквозь препятствия, преодолевая трудности',
        'Мы живы не потому, что бережем себя, а потому, что делаем дело жизни',
        'Жизнь — это комедия для тех, кто думает, и трагедия для тех, кто чувствует.',
        'Если у тебя получилось обмануть человека, это не значит, что он дурак, это значит, что тебе доверяли больше, чем ты этого заслуживаешь',
        'Те, кто читают книги, всегда будут управлять теми, кто смотрит телевизор.',
        'Сильный человек — это не тот у которого все хорошо. Это тот, у которого все хорошо несмотря ни на что.',
        'Два самых важных дня в твоей жизни: день, когда ты появился на свет, и день, когда ты понял зачем!',
        'Доброта — это то, что может услышать глухой и увидеть слепой.',
        'Не заблуждайтесь в мысли, что мир вам чем-то обязан — он был до вас и ничего вам не должен.',
        'Через двадцать лет вы будете более сожалеть о том, чего не сделали, чем о том, что вы сделали. Поэтому, отбросьте сомнения.',
        'Не расставайтесь со своими иллюзиями. Когда их не станет, может быть вы и продолжите существовать, но перестанете жить.',
        'Прощение — это аромат, который оставляет фиалка на сапоге, раздавившем ее.',
        'Давайте поблагодарим дураков. Не будь их, остальным было бы трудно добиться успеха.',
        'Горе нужно пережить в одиночестве, но радость — чтобы познать в полной мере — нужно разделить с другим человеком.'
    ]
    return phrases[np.random.randint(len(phrases))]
