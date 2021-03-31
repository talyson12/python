frase = 'Curso em Vídeo Python'
print(type(frase), frase)
print('-'*10)
print(frase[3]) #terceiro slot da frase, ou seja, letra 's'
print('-'*10)
print(frase[:3]) #vai do zero até o 3, sem contar o 3, ou seja, mostra o 2
print('-'*10)
print(frase[5:]) #vai do 5 até o final
print('-'*10)
print(frase[3:10]) #vai do 3 até o 10, sem contar o 10, ou seja, mostra até o 9
print('-'*10)
print(frase[3:15:2]) #do 3 até o 15 pulando de 2 em e
print('-'*10)
print(frase[3::2]) #indo do 3 até o final pulando de 2 em 2
print('-'*10)
print(frase[:15:2]) #indo do início até o 15 pulando de 2 em 2
print(frase[::2]) #vai do início ao fim pulando de 2 em 2
print('-'*10)
print("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")

