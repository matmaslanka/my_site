from datetime import date

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

all_posts = [
    {
    'slug': 'django',
    'image': 'django_icon.png',
    'autor': 'Mati',
    'date': date(2024, 2, 22),
    'title': 'Django',
    'excerpt': 'Praca w django to czysta przyjemność!',
    'content': """Django to otwartoźródłowy framework, który został zaprojektowany tak, aby umożliwić szybkie i efektywne tworzenie skalowalnych aplikacji webowych. Dzięki swojej przejrzystej strukturze i bogatym zestawie funkcji, Django jest wyborem wielu programistów na całym świecie.

        Jedną z największych zalet Django jest jego wbudowane wsparcie dla modelu MTV (Model-Template-View), co ułatwia organizację kodu i separację logiki biznesowej od warstwy prezentacji. Dodatkowo, Django oferuje wiele gotowych modułów i rozszerzeń, które pozwalają programistom szybko budować funkcjonalności, takie jak uwierzytelnianie użytkowników, obsługa formularzy czy obsługa baz danych.

        Co więcej, Django promuje dobre praktyki programistyczne, takie jak DRY (Don't Repeat Yourself) i convention over configuration, co sprawia, że kod jest czytelny, łatwy do zrozumienia i łatwy do utrzymania.

        Warto również wspomnieć o rozbudowanej społeczności Django, która stale rozwija framework, udostępniając nowe wersje i rozwiązując zgłaszane problemy.

        Podsumowując, Django to potężne narzędzie, które umożliwia szybkie i efektywne tworzenie zaawansowanych aplikacji internetowych w języku Python. Jeśli dopiero zaczynasz swoją przygodę z tworzeniem stron internetowych lub szukasz solidnego frameworka do swojego projektu, warto dać szansę Django. Do zobaczenia w kolejnych wpisach, gdzie zgłębimy jeszcze bardziej tę fascynującą tematykę!""",
    },
    {
    'slug': 'wspinaczka',
    'image': 'wspinaczka.jpg',
    'autor': 'Mati',
    'date': date(2024, 1, 5),
    'title': 'Wspinaczka po baldach',
    'excerpt': 'Wspinanie daje siłę!',
    'content': """Bouldering to rodzaj wspinaczki, który polega na pokonywaniu krótkich, intensywnych tras bez użycia liny ani asekuracji. Zamiast tego, wspinaczka odbywa się na niewielkich skałach, zwanych boulderami, często umieszczonych na specjalnie przygotowanych ścianach w salach wspinaczkowych lub na świeżym powietrzu.

Co sprawia, że bouldering jest tak popularny? Przede wszystkim jest to niezwykle ekscytująca i satysfakcjonująca forma aktywności fizycznej. Każdy problem wspinaczkowy (tzw. boulder) stanowi unikalne wyzwanie, które wymaga od wspinacza nie tylko siły fizycznej, ale także zręczności, elastyczności i strategii.

Bouldering to również świetny sposób na poprawę kondycji fizycznej i zdrowia psychicznego. Wspinaczka angażuje całe ciało, wzmacniając mięśnie, poprawiając gibkość i koordynację ruchową. Ponadto, skupienie się na pokonywaniu kolejnych trudności oraz osiąganiu celów daje ogromną dawkę endorfin i poczucie satysfakcji.

Jedną z najpiękniejszych rzeczy w boulderingu jest też społeczność, która go otacza. Wspinacze z różnych środowisk i poziomów umiejętności spotykają się na ścianach, aby wspólnie trenować, motywować się i dzielić swoimi osiągnięciami. Ta atmosfera współpracy i wsparcia sprawia, że bouldering staje się nie tylko sportem, ale także stylem życia.

Jeśli szukasz nowego sposobu na aktywne spędzanie czasu i wyzwanie dla swojego ciała i umysłu, bouldering może być idealnym rozwiązaniem. Niezależnie od tego, czy dopiero zaczynasz swoją przygodę z wspinaczką, czy już jesteś doświadczonym wspinaczem, bouldering zapewni Ci mnóstwo radości, satysfakcji i nowych doświadczeń. Do zobaczenia na ścianie!""",
    },
    {
    'slug': 'rowerki',
    'image': 'rower.jpg',
    'autor': 'Mati',
    'date': date(2023, 7, 4),
    'title': 'Rowerowe przygody',
    'excerpt': 'Nasze wycieczki rowerowe!',
    'content': """Wycieczki rowerowe to nie tylko sposób na zdrowy tryb życia, ale również doskonała okazja do eksploracji najpiękniejszych zakątków naszego otoczenia. Bez względu na to, czy wybieramy się na krótką przejażdżkę po okolicy, czy też na dłuższy wyprawowy wyjazd, każda pedalowana trasa jest pełna niepowtarzalnych widoków, zapierających dech w piersiach.

Jedną z największych zalet wycieczek rowerowych jest ich wszechstronność. Możemy dostosować trasę do naszych preferencji i umiejętności, wybierając zarówno spokojne trasy po równinach, jak i bardziej wymagające trasy górskie. Niezależnie od tego, czy jesteśmy amatorami czy doświadczonymi rowerzystami, zawsze znajdziemy coś odpowiedniego dla siebie.

Warto również podkreślić korzyści zdrowotne płynące z regularnych wycieczek rowerowych. Pedalowanie wzmacnia nasze serce, poprawia kondycję fizyczną i redukuje stres. Dodatkowo, pozwala nam cieszyć się bliskością natury i oddychać świeżym powietrzem, co korzystnie wpływa na nasze samopoczucie i zdrowie psychiczne.

Ale wycieczki rowerowe to nie tylko o zdrowiu i przyrodzie. To także doskonała okazja do spędzenia czasu z rodziną i przyjaciółmi, dzielenia się wspólnymi przeżyciami i tworzenia niezapomnianych wspomnień.

Dlatego jeśli szukasz sposobu na aktywne spędzanie czasu, odkrywanie nowych miejsc i nawiązywanie niezapomnianych doświadczeń, wycieczki rowerowe są idealnym wyborem. Niech każdy kilometr na twoim rowerze będzie nową przygodą i inspiracją do dalszych podróży. Do zobaczenia na szlaku!""",
    },
        {
    'slug': 'rodzicielstwo',
    'image': 'family.jpg',
    'autor': 'Mati',
    'date': date(2024, 6, 25),
    'title': 'Być rodzicem',
    'excerpt': 'Rodzice w akcji',
    'content': """Czy istnieje coś bardziej fascynującego niż obserwowanie, jak Twoje dziecko w wieku czterech lat odkrywa świat wokół siebie? 
        To niesamowite doświadczenie, pełne nieustannych odkryć i niespodzianek. Bycie rodzicem 4-latka to podróż pełna radości, wyzwań i nauki.
        
        Czteroletnie dzieci to małe kuleczki energii, które potrafią zaskoczyć Cię swoją ciekawością i kreatywnością każdego dnia. 
        Ich niewinność i otwartość na świat sprawiają, że nawet najprostsze rzeczy stają się powodem do radości i zdumienia.
        
        Jednocześnie, bycie rodzicem 4-latka to także czas, kiedy musimy nauczyć się radzić sobie z ich rosnącą niezależnością i silną wolą. To okres, w którym zaczynają wyrażać swoje własne preferencje i zdolności, co może być zarówno zachęcające, jak i frustrujące.
        
        Ale mimo wszystkich wyzwań, bycie rodzicem czteroletniego dziecka to niezwykle satysfakcjonujące doświadczenie. To czas, kiedy możemy wspólnie odkrywać świat, uczyć się od siebie nawzajem i budować silne więzi, które będą trwać przez całe życie.
        
        Dlatego też, choć bycie rodzicem 4-latka może być trudne, warto docenić każdą chwilę spędzaną z naszym małym odkrywcą i cieszyć się każdym wspólnie przeżytym momentem.""",
    }
]

def get_date(post):
    return post['date']


def index(request):  # tę nazwę zmienić na starting_page
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts [-3:]

    return render(request, "blog/index.html", {
        'posts': latest_posts
    })

def get_date(post):
    return post['date']


def posts(request):
    return render(request, "blog/posts.html", {
        'all_posts': all_posts
    })


def post_content_by_number(requst, post):  # tej funkcji nie dawał
    posts = list(all_posts.keys())

    if post > len(posts):
        return HttpResponseNotFound('Invalid post number')

    redirect_post = posts[post - 1]
    redirect_path = reverse('post-content', args=[redirect_post])
    return HttpResponseRedirect(redirect_path)


def post_content(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    # try:
        # post_text = all_posts[post]
    return render(request, "blog/post.html", {
        'post': identified_post,
        # 'text': post_text
        })
    # except:
    #     raise Http404()
