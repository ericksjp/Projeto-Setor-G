



lista = [

                    "BF Surfer",

                    "Bravado Bison",

                    "Bravado Rumpo",

                    "Bravado Youga",

                    "Brute Boxville",

                    "Brute Camper",

                    "Brute Pony",

                    "Brute Taco Van",

                    "Declasse Burrito",

                    "Declasse Gang Burrito",

                    "Vapid Bobcat XL",

                    "Vapid Clown Van",

                    "Vapid Minivan",

                    "Vapid Speedo",

                    "Zirconium Journey",

                    "Bravado Paradise",

                    "Declasse Moonbeam",

                    "Declasse Moonbeam Custom",

                    "Vapid Minivan Custom",

                    "Bravado Rumpo Custom",

                    "Bravado Youga Classic",

                    "Brute Armored Boxville",

                    "Vapid Speedo Custom",



]

for i, word in enumerate(lista):
    print(f'<li><a href="#v{i+1}"><span>{i+1}.</span> {word}</a></li>')