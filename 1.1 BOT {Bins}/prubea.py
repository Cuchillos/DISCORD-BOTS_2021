import json

with open('servidores.json') as file:
    content = json.load(file)
    file.close()

creado = 0

for x in content:
    if str(812324710959677480) in x:
        cana = content[x]['Canal']

        with open('servidores.json', 'r+') as file:
            content = file.read()
            file.seek(0)
            content = content.replace(f'{cana}', 'Se vino totiiii vamooo')
            file.write(content)
            file.close()
    else:
        if creado == 0:
            with open('servidores.json', 'r+') as file:
                content = json.load(file)

                nuevo = {"aaaaaaaaaaaxd": {"Canal": "jaja", "Premium": "claro"}}
                content.update(nuevo)
                file.seek(0)
                json.dump(content, file)

                file.close()

            creado +=1

