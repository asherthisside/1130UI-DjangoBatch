from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    textarea = request.POST['text']
    num_of_letters = len(textarea)
    num_of_words = len(textarea.split(' '))

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    num_of_vowels = 0
    num_of_consonants = 0

    for i in textarea:
        if i in vowels:
            num_of_vowels += 1 
        else:
            num_of_consonants += 1

    print(num_of_letters, num_of_words, num_of_vowels, num_of_consonants)
    
    context = {
        'letters' : num_of_letters,
        'words' : num_of_words,
        'vowels' : num_of_vowels,
        'consonants' : num_of_consonants,
    }
    return render(request, 'result.html', context)