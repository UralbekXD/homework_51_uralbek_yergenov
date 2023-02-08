from random import choices

from django.shortcuts import render


class Cat:
    name = None
    age = 1
    happiness = 10
    fullness = 40
    is_sleeping = False

    @staticmethod
    def eat():
        if not Cat.is_sleeping:
            Cat.fullness += 15
            Cat.happiness += 5

            if Cat.happiness > 100:
                Cat.happiness = 100

            if Cat.fullness < 0:
                Cat.fullness = 0

            if Cat.fullness > 100:
                Cat.fullness = 100
                Cat.happiness -= 30

    @staticmethod
    def play():
        if not Cat.is_sleeping:
            Cat.happiness += 15
            Cat.fullness -= 10
            rand = choices([1, 2, 3], weights=[.3, .3, .3])

            is_angry = False if rand not in (2, 3) else True
            if is_angry:
                Cat.happiness = 0

            if Cat.happiness > 100:
                Cat.happiness = 100
            if Cat.happiness < 0:
                Cat.happiness = 0

            if Cat.fullness < 0:
                Cat.fullness = 0
        else:
            Cat.happiness -= 5
            Cat.is_sleeping = False

    @staticmethod
    def sleep():
        Cat.is_sleeping = True

    @staticmethod
    def set_mood() -> str:
        if Cat.is_sleeping:
            return 'media/sleeping.jpg'

        if Cat.happiness >= 50:
            return 'media/happy.jpg'

        return 'media/angry.jpg'


# Create your views here.
def index(request):
    return render(request, 'index.html')


def stats(request):
    match request.method:
        case 'POST':
            name = request.POST.get('name')
            if name:
                Cat.name = name
        case 'GET':
            action = request.GET.get('action')
            match action:
                case 'play':
                    Cat.play()
                case 'feed':
                    Cat.eat()
                case 'sleep':
                    Cat.sleep()

    context = {
        'name': Cat.name,
        'age': Cat.age,
        'happiness': Cat.happiness,
        'fullness': Cat.fullness,
        'image': Cat.set_mood(),
    }

    return render(request, 'stats.html', context=context)
