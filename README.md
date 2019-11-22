Задача №1 ”Разработка протокола прикладного уровня”

Необходимо разработать протокол прикладного уровня, который будет соотвествовать следующей спецификации:

Сообщение клиент-сервер:😁

∙ Сначало передается командная строка состоящая из [Команда] [Размер поляполезной нагрузки]

– Команды - STAT и ENTI, команда STAT возращает статистические дан-

ные, собранные в ходе анализа переданного текста, а команда ENTI

возвращает найденные именованные сущности

– В качестве полезной нагрузки будет передаваться список твитов

– Нужно посчитать 10 наиболее часто встречающихся слов, 10 наиболее

популярных твитов, их авторов и сколько раз они были ретвитнуты, 10

самых популярных авторов. Информацио о странах, в которых пользо-

ватели создают контент (твиты) и в которых его потребляют (ретвитят)

– Датасет - Tweets

– Для распознования именованных сущностей предлагается использовать

Stanford CoreNLP Natural Language Processing Using Stanford’s CoreNLP

– Сервер должен поддерживать несколько одновременных подключений

∙ После передаются данные, размер которых указан в комндной строке

∙ Данные могут передавать в любом удобном формате - csv, json, xml etc

Сообщение сервер-клиент:😊

∙ Ответ может передаваться в любом удобном формате - csv, json, xml etc

∙ Первой строкой передается размер данных ответа