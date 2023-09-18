import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
django.setup()

from streaming.models import Favourite, Movie, MovieWatched, User

print('Starting populate script')

# Remove existing data
print('- Removing existing data')
User.objects.all().delete()
Movie.objects.all().delete()
Favourite.objects.all().delete()
MovieWatched.objects.all().delete()


# Generate some users
print('- Generating some user')
User.objects.create(
    username='pedro.carvalho',
    email='pedro@mail.com',
    first_name='Pedro',
    last_name='Carvalho',
    birth_date=date(1987, 4, 17),
)
User.objects.create(
    username='jorge.campos',
    email='jorge@mail.com',
    first_name='Jorge',
    last_name='Campos',
    birth_date=date(1992, 11, 5),
)
User.objects.create(
    username='julia.martins',
    email='julia@mail.com',
    first_name='Julia',
    last_name='Martins',
    birth_date=date(1989, 7, 23),
    type=User.Type.ADMIN
)
for user in User.objects.all():
    user.set_password('fgv123')
    user.save()

# Generate some movies
print('- Generating some movies')
Movie.objects.create(
    title='Iron Man 2',
    year=2010,
    cover='https://static.wikia.nocookie.net/marvel/images/0/0c/Homem_de_Ferro_2_p%C3%B4ster.jpg/revision/latest?cb=20170809144405&path-prefix=pt-br',
    description='Homem de Ferro 2)[4][5] é um filme estadunidense de super-herói de 2010 baseado no personagem Homem de Ferro da Marvel Comics.' 
            'Produzido pelo Marvel Studios e distribuído pela Paramount Pictures,[a] é a sequência de Iron Man (2008), e o terceiro filme do Universo Cinematográfico Marvel. Dirigido por Jon Favreau e escrito por Justin Theroux, o filme é estrelado por Robert Downey, Jr., Gwyneth Paltrow, Don Cheadle, Scarlett Johansson, Sam Rockwell, Mickey Rourke e Samuel L. Jackson. Após os acontecimentos de Iron Man, Tony Stark está resistindo apelos do governo dos Estados Unidos para entregar a tecnologia do Homem de Ferro e ao mesmo tempo combater a sua saúde em declínio a partir do reator arc em seu peito. Enquanto isso, o desonesto cientista russo Ivan Vanko desenvolveu a mesma tecnologia e construiu suas próprias armas, a fim  de prosseguir uma vingança contra a família Stark, unindo forças com rival de Stark, Justin Hammer. 2008',
    midia='https://www.youtube.com/watch?v=b5qs_RtpkhA'
)
Movie.objects.create(
    title='The Dark Knight',
    year=2008,
    cover='https://uauposters.com.br/media/catalog/product/cache/1/thumbnail/800x930/9df78eab33525d08d6e5fb8d27136e95/5/0/508720201013-uau-posters-filmes-batman-the-dark-knight-batman-o-cavaleiro-das-trevas.jpg',
    description='Batman: O Cavaleiro das Trevas[1][6]; prt: O Cavaleiro das Trevas[4]) é um filme britânico-estadunidense de super-herói de 2008,' 
            'dirigido, produzido e co-escrito por Christopher Nolan. Baseado no personagem Batman da DC Comics, The Dark Knight faz parte da série de filmes Batman de Nolan, sendo uma continuação de Batman Begins, de 2005. Christian Bale repete seu papel como Bruce Wayne/Batman, com Morgan Freeman, Gary Oldman e Michael Caine retornando como Lucius Fox, James Gordon e Alfred Pennyworth, respectivamente. O filme introduz o personagem Harvey Dent (Aaron Eckhart), o novo promotor público de Gotham e chefe de Rachel Dawes (Maggie Gyllenhaal), amiga de infância de Wayne, que se juntam ao Batman e à polícia para combater a nova ameaça emergente de um criminoso que se auto-intitula "Coringa" (Heath Ledger)',
    midia='https://www.youtube.com/watch?v=8sB1HTghkg4'
)
Movie.objects.create(
    title='Rocky Balboa',
    year=2006,
    cover='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAfcbCgonz2bmvyW5b6JasgG51irW0-bxN5guGRw4uYg&s',          
    description='Rocky Balboa, ex-campeão mundial de pesos pesados, está há 16 anos aposentado do boxe depois de lutar com Tommy Gunn. Rocky depois de ter perdido a esposa, Adrian, por causa de um câncer em 2002, não consegue parar de pensar em tudo o que havia vivido junto a ela ao longo de toda sua vida. Após isso Rocky passa a ser dono de um restaurante italiano com o nome de Adrian, onde as pessoas vão principalmente para ouvir-lhe contar histórias durante a refeição. Seu filho já é um adulto e apesar dos triunfos de seu pai se envergonha dele e se sente ofuscado e dependente da imagem do pai. Porém com saudades de suas lutas Rocky decide enfrentar o atual campeão dos pesos pesados, Mason Dixon, que é desprezado pelos fãs deste esporte devido aos seus combates rápidos e chatos, onde seu rival apenas tem tempo para cair abatido na lona. A falta de um rival à altura de Dixon e a mediocridade dos existentes leva à criação de um programa virtual,'
         'com o qual se comprova quem seria vencedor se Mason enfrentasse o legendário Rocky Balboa.'
                'one of the greatest psychological and physical tests of his ability to fight injustice.',
    midia='https://www.youtube.com/watch?v=cx48_97PfvM'
)
Movie.objects.create(
    title='The Warriors  Os Selvagens da Noite',
    year=2003,
    cover='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTgMKgtthdEZWFj-aRWvoq3KTepj6-L7CsvR3AFIYfrTURwjnV0',
    description='É ambientado em uma Nova York tomada por gangues de rua, no início dos anos 80. O líder da maior gangue da cidade,' 
            'a “Gramercy Riffs”, declara uma trégua e convoca uma reunião geral no Bronx, com a intenção de unir' 
            'todas as gangues para a dominação da cidade. No entanto, durante o seu pronunciamento, Cyrus é brutalmente assassinado por Luther, líder da “Rogues”. Um membro da gangue “Warriors”, do distante bairro de Coney Island, testemunha seu ato e é visto por ele. Para salvar a própria pele, Luther imediatamente acusa a “Warriors” de assassinar Cyrus, fazendo com que a “Gramercy Riffs” os persigam por toda a cidade, após anunciarem numa estação de rádio que querem todos os “Warriors”, vivos ou mortos.',
    midia='https://www.youtube.com/watch?v=MN4-i_rJhkc'
)
Movie.objects.create(
    title='Top Gun Maverick',
    year=2022,
    cover='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthgBba12lF_hfubI1G57okF5tXlKOoDzbyKncEKQ39BdEc-pH',
    description='Maverick é um filme estadunidense de 2022, dos gêneros ação, aventura e drama, dirigido por Joseph Kosinski; com roteiro de Peter Craig, Justin Marks, Ashley Edward Miller e Zack Stentz, sendo a sequência de Top Gun, de 1986.' 
            'Tom Cruise reprisa seu papel principal como o aviador naval Pete Maverick Mitchell. Também é estrelado por Miles Teller, Jennifer Connelly, Jon Hamm, Glen Powell, Monica Barbaro, Ed Harris e Val Kilmer,este último reprisando seu papel como Tom Iceman Kazanski. A história envolve Maverick confrontando seu passado enquanto treina um grupo de jovens graduados na Escola Aeronáutica Top Gun, incluindo o filho de seu falecido melhor amigo, para uma missão perigosa.',
    midia='https://www.youtube.com/watch?v=9Jgua93Xhcw'
)
Movie.objects.create(
    title='Surf no Havaí',
    year=1987,
    cover='https://encrypted-tbn0.gstatic.com/images?q=tbn:AN…yBElwmCbsOJxa04L6vAkNQF4mWf7dz8H9TTY00&usqp=CAE&s',
    description='Rick é um surfista do interior dos EUA que vai ao Havaí para realizar seu grande sonho: encarar na prancha as ondas mais perigosas do mundo. Mas ele não conhece praticamente nada sobre os costumes locais, o que lhe traz alguns problemas. Até que ele conhece o guru Chandler, que vai ensinar a Rick a diferença entre os "soul surfers" (surfistas de alma) e aqueles que surfam simplesmente pelo dinheiro. Ao mesmo tempo, o jovem ficará interessado' 
        'por uma bela garota nativa. O filme conta com participações de surfistas profissionais e campeões - como Shaun Tompson e Derek Ho, entre outros.',
    midia='https://www.youtube.com/watch?v=mbpjXvoMAz8'
)
Movie.objects.create(
    title='O Grande Dragão Branco',
    year=1988,
    cover='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlS8LLePZQxSYmEll4wlvydApSeLzukjD8LHEG9NNYQEoy55Fn',
    description='Foi neste filme de Newt Arnold que o ator belga Jean-Claude Van Damme, aos seus 28 anos, deu os primeiros passos da sua carreira cinematográfica nos Estados Unidos, precisamente numa história baseada em acontecimentos verídicos.' 
        'Van Damme é Frank Dux, um jovem treinado em Ninjutsu que aprendeu os rudimentos das artes marciais através dos ensinamentos do seu mestre Senzo Tanaka. E será precisamente num tributo à Senzo que Frank aceita participar do famoso, exigente,' 
        'mortífero e clandestino torneio Kumite, em Hong Kong, tornando-se assim o primeiro ocidental a ganhar aquela competição.',
    midia='https://www.youtube.com/watch?v=rqksyq5tvV4'
)
Movie.objects.create(
    title='Tropa de Elite',
    year=2002,
    cover='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSImFOG2njNPb5YzasyZBccPPtykmGZWGlx7sPNUWb3&usqp=CAE&s',
    description='É o primeiro longa de ficção do diretor José Padilha, que anteriormente dirigiu o documentário Ônibus 174 (2002). Foi objeto de grande repercussão antes mesmo de seu lançamento, por ter sido o primeiro filme brasileiro, a meses antes de chegar aos cinemas, vazar para o mercado pirata e a internet.[6] Um dos protagonistas do filme, o ator Caio Junqueira, chegou a declarar que, por mais que achasse a pirataria algo negativo, sabia que havia sido "por causa dela que o trabalho atingiu o público da televisão".' 
        'Uma pesquisa feita pelo Ibope chegou a estimar que mais de 11 milhões de brasileiros teriam visto o filme de forma ilegal [8] – isso, entretanto, não impediu o filme de ter sido bem-sucedido nas bilheterias, tendo estreado em primeiro lugar.',
    midia='https://www.youtube.com/watch?v=_V_nZNWPYQk'
)
Movie.objects.create(
    title='Transformes',
    year=2017,
    cover='https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcRL1XgVEINwK9ZkYMu2_3Sw_4RRp7p0WRSVM6mHwvbOR-e_Lc-qMM-o3XPGXRy3GDx4',
    description='A série tem recebido críticas mistas; especialmente com relação a enredo, humor ácido, abuso de marketing indireto e duração dos filmes.[2] Por outro lado, os efeitos visuais, sequências de ação e música empregados ao longo de toda a franquia têm sido amplamente elogiados e observados positivamente pela crítica em geral. Atualmente, a série Transformers é a décima terceira franquia mais lucrativa da história, juntamente com Pirates of the Caribbean e Fast & Furious, sendo também a quarta franquia com maior rendimento por filme, atrás apenas de The Lord of the Rings e Harry Potter e Pirates of the Caribbean.',
    midia='https://www.youtube.com/watch?v=v8ItGrI-Ou0'
)
Movie.objects.create(
    title='Exterminador do Futuro 2',
    year=1991,
    cover='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuzfZO11pBIB7x1wEetZ7Y-GX5cGLPDEiQ1Vm9dcY&usqp=CAE&s',
    description='O clássico longa-metragem co-escrito e dirigido por James Cameron foi lançado em 1991' 
    'e trouxe todo o elenco protagonista de volta, incluindo Arnold Schwarzenegger e Linda Hamilton',
    midia='https://www.youtube.com/watch?v=lwSysg9o7wE'
)

# Create some favourite movies for each user
print('- Creating favourite movies for each user')
for user in User.objects.all():
    from random import randint
    num_favourite_movies = randint(1, 3)
    movies = Movie.objects.order_by('?')[:num_favourite_movies]
    for movie in movies:
        Favourite.objects.create(
            user=user,
            movie=movie
        )

print('Finished!')